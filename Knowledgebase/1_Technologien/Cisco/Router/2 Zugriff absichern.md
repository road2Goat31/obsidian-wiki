Unautorisierten Zugriff über den Konsolenport:
```
Switch(config)# line console 0
Switch(config-line)# password {password}
Switch(config-line)# login
```

Über SSH/Telnet
```
Switch(config)# line vty 0 15
Switch(config-line)# password password
Switch(config-line)# transport input {ssh | telnet | none | all}
Switch(config-line)# login
```

PW verschlüsseln:
`service password-encryption`