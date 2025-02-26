
Python3 installiert?
PIP installiert?

1. git installieren
2. Ansible installieren -> sudo pip3 install --user ansible --break-system-packages
3. tio installieren sudo apt install tio
4. expect installieren pip install expect
5. pip install pexpect


Zielstellung:

- von einem Rasbperry Pi mit Ansible ein Playbook ausführen
- dieses soll einen Switch (befindet sich im Werkszustand) konfigurieren
- es müssen mehrere Ports auf dem KVM-Switch betrachtet werden
- unterschiedliche Hostnamen vergeben werden

Screen: strg-a d -> trennen, strg a K --> beenden


Zu lösende Probleme:

1. wie wird der Switch am Anfang angesprochen (noch kein SSH möglich)
--> SSH wird auf dem Switch per Python-Skript konfiguriert
2. unterschiedliche Hostnamen vergeben (keinen Doppelt)
--> mehrere Skripte anlegen, in denen jeweils der richtige serielle Port aufgerufen wird
![](Anhang/Pasted%20image%2020241101150036.png)
3. Kommunikation über SSH ermöglichen
	--> IP-Adresse vergeben, Nutzer anlegen, SSH aktivieren und SSH-Key erstellen 
4. Konfigurationen sollen eventuell unterschiedlich sein
	--> jeder Port bekommt eine einzelne Rolle -> an jedem Port(somit auch Switch, der daran angeschlossen ist) können dann unterschiedliche Konfigurationen vorgenommen werden

5. Erstellte running-config auf dem Pi speichern
	--> vordefinierten Ordner erstellen
	Beispiel Cisco-Switch:
	![](Anhang/Pasted%20image%2020241101150459.png)

Ablauf:

1. ansible verbindet sich mit Konsolen Server und meldet sich an
   --> sudo apt-get install sshpass wird benötigt
   --> labterm.lab.shd-online muss in der known_hosts-Datei sein
1. screen session eröffnen (connect-port12)
2. python skrip anlaufen lassen


ansible_user=user ansible_password=netlog