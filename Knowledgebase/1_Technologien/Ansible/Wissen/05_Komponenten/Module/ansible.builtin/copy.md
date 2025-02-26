- dient dem kopieren von Dateien

# Datei kopieren

```
- name: Kopiere eine Datei auf den Remote-Host 
  copy: 
    src: /path/to/local/file.txt 
    dest: /path/to/remote/file.txt
```

# Inhalt in eine Datei kopieren

```
- name: Schreibe Inhalt in eine Datei 
  copy: 
    content: "Dies ist eine Beispiel-Konfiguration." 
    dest: /path/to/remote/config.txt
```

# Mit Berechtigungen und Eigentümer (Linux)

```
- name: Kopiere eine Datei mit speziellen Berechtigungen
  copy:
    src: /path/to/local/file.txt
    dest: /path/to/remote/file.txt
    owner: root
    group: root
    mode: '0644'
```