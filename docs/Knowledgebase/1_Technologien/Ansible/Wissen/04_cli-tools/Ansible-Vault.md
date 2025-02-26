Im Ansible-Vault können  Passwörter und  Zertifikate in verschlüsselten Dateien gespeichert werden. 

Erstellen eines Vaults:
```
ansible-vault create secret_vars.yml
```

-> Passwort für das entschlüsseln der Datei festlegen

Ändern des Vault-PW:
```
ansible-vault rekey <dateiname>
```

Dann die Passwort-Variablen definieren:
```
# secret_vars.yml
db_password: "mein-geheimes-passwort"
api_key: "super-geheimer-api-key"
```

Vault editieren:
```
ansible-vault edit <dateiname>
```

Um ein Playbook mit enthaltenen Passwörtern gegen Hosts zu fahren muss folgender Befehl benutzt werden:
```
ansible-playbook playbook.yml --ask-vault-pass
```
und anschließend das PW zum Vault eingegeben werden


Man kann auch mit mehreren PW-Dateien arbeiten:
```
ansible-playbook playbook.yml --vault-id production@prompt --vault-id staging@prompt
```

