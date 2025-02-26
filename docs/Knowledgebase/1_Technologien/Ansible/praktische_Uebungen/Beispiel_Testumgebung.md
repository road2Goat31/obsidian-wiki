# Quelle 
[Getting started with Ansible 01 - Introduction (youtube.com)](https://www.youtube.com/watch?v=3RiVKs8GHYQ&list=PLT98CRl2KxKEUHie1m24-wkyHpEsa4Y70&index=2)

# Umgebung

VMs: 
- MKS-AnsibleHost (maik/mkspasswort)
- MKS-DebianServer1 (maik/mkspasswort, root/sudopasswort)
- MKS-DebianServer2 (maik/mkspasswort, root/sudopasswort)
- MKS-DebianServer3 (maik/mkspasswort, root/sudopasswort)

Was wird benötigt?
- SSH-Client auf dem Ansible-Host
- SSH-Server auf dem Server
- Ansible-Host und Server müssen sich gegenseitig erreichen
- Git
- PIP
- Ansible

# SSH-Keys erstellen

--> Per SSH mit dem Gerät verbinden
--> SSH Key pair erstellten
	`ssh-keygen -t ed25519 -C "maik default"`
	passphrase: mkspasswort  --> Passphrase wird empfohlen
	`ls -la .ssh`  --> Directory mit den Keys anzeigen
	`cat .ssh/id_ed25519.pub`  --> öffentlichen Key anzeigen lassen

--> SSH Key auf den Servern kopieren
	`ssh-copy-id -i ~/.ssh/id_ed25519.pub 172.20.17.2`
	`ssh-copy-id -i ~/.ssh/id_ed25519.pub 172.20.17.3`
	`ssh-copy-id -i ~/.ssh/id_ed25519.pub 172.20.17.4` 

--> Ansible SSH-Key erstellen
	`ssh-keygen -t ed25519 -C "ansible"`
	`enter file: /home/maik/.ssh/ansible`
	`no passphrase`
	
--> auf jeden Host den Ansible-Key kopieren

# Git installieren

Git-Repository angelegt
Settings -> SSH Key ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBgQN6EAAHFF1yik69+edToGgeu5SuHnEcEZqTxidcwf maik default

Auf AnsibleHost:

`apt install git`

`git clone git@github.com:{username}/{repository name}`

--> z.B. README.md ändern

`git diff README.md` -> alle Änderungen sehen

`git add README.add`

`git status` -> alle geänderten Dateien werden angezeigt

`git commit -m "in readme geschrieben"` --> wird für das pushen vom Server vorbereitet 

`git push`

`history` -> alle eingegeben Befehle nachsehen

---

	Installation von Ansible

PIP installieren: 
`sudo apt install python3-pip`
[How to Install Python Pip on Ubuntu 22.04 | Linuxize](https://linuxize.com/post/how-to-install-pip-on-ubuntu-22.04/)

`python3 -pip install --user ansible`

![](Anhang/Pasted%20image%2020250226104011.png)

--> da im Userkontext heruntergeladen -> Skript nicht in der CLI verfügbar
PATH gesetzt: `export PATH=/home/maik/.local/bin:$PATH`
[Quelle](https://www.howtogeek.com/658904/how-to-add-a-directory-to-your-path-in-linux/) 


--> dann ist "ansible" verfügbar zur Verwendung

--> In das Repository wechseln
--> `cd ansible/`
`nano inventory` --> Hosts eintragen

![](Anhang/Pasted%20image%2020250226104026.png)

---
# Ad-hoc-Commands

`ansible all --key-file ~/.ssh/ansible -i inventory -m ping`

--> -m = module
--> -i = Inventory

![](Anhang/Pasted%20image%2020250226104041.png)

**Config-Datei anlegen:**

`/ansible$ nano ansible.cfg`
![](Anhang/Pasted%20image%2020250226104057.png)

Ad-Hoc-Command konnte gekürzt werden
![](Anhang/Pasted%20image%2020250226104119.png)

Alle Hosts auflisten:
![](Anhang/Pasted%20image%2020250226104143.png)

Informationen für Hosts abrufen:

![](Anhang/Pasted%20image%2020250226104158.png)

Bei Ad-hoc-Befehlen, welche Änderungen hervorrufen wird die sudo-Berechtigung benötigt

--> `ansible all -m apt -a update_cache=true --become --ask-become-pass`
=APT-Cache aktualisieren
--> funktioniert nur, wenn auf jedem Knoten das gleiche Sudo-Passwort vergeben wurde

--> zum Sudo machen: über Benutzerverwaltung und einen Systemverwalter erstellen
oder `sudo usermod -aG {username}`

Im folgenden wird man dazu aufgerufen das sudo-Passwort einzugeben
![](Anhang/Pasted%20image%2020250226104219.png)

**mehr zum APT Modul:** [Hier](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html)

Auf allen Knoten vim-nox installieren:

"-a" steht für Argument
![](Anhang/Pasted%20image%2020250226104237.png)

Wenn man es noch einmal eingibt, dann kommt die Meldung, dass keine Änderung vorgenommen wurde, da es schon installiert ist
![](Anhang/Pasted%20image%2020250226104255.png)

neueste Version eines Paketes installieren:
![](Anhang/Pasted%20image%2020250226104310.png)

Alle Pakete upgraden:
![](Anhang/Pasted%20image%2020250226104330.png)

[hw_dungeonisle12a_h_en_173 (youtube.com)](https://www.youtube.com/watch?v=VANub3AhZpI&list=PLT98CRl2KxKEUHie1m24-wkyHpEsa4Y70&index=6)

---
# Playbooks

--> bei Playbooks wird eine Abfolge von Aufgaben abgearbeitet

![](Anhang/Pasted%20image%2020241016081014.png)

- .yml-Dateiformat

Ausführung des Befehls:
![](Anhang/Pasted%20image%2020241016081221.png)

Playbook: Repository Update, Apache und PHP installieren
![](Anhang/Pasted%20image%2020241016082754.png)
Playbook: Apache und PHP löschen
![](Anhang/Pasted%20image%2020241016082731.png)

---

## When-Conditional --> Fehlerbehandlung

--> Gather_facts wird davor benötigt 

![](Anhang/Pasted%20image%2020241016084335.png)

**ODER**

![](Anhang/Pasted%20image%2020241016084551.png)

## Playbooks verbessern

--> mehrere Pakete in eine Aufgabe
![](Anhang/Pasted%20image%2020241016105645.png)

--> Option update_cache mit in die Aufgabe reinnehmen
![](Anhang/Pasted%20image%2020241016105836.png)

Variablen benutzen:
--> Package als generischen Paketmanager

![](Anhang/Pasted%20image%2020241016110805.png)
Variablen in der Inventory-Datei definieren:
![](Anhang/Pasted%20image%2020241016110622.png)


Inventory gruppieren:

![](Anhang/Pasted%20image%2020241016111427.png)

Aufgaben nur auf bestimmte Hostgruppen anwenden:
![](Anhang/Pasted%20image%2020241016113902.png)

**pre_tasks**
--> pre_tasks werden als erstes ausgeführt
![](Anhang/Pasted%20image%2020241016113337.png)

---

## Tags

--> dient dazu nur bestimmte Aufgaben gegen die Knoten laufen zu lassen

![](Anhang/Pasted%20image%2020241017081108.png)
Tags eines Playbooks abfragen:
![](Anhang/Pasted%20image%2020241017075347.png)

Abfragen mit Tags:
![](Anhang/Pasted%20image%2020241017081206.png)
Mehrere Tags:
![](Anhang/Pasted%20image%2020241017082132.png)

---

# Dateien mit Ansible managen

--> Files-Ordner erstellt
![](Anhang/Pasted%20image%2020241017082722.png)

--> Datei in dem Ordner "Files" erstellen

-->Im Playbook das Modul "copy" benutzen:

![](Anhang/Pasted%20image%2020241017083414.png)mode: Berechtigung, welche vergeben wird

--> Kopieren einer Datei aus dem Internet:
![](Anhang/Pasted%20image%2020241017085151.png)

---

# Dienste mit Ansible managen

--> einen Dienst starten und dauerhaft laufen lassen

![](Anhang/Pasted%20image%2020241017092612.png)

--> Zeile in Conf-Datei ändern und Dienst neustarten
![](Anhang/Pasted%20image%2020241017101435.png)
mit Überprüfung, ob "apache2" überhaupt geändert wurde

# Nutzer hinzufügen und Bootstrapping

Mudul "user" wird genutzt:
![](Anhang/Pasted%20image%2020241017102534.png)

SSH-Key hinzufügen und Nutzer Sudo-Rechte geben
![](Anhang/Pasted%20image%2020241017103351.png)
unter /Files abgelegte Datei:
![](Anhang/Pasted%20image%2020241017104042.png)


--> direkt einloggen mit User
--> ansible.cfg bearbeiten
![](Anhang/Pasted%20image%2020241017104810.png)

Funktioniert jetzt ohne Login: --> da User Simone Sudo-Rechte besitzt
![](Anhang/Pasted%20image%2020241017104919.png)


Bei einem neu aufgesetzten Server notwendige Konfigurationen vornehmen (User anlegen, Sudo-Rechte vergeben und SSH-Key hinterlegen) 
--> Bootstrap-Datei

![](Anhang/Pasted%20image%2020241017110230.png)

Danach kann man die boot.yml ohne Passwort ausführen
![](Anhang/Pasted%20image%2020241017110325.png)

---

# Rollen

--> Rollen dienen dazu Playbooks übersichtlich zu halten
--> Ordnerstruktur angelegt
- Rollen-Ordner
- In dem Rollen-Ordner ein Files-, Tasks und Handlers-Ordner
- in der boot.yml wird auf die Rollen verlinkt

![](Anhang/Pasted%20image%2020241017123521.png)

--> Verlinkung auf die Rollen
![](Anhang/Pasted%20image%2020241017120009.png)

---

# Variablen und Handler

## Variablen

 --> einen "host_vars"-Ordner anlegen
 --> für jeden Host eine Datei, wo die Variablen definiert werden
 --> Dateien entweder wie IP-Adresse oder DNS-Name benennen
 ![](Anhang/Pasted%20image%2020241017132000.png)

Definieren der Variablen:
![](Anhang/Pasted%20image%2020241017132437.png)

## Handler

**Ein Handler wird aufgerufen, wenn die Task davor eine Änderung hervorgerufen hat**

--> "handlers"-Ordner hinzufügen
--> darin eine main.yml-Datei
-->in der Task-Datei der Rolle auf den Handler verweisen
![](Anhang/Pasted%20image%2020241017134215.png)

![](Anhang/Pasted%20image%2020241017134027.png)

--> Die main.yml

![](Anhang/Pasted%20image%2020241017134311.png)

# Templates


--> "Templates"-Ordner unter "/ansible/roles/base/" anlegen

--> SSH-Config-Datei des Systems (Debian-Host) auf den Ansible-Host kopieren und unter "/Templates" ablegen

![](Anhang/Pasted%20image%2020241017142305.png)

--> Variable in die SSH-Config-Datei schreiben
![](Anhang/Pasted%20image%2020241017143002.png)

--> Variablen in die Variablen-Datei (im Ordner "host_vars" zu finden) der einzelnen Hosts schreiben
am Bsp. des Hosts 172.20.17.2
--> muss für alle 3 Hosts gemacht werden
![](Anhang/Pasted%20image%2020241017143326.png)

--> in der Datei unter "/ansible/roles/base/tasks/main.yml" eine weitere Aufgabe einfügen
![](Anhang/Pasted%20image%2020241017144917.png)
