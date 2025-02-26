SSH support verifizieren:
`show ip ssh`

IP-Domain festlegen:
`ip domain-name {Domänennamen}`

RSA Schlüsselpaar erstellen:
```
crypto key generate rsa
modulus 1024
username {Benutzername} secret {Passwort}
line vty 0 15
transport input ssh
login local
exit

ip ssh version 2
```

RSA-Schlüssel löschen:
`crypto key zeroize rsa`