# Playbooks

- sind Automatisierungsskripte in Ansible

- sind in **YAML** geschrieben

- enthält eine oder mehrere **Plays**, die auf Hosts ausgeführt werden

- ein Play beschreibt Aufhaben (**Tasks**), welche auf bestimmten Hosts ausgeführt werden

- ermöglichen die Automatisierung von IT-Aufgaben wie Installation, Konfiguration und Verwaltung

- können wiederverwendbar und strukturierbar erstellt werden, um eine konsistente Infrastruktur zu gewährleisten.

# Tasks

- enthält eine oder mehrere Anweisungen, welche auf dem Remote-Host ausgeführt werden sollen

```
- name: Installiere Apache 
  apt:                               # Modul wird aufgerufen
    name: apache2                    # Apache2 installiert
    state: present                   # aktuelle Verison
```

# Handlers

- sind Aufgaben, die vorher durch andere Tasks aufgerufen (benachrichtigt)  
  werden --> durch `notify:`

```
- name: Ändere Konfigurationsdatei 
  template: 
  src: httpd.conf.j2 
  dest: /etc/httpd.conf 
  notify: 
    - Starte Apache neu
    
handlers: 
  - name: Starte Apache neu
    service:                        # Modul wird aufgerufen
      name: apache2 
      state: restarted
```

# Inventory

- beschreibt die Hosts und Gruppen von Hosts, auf denen Ansible Aufgaben ausführt

- kann als **statische Datei** (z. B. `hosts`-Datei) oder als **dynamische Quelle** (z. B. aus einer Cloud-Umgebung) vorliegen

- In einem **statischen Inventory** können Hosts direkt oder in Gruppen organisiert werden

- **Gruppen** ermöglichen es, Hosts zu kategorisieren (z. B. Webserver, Datenbank-Server)

- Variablen können auf Hosts oder Gruppen angewendet werden (mit `vars:`)

```
all: 
  children:                 # damit werden Untergruppen gebildet
    webservers:             # 1. Untergruppe
      hosts: 
        web1.example.com:   # Hosts der ersten Untergruppe
        web2.example.com:
      vars: http_port:      # Variablen, die für alle Hosts der Gruppe 
        80 max_clients:     # "webservers" gelten
        200 dbservers:
       
      hosts: 
        db1.example.com: 
        db2.example.com: 
      vars: 
        db_port: 3306 
        db_user: admin
```

# Rollen

- sind wiederverwendbare Einheiten in Ansible, die Aufgaben, Variablen, Dateien, Templates und Handlers gruppieren

- Bsp.: 
```
└── roles
    ├── role1
    │   ├── defaults
    │   ├── files
    │   │   └── file1
    │   ├── handlers
    │   ├── library
    │   ├── lookup_plugins
    │   ├── meta
    │   ├── module_utils
    │   ├── tasks
    │   │   └── main.yml
    │   ├── templates
    │   └── vars
    └── role2
        └── tasks
            └── main.yml

```


# Module

- sind die Bausteine in Ansible, die bestimmte Aufgaben auf Remote-Hosts ausführen   (z. B. Pakete installieren, Dateien kopieren, Benutzer anlegen)

- führt eine spezifische Funktion aus und wird innerhalb eines Playbooks oder einer Rolle aufgerufen

- Beispiele: `apt`, `yum`, `copy`, `service`, `user`

```
- name: Installiere Apache 
  apt:                               # Modul wird aufgerufen
    name: apache2                    # Apache2 installiert
    state: present                   # aktuelle Verison
```

- Alle Module und Informationen dazu: [All modules — Ansible Documentation](https://docs.ansible.com/ansible/2.9/modules/list_of_all_modules.html)

# Plugins

- Plugins erweitern die Funktionalität von Ansible und ermöglichen die Integration zusätzlicher Features oder Dienste

- Sie werden Systemweit oder mit im Projektverzeichnis gespeichert:
	- Systemweit `/usr/share/ansible/plugins/`
	- im Projekt: `<project>/plugins/
		- dann muss in der ansible.cfg darauf verwiesen werden   
		 `plugin_paths = /path/to/custom/plugins`
	
- verschiedene Arten von Plugins:
	- Connection Plugins (wie Ansible mit Remote-Systemen kommuniziert)
	- Action Plugins
	- Inventory Plugins
	- ...
	
- Alle vorhandenen Plugins und Informationen zu diesen: [Using Ansible modules and plugins — Ansible Community Documentation](https://docs.ansible.com/ansible/latest/module_plugin_guide/index.html)

# Variablen

- **Definition**: Variablen sind Platzhalter, die in Ansible verwendet werden, um dynamische Werte zu speichern und zu verwenden (z. B. für Hosts, Konfigurationen oder Passwörter)

- **Arten von Variablen**:
    - **Host-Variablen**: Spezifische Werte für einzelne Hosts im Inventory/host_vars-Verzeichnis
    - **Gruppen-Variablen**: Werte, die für alle Hosts in einer Gruppe gelten (im group_vars-Verzeichnis)
    - **Playbook-Variablen**: Variablen, die direkt in Playbooks definiert werden.
    - **Fakten (Facts)**: Automatisch ermittelte Systeminformationen, z. B. IP-Adressen oder Betriebssystemversionen.
    - **Einzelne Variablen**: Zuweisung direkt in Playbooks oder Rollen.
    
- **Zugriff**: Variablen werden mit `{{ variable_name }}` innerhalb von Playbooks referenziert.

- **Reihenfolge der Präzedenz**: Ansible verwendet eine spezifische Reihenfolge, um Variablen aufzulösen (z. B. Variable in Playbook überschreibt Group-Variable).

- **Verwendung**: Ermöglicht Flexibilität und Wiederverwendbarkeit von Playbooks und Rollen.

# Collections

- **Definition**: Collections sind Sammlungen von Ansible-Inhalten, wie Modulen, Plugins, Rollen und Playbooks, die zusammen in einem Paket organisiert sind

- **Zweck**: Sie ermöglichen eine einfache Distribution und Wiederverwendung von Ansible-Inhalten

- **Inhalt einer Collection**:
    - **Module**: Erweitern die Funktionalität von Ansible.
    - **Rollen**: Bieten vordefinierte Automatisierungsaufgaben.
    - **Plugins**: Erweiterungen für Verbindung, Filter, Lookup usw.
    - **Playbooks**: Fertige Automatisierungslösungen.
    
- zur Installation und Verwendung siehe: [Installation und Verwendung](../05_Komponenten/Collections/Installation%20und%20Verwendung.md)
