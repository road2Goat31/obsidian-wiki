import os
import subprocess
import yaml
import re

# Konfiguration
IGNORED_FOLDERS = {".obsidian", "3_Vorlagen", "4_Test"}
BASE_DIR = "docs/Knowledgebase"
MKDOCS_YML = "mkdocs.yml"
REMOVE_PREFIX_FROM = {"1_Technologien", "2_Aufgaben", "5_Belegarbeit"}

# Standardkonfiguration für mkdocs.yml
DEFAULT_CONFIG = {
    "site_author": "Maik Käseberg",
    "site_name": "Knowledgebase",
    "theme": {
        "name": "material",
        "custom_dir": "docs/overrides",
        "font": False,
        "favicon": "icon/icon.ico",
        "logo": "icon/icon.png",
        "icon": {"admonition": {"info": "material/alarm"}},
        "palette": [
            {
                "media": "(prefers-color-scheme: light)",
                "scheme": "default",
                "primary": "#00305d",
                "accent": "#255f8b",
                "toggle": {
                    "icon": "material/toggle-switch-off-outline",
                    "name": "Switch to dark mode"
                }
            },
            {
                "media": "(prefers-color-scheme: dark)",
                "scheme": "slate",
                "primary": "#00305d",
                "accent": "#255f8b",
                "toggle": {
                    "icon": "material/toggle-switch",
                    "name": "Switch to light mode"
                }
            }
        ],
        "features": [
            "navigation.top", "navigation.tabs", "navigation.instant",
            "navigation.sections", "toc.integrate", "content.tabs",
            "content.code.copy", "content.code.annotate", "content.action.edit",
            "content.action.view", "search.suggest", "search.highlight",
            "search.share", "navigation.footer", "navigation.indexes",
            "navigation.tracking", "navigation.path", "content.tooltips"
        ]
    },
    "extra": {
        "social": [
            {"icon": "fontawesome/brands/github", "link": "https://github.com/road2Goat31/obsidian-wiki"}
        ],
        "generator": False
    },
    "extra_css": ["css/extra.css"],
    "extra_javascript": ["js/print-button.js"],
    "plugins": ["search"]
}

def clean_name(name, remove_prefix=True):
    """Entfernt numerische Präfixe (z. B. '1_') nur, wenn remove_prefix=True."""
    name = name.strip()
    if remove_prefix:
        match = re.match(r"^\d+_(.+)", name)
        return match.group(1) if match else name  
    return name

def scan_directory(base_dir):
    """
    Scannt das Verzeichnis und erstellt eine geschachtelte Struktur.
    Entfernt Präfixe nur in der obersten Ebene.
    """
    structure = {}

    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in IGNORED_FOLDERS]
        md_files = sorted(f for f in files if f.endswith(".md"))
        
        if md_files or dirs:
            rel_path = os.path.relpath(root, BASE_DIR)
            path_parts = rel_path.split(os.sep)

            # Entferne Präfixe nur auf der obersten Ebene
            section = [
                clean_name(part, remove_prefix=(i == 0)) 
                for i, part in enumerate(path_parts) if part
            ]

            if section and section[0] in REMOVE_PREFIX_FROM:
                section[0] = clean_name(section[0])

            if not section or section == ["."]:
                continue

            current_level = structure
            for part in section:
                current_level = current_level.setdefault(part, {})

            for md_file in md_files:
                file_name = clean_name(os.path.splitext(md_file)[0], remove_prefix=False)
                final_path = "Knowledgebase/" + os.path.join(rel_path, md_file).replace("\\", "/")
                current_level[file_name] = final_path

    structure.pop(".", None)
    return structure

def convert_to_yaml_list(data):
    """Konvertiert ein geschachteltes Dictionary in eine formatierte YAML-Liste."""
    if isinstance(data, dict):
        return [{key: convert_to_yaml_list(value)} for key, value in data.items()]
    return data

def update_mkdocs_yml():
    """
    Aktualisiert mkdocs.yml und stellt sicher, dass die Default-Konfiguration vor dem
    nav-Bereich steht – in der gewünschten Reihenfolge.
    """
    if not os.path.exists(MKDOCS_YML):
        print("⚠️ mkdocs.yml nicht gefunden. Erstelle neue Datei mit Standardwerten.")
        config = DEFAULT_CONFIG.copy()
    else:
        with open(MKDOCS_YML, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}

    # Fehlende Standardwerte ergänzen
    for key, value in DEFAULT_CONFIG.items():
        if key not in config:
            config[key] = value

    # Navigation generieren
    structure = scan_directory(BASE_DIR)
    new_nav = convert_to_yaml_list(structure)
    if not new_nav:
        print("⚠️ Keine Markdown-Dateien gefunden! Navigation bleibt leer.")
        return

    # Füge index.md (Home) immer als ersten Eintrag hinzu
    new_nav.insert(0, {"Home": "index.md"})
    config["nav"] = new_nav

    # Stellen sicher, dass extra_javascript enthalten ist
    if "extra_javascript" not in config:
        config["extra_javascript"] = ["js/print-button.js"]
    elif "js/print-button.js" not in config["extra_javascript"]:
        config["extra_javascript"].append("js/print-button.js")

    # Reihenfolge erzwingen
    ordered_keys = ["site_author", "site_name", "theme", "extra", "extra_css", "extra_javascript", "plugins", "nav"]
    ordered_config = {key: config[key] for key in ordered_keys if key in config}

    # Pfade korrigieren
    config["theme"]["custom_dir"] = config["theme"]["custom_dir"].replace("\\", "/")

    with open(MKDOCS_YML, "w", encoding="utf-8") as f:
        yaml.dump(ordered_config, f, allow_unicode=True, default_flow_style=False, indent=4, sort_keys=False)

    print("✅ mkdocs.yml erfolgreich aktualisiert!")

if __name__ == "__main__":
    update_mkdocs_yml()

    print("📦 Installiere benötigte Python-Pakete...")
    subprocess.run(["pip", "install", "mkdocs", "mkdocs-material"], check=True)

    print("🔧 Baue die MkDocs-Dokumentation...")
    subprocess.run(["mkdocs", "build"], check=True)

    print("🚀 Starte Deployment...")
    subprocess.run(["mkdocs", "gh-deploy", "--force"], check=True)

    print("✅ Deployment abgeschlossen!")
