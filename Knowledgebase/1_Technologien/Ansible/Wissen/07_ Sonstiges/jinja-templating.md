# Jinja

- verwendete Jinja-Version ausgeben via
	- `ansible --version`
- ermöglicht das Verwenden von Platzhaltern
	- `{{ some_name }}`
- semantische Ersetzungen werden rekursiv in der gesamten Datei gesucht

> **Warning:** Folgendes führt zu Endlosschleife

```
a = {{ b + 'foo' }}
b = {{ a + 'bar' }}
```

## Filter

- Filter können via `|` auf Variable angewendet werden

### default

#### value

- [Jinja: default](https://tedboy.github.io/jinja2/templ14.html#default)
- `{{ var | default('default_value') }}`
	- setzt Wert, wenn:
		- Variable nicht gesetzt ist
	- **gilt nicht für leere Variablen e.g. `""`**
- `{{ var | default('default_value', true) }}`
	- setzt Wert, wenn:
		- Variable nicht gesetzt
		- Variable validiert zu `false` (z.B. leerer String)

#### empty list

- wenn für einen Host z.B. keine Liste an Daten für einen Eintrag hinterlegt ist
	- z.B. `vars_list` als `var` für Host erwartet aber nicht vorhanden

```
vars_list:
  - foo
  - bar
```

- `{{ vars_list | default([]) }}`
	- gibt leere Liste zurück
	- damit werden keine Tasks ausgeführt
	- vermeidet ein Fail wegen falschem Datentyp (`List != None`)

```
- name: Some Task
  ...
  loop: "{{ vars_list | default([]) }}"
```

### flatten

- geschachtelte Listen in einfach Liste überführen
- `{{ [a, b, [c, d], e] | flatten }} => [a, b, c, d, e]`

### subelements

- verschachtelte Listen werden auf eine Ebene gedrückt
	- es ist pro Task nur ein Schleifendurchgang angedacht
- Elementzugriff über
	- `item[0]`
		- für äußere Schleife
	- `item[1]`
		- für innere Schleife
	- `item[0]` und `item[1]` werden je Schleifendurchlauf wiederholt

```
array:
	- name: foo_1
	  property: value
	  elements:
		- name: bar_1_1
		- name: bar_1_2
	- name: foo_2
	  property: value
	  elements:
		- name: bar_2_1
		- name: bar_2_2
	# gets filtered out by skip_missing
	- name: foo_no_elements
```

- Anwendung in Task

```
- name: Nested Loop Task
  some_module:
    #                == foo_1
    parameter_1: "{{ item[0].name }}"
    #                == bar_1_1
    parameter_2: "{{ item[1].name }}"
  loop: {{ array | subelements('elements', {'skip_missing': true}) | default([]) }}
```

### selectattr

- Subelement aus Liste herausziehen