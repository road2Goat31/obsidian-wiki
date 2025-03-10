``configure Terminal``
``hostname {Hostanme}``
`enable secret {Passwort}`     --> Login mit Authentifizierung
`line console 0`               
`password {Passwort}`
`login`
`exit`
`line vty 0 4`                 --> 5 virtuelle Interfaces öffnen / bei neueren sind es 16
`password {Passwort}`
`login`
`transport input {ssh | telnet | none | all}`
`exit`
`service password-encryption`  --> Verschlüsselung des Passworts

# Erstellen eines Banners:

``banner motd #Nur authorisierter Zugriff!#``

# Konfiguration Speichern

``copy running-config startup-config``

# Passwörter
![](Anhang/Pasted%20image%2020250310080332.png)



