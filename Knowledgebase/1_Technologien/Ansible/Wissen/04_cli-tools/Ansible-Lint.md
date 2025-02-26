# ansible-lint

- Doku von Lint: [ansible-lint](https://ansible.readthedocs.io/projects/lint/)
- Lint ist ein Werkzeug für:
	- Überprüfung von Playbooks, Rollen und Tasks
	- potentielle Fehlererkennung
	- Verbesserung der Qualität und Lesbarkeit eines Ansible Projektes
	- Sicherstellung von fehlerfreiem und wartbarem Code
- wird durch das [Ansible-Plugin für VSCode](https://marketplace.visualstudio.com/items?itemName=redhat.ansible) direkt unterstützt
	- durch die Installation vom Ansible-Plugin wird automatisch auf Fehler hingewiesen
- kann für CI/CD-Pipelines benutzt werden



## Install

```
pip3 install --user ansible-lint
```

# Using

```
ansible-lint --help
```

```
ansible-lint <playbook.yml>
```
--> gibt eine Liste an Verbesserungsvorschlägen für das gesamte Playbook

```
ansible-lint roles/
```
--> gibt eine Liste an Verbesserungsvorschlägen für alle Rollen

# Erstellung einer `.ansible-lint.yml`

- In dieser können bestimmte Regeln bei der Überprüfung ausgeschlossen werden
- eigene Regeln einbezogen werden

# benutzerdefinierte Regeln

- eigenes Lint-Rege-Verzeichnis erstellen
- die Regeln als Python-Dateien darin ablegen
	- Beispiel von ChatGPT:
```
from ansiblelint.rules import AnsibleLintRule 

class CustomRule(AnsibleLintRule): 

	id = 'EXTRA001' 
	shortdesc = 'Custom rule to enforce something specific'
	description = 'Detailed description of the rule' 
	tags = ['custom']
	
	def matchtask(self, file, task): 
		return 'custom_key' in task
```
- in der ansible-lint.yml darauf verweisen
```
rulesdir:
	- ./custom_rules
```