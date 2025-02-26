
| Befehl | Beschreibung
| ------- | ---------------
| ansible all --key-file ~/.ssh/ansible -i inventory -m ping | Ping auf alle Geräte im Inventory
|ansible all --list-hosts |                        Alle Hosts auflisten
|ansible all -m gather_facts |                 Daten von Hosts abrufen
|ansible all -m gather_ facts --limit {IP-Adresse}| Datensammlung auf bestimmte Geräte begrenzen
|ansible-playbook --ask-become-pass {Playbookname} | Playbook gegen Knoten laufen lassen
|ansible-playbook --tags {Tag} --ask-become-pass {Playbookname} | Aufgaben eines Playbooks mit bestimmten Tag gegen die Knoten laufen lassen
|ansible-playbook --list-tags {Playbookname} | Tags eines Playbooks auflisten
| ansible all -m gather_ facts --limit {IP-Adresse} \| grep ansible_dustribution |  Betriebssystem eines bestimmten Knotens

## Parameter

- **Checkmode**
	- `-C`
		- Aktionen nicht durchführen
		- geplante Aktion ausgeben

```
ansible -C -m file ...
```

- **Step**
	- `--step`
		- zum Debugging für schrittweises durchgehen der Tasks

