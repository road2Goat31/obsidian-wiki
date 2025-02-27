import os
import yaml
import re

# Konfiguration: Ignorierte Ordner & Ordner, bei denen Präfixe entfernt werden
IGNORED_FOLDERS = {".obsidian", "3_Vorlagen", "4_Test"}
BASE_DIR = "docs/Knowledgebase"
MKDOCS_YML = "mkdocs.yml"

# Hauptkategorien, bei denen Nummern entfernt werden
REMOVE_PREFIX_FROM = {"1_Technologien", "2_Aufgaben", "5_Belegarbeit"}

def clean_name(name):
    """Entfernt numerische Präfixe (z. B. '1_') und korrigiert Leerzeichen."""
    name = name.strip()  # Eventuelle führende/trailing Leerzeichen entfernen
    match = re.match(r"^\d+_(.+)", name)
    return match.group(1) if match else name  # Entfernt nur Zahlen-Präfixe

def scan_directory(base_dir):
    """Scannt das Verzeichnis und erstellt eine geschachtelte Struktur für mkdocs.yml."""
    structure = {}

    print(f"📂 Durchsuche das Verzeichnis: {base_dir}")

    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in IGNORED_FOLDERS]

        md_files = sorted(f for f in files if f.endswith(".md"))
        if md_files or dirs:
            rel_path = os.path.relpath(root, BASE_DIR)
            section = [clean_name(part) for part in rel_path.split(os.sep) if part]

            current_level = structure
            for part in section:
                current_level = current_level.setdefault(part, {})

            for md_file in md_files:
                file_name = clean_name(os.path.splitext(md_file)[0])  # Auch für Dateien Namen bereinigen
                current_level[file_name] = os.path.join(rel_path, md_file).replace("\\", "/")

    print(f"📄 Gefundene Struktur: {structure}")
    return structure

def build_nav_structure(structure):
    """Konvertiert die gescannte Ordnerstruktur in das NAV-Format von mkdocs."""
    def build_recursive(node):
        nav = []
        for key, value in sorted(node.items()):
            if isinstance(value, dict):
                sub_nav = build_recursive(value)
                if sub_nav:
                    nav.append({key: sub_nav})
            else:
                nav.append({key: value})
        return nav

    nav_structure = build_recursive(structure)
    return nav_structure

def update_mkdocs_yml():
    """Aktualisiert die mkdocs.yml Datei mit der neuen Navigationsstruktur."""
    if not os.path.exists(MKDOCS_YML):
        print(f"❌ Fehler: mkdocs.yml nicht gefunden unter {MKDOCS_YML}")
        return

    with open(MKDOCS_YML, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    new_nav = build_nav_structure(scan_directory(BASE_DIR))
    if not new_nav:
        print("⚠️ Keine Markdown-Dateien gefunden! Navigation bleibt leer.")
        return

    # Entfernt den Punkt-Eintrag, falls vorhanden
    new_nav = [entry for entry in new_nav if not (isinstance(entry, dict) and "." in entry)]

    config["nav"] = new_nav

    with open(MKDOCS_YML, "w", encoding="utf-8") as f:
        yaml.dump(config, f, allow_unicode=True, default_flow_style=False, sort_keys=False, indent=4)

    print("✅ mkdocs.yml erfolgreich aktualisiert!")

if __name__ == "__main__":
    update_mkdocs_yml()
