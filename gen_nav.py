import os
import yaml
import re

# Konfiguration
IGNORED_FOLDERS = {".obsidian", "3_Vorlagen", "4_Test"}
BASE_DIR = "docs/Knowledgebase"
MKDOCS_YML = "mkdocs.yml"

REMOVE_PREFIX_FROM = {"1_Technologien", "2_Aufgaben", "5_Belegarbeit"}

# Standardkonfiguration
DEFAULT_CONFIG = {
    "site_name": "Knowledgebase",
    "site_author": "Maik Käseberg",
    "theme": {
        "name": "material",
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
            "navigation.tracking", "navigation.path", "content.tooltips",
            "palette"
        ]
    },
    "extra_css": ["css/extra.css"],
    "extra": {
        "social": [
            {"icon": "fontawesome/brands/github", "link": "https://github.com/road2Goat31/obsidian-wiki"}
        ],
        "generator": False
    }
}

def clean_name(name, parent=None):
    """Entfernt numerische Präfixe aus Datei- und Ordnernamen."""
    name = name.strip()
    
    # Falls der übergeordnete Ordner in REMOVE_PREFIX_FROM ist, entferne das Präfix
    if parent and parent in REMOVE_PREFIX_FROM:
        name = re.sub(r"^\d+_", "", name)
    else:
        match = re.match(r"^\d+_(.+)", name)
        name = match.group(1) if match else name  

    return name

def scan_directory(base_dir):
    """Scannt das Verzeichnis und erstellt eine geschachtelte Navigationsstruktur."""
    structure = {}

    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in IGNORED_FOLDERS]

        md_files = sorted(f for f in files if f.endswith(".md"))
        if md_files or dirs:
            rel_path = os.path.relpath(root, BASE_DIR)
            path_parts = rel_path.split(os.sep)

            # Falls das Verzeichnis ignoriert werden soll, weiter zur nächsten Iteration
            if not path_parts or path_parts == ["."]:
                continue  

            cleaned_parts = [clean_name(part, path_parts[0]) for part in path_parts]

            # Struktur schrittweise aufbauen
            current_level = structure
            for part in cleaned_parts:
                current_level = current_level.setdefault(part, {})

            # Markdown-Dateien hinzufügen
            for md_file in md_files:
                file_name = clean_name(os.path.splitext(md_file)[0])
                current_level[file_name] = os.path.join(rel_path, md_file).replace("\\", "/")

    structure.pop(".", None)  # Falls "." als Schlüssel existiert, löschen
    return structure

def convert_to_yaml_list(data):
    """Konvertiert eine geschachtelte Struktur in eine YAML-Formatierte Liste."""
    if isinstance(data, dict):
        return [{key: convert_to_yaml_list(value)} for key, value in data.items()]
    return data

def yaml_dump_custom(data, indent=0):
    """Erstellt eine YAML-Darstellung mit genau 4 Leerzeichen pro Einrückung."""
    yaml_str = ""
    space = " " * indent
    if isinstance(data, list):
        for item in data:
            for key, value in item.items():
                yaml_str += f"{space}- {key}:\n{yaml_dump_custom(value, indent + 4)}"
    elif isinstance(data, dict):
        for key, value in data.items():
            yaml_str += f"{space}{key}:\n{yaml_dump_custom(value, indent + 4)}"
    else:
        yaml_str += f"{space}- {data}\n"
    return yaml_str

def update_mkdocs_yml():
    """Aktualisiert oder erstellt mkdocs.yml mit korrekter Navigationsstruktur."""
    # Falls mkdocs.yml nicht existiert, eine neue Datei mit Standardwerten erstellen
    if not os.path.exists(MKDOCS_YML):
        print(f"⚠️ mkdocs.yml nicht gefunden. Erstellt eine neue Datei mit Standardwerten.")
        config = DEFAULT_CONFIG.copy()
    else:
        with open(MKDOCS_YML, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}

    # Fehlende Standardwerte setzen
    for key, value in DEFAULT_CONFIG.items():
        if key not in config:
            config[key] = value

    # Navigation generieren
    structure = scan_directory(BASE_DIR)
    new_nav = convert_to_yaml_list(structure)

    if not new_nav:
        print("⚠️ Keine Markdown-Dateien gefunden! Navigation bleibt leer.")
        return

    config["nav"] = new_nav  

    with open(MKDOCS_YML, "w", encoding="utf-8") as f:
        yaml.dump(config, f, allow_unicode=True, default_flow_style=False, indent=4)

    print("✅ mkdocs.yml erfolgreich aktualisiert!")

if __name__ == "__main__":
    update_mkdocs_yml()
