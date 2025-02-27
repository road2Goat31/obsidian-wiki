import os
import yaml
import re

# Konfiguration
IGNORED_FOLDERS = {".obsidian", "3_Vorlagen", "4_Test"}
BASE_DIR = "docs/Knowledgebase"
MKDOCS_YML = "mkdocs.yml"

REMOVE_PREFIX_FROM = {"1_Technologien", "2_Aufgaben", "5_Belegarbeit"}

def clean_name(name):
    """Entfernt numerische Präfixe (z. B. '1_') und korrigiert Leerzeichen."""
    name = name.strip()
    match = re.match(r"^\d+_(.+)", name)
    return match.group(1) if match else name  

def scan_directory(base_dir):
    """Scannt das Verzeichnis und erstellt eine geschachtelte Struktur."""
    structure = {}

    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in IGNORED_FOLDERS]

        md_files = sorted(f for f in files if f.endswith(".md"))
        if md_files or dirs:
            rel_path = os.path.relpath(root, BASE_DIR)
            section = [clean_name(part) for part in rel_path.split(os.sep) if part]

            # Leeren Eintrag verhindern!
            if not section or section == ["."]:
                continue  

            current_level = structure
            for part in section:
                current_level = current_level.setdefault(part, {})

            for md_file in md_files:
                file_name = clean_name(os.path.splitext(md_file)[0])
                current_level[file_name] = os.path.join(rel_path, md_file).replace("\\", "/")

    #  Falls "." als Schlüssel existiert, löschen
    structure.pop(".", None)  

    return structure

def convert_to_yaml_list(data):
    """Konvertiert ein geschachteltes Dictionary in eine formatierte YAML-Liste."""
    if isinstance(data, dict):
        return [{key: convert_to_yaml_list(value)} for key, value in data.items()]
    return data

def yaml_dump_custom(data, indent=0):
    """Erstellt eine YAML-Darstellung mit exakt 4 Leerzeichen pro Einrückung."""
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
    """Aktualisiert mkdocs.yml mit korrekter Einrückung."""
    if not os.path.exists(MKDOCS_YML):
        print(f"❌ Fehler: mkdocs.yml nicht gefunden unter {MKDOCS_YML}")
        return

    with open(MKDOCS_YML, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    structure = scan_directory(BASE_DIR)
    new_nav = convert_to_yaml_list(structure)

    if not new_nav:
        print("⚠️ Keine Markdown-Dateien gefunden! Navigation bleibt leer.")
        return

    config["nav"] = new_nav  

    with open(MKDOCS_YML, "w", encoding="utf-8") as f:
        f.write("nav:\n" + yaml_dump_custom(new_nav, 4))

    print("✅ mkdocs.yml erfolgreich aktualisiert mit korrekter Einrückung!")

if __name__ == "__main__":
    update_mkdocs_yml()
