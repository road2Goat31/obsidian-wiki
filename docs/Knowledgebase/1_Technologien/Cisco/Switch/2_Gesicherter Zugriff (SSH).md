``show ip ssh``           -> überprüfen, ob Gerät SSH-fähig ist

``ip domain name {Domäne}``

``crypto key generate rsa``
-> 1024

``username {Nutzername} seceret {Passwort}``

**VTY Lines:**

-> sind virtuelle Interafaces und legen fest, wie viele Admins gleichzeit per SSH auf den Switch zugreifen können

``line vty 0 15``     -> alle 16 Kanäle offen
``transport input ssh``
``login local``         -> lokale Authentifikation erforderlich machen 
``exit``

**SSH Version 2:**

``ip ssh version 2``

