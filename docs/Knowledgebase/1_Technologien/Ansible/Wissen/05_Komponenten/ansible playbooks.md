# Playbooks

```
---
- name: My Playbook
```

## Playbooks in andere Playbooks importieren

-> dient dazu, dass am entscheiden kann, ob man alle Playbooks auf einmal oder nur einzelne laufen lassen möchte

-> Playbook zum zusammenführen
```
---
# file: site.yml
- import_playbook: webservers.yml
- import_playbook: dbservers.yml
```

-> einzelnes Playbook, welches Rollen aufruft
```
---
# file: webservers.yml
- hosts: webservers
  roles:
    - common
    - webtier
```
## Jinja

- via `{{ }}` gekennzeichnet
- Parameter in Modulen wechseln teilweise automatisch in den Jinja-Mode
	- `{{ }}` nicht mehr notwendig
	- z.B: [assert](#assert)
- weiter Infos siehe [jinja-templating](../07_%20Sonstiges/jinja-templating.md)

## limit

- `-l` Ausführung auf Hosts oder Gruppen beschränken
- `default(omit)`
	- wenn var nicht gesetzt ist, wird die Zeile auskommentiert
	- nützlich um versehentliches Ausführen auf allen Nodes im Inventory zu verhindern

```
hosts: "{{ ansible_limit | default(omit) }}"
```

## Tasks

### name

- beschreibt normale Tasks in einem Play
- innerhalb "normaler" Tasks werden [Modules](#Modules) verwendet

```
- name: Some Task
  ...
```

### set_fact

- definieren eigener Variablen direkt im Play

```
- set_fact:
  new_var_foo: "my_new_entry"
  new_var_bar: "{{ "abc" | replace("a","c") }}"
```

### pause

- unterbricht die Ausführung eines Plays
	- kann zum interaktiven Abfragen via prompt genutzt werden

### fail

- Abbruch des Playbooks
	- in Kombination mit `when`

```
- fail:
  msg: "Some Message"
  when: 
```

### assert

- validieren von gegebenen Variablen
	- `Fail` für Play wenn Test fehlschlägt
	- gibt explizit fehlgeschlagenen Task aus

```
- assert:
  that:
    - some_var is defined
```

## Modules

- werden innerhalb eines Tasks verwendet

#### assert

- validieren von gegebenen Variablen
	- `Fail` für Task wenn Test fehlschlägt (wenn in Task verwendet)
	- gibt explizit fehlgeschlagenen Task aus

```
- name: Task with assertions
  ...
  assert:
    that:
      - some_var is defined
      - some_var | int < 1000
```

#### debug

- verboses Ausgeben von Variablen

```
- name: Debug Task
  debug:
    var: vars
    # Ausgeben, wenn -vv
    verbosity: 2
```

#### pause

- Ausführung des Tasks pausieren

#### include_tasks

- Tasks aus externer `YML` laden

##### Tags

- im task können `Tags` vergeben werden
	- (auf Task-Ebene)

```
- name: Some Task
  tags: <some_tag>
```

- **Ausführen** nur bestimmter Tags

```
ansible-playbook --tags <tag> [, <tag>]
```

- **Auslassen** bestimmter Tags

```
ansible-playbook --skip-tags <tag> [, <tag>]