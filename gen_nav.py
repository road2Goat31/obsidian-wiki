import os
import yaml

# Konfiguration: Ignorierte Ordner
IGNORED_FOLDERS = {".obsidian", "3_Vorlagen", "4_Test"}
BASE_DIR = "Knowledgebase"
MKDOCS_YML = "mkdocs.yml"

def scan_directory(base_dir):
    """Scannt das Verzeichnis und erstellt eine geschachtelte Struktur für mkdocs.yml."""
    structure = {}
    
    for root, dirs, files in os.walk(base_dir):
        # Entferne ignorierte Ordner aus der Suche
        dirs[:] = [d for d in dirs if d not in IGNORED_FOLDERS]
        
        md_files = [f for f in files if f.endswith(".md")]
        if md_files:
            rel_path = os.path.relpath(root, BASE_DIR)
            section = rel_path.split(os.sep)
            
            current_level = structure
            for part in section:
                current_level = current_level.setdefault(part, {})
            
            for md_file in md_files:
                file_name = os.path.splitext(md_file)[0]
                current_level[file_name] = os.path.join(rel_path, md_file)
                
    return structure

def build_nav_structure(structure):
    """Konvertiert die gescannte Ordnerstruktur in das NAV-Format von mkdocs."""
    def build_recursive(node):
        result = []
        for key, value in sorted(node.items()):
            if isinstance(value, dict):
                result.append({key: build_recursive(value)})
            else:
                result.append({key: value})
        return result
    
    return build_recursive(structure)

def update_mkdocs_yml():
    """Aktualisiert die mkdocs.yml Datei mit der neuen Navigationsstruktur."""
    with open(MKDOCS_YML, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    config["nav"] = build_nav_structure(scan_directory(BASE_DIR))
    
    with open(MKDOCS_YML, "w", encoding="utf-8") as f:
        yaml.dump(config, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    
    print("✅ mkdocs.yml erfolgreich aktualisiert!")

if __name__ == "__main__":
    update_mkdocs_yml()
