Schritt                                | Aktion |
----                                     | -----|
DHCP Discover                  | Broadcast in das Netz (Suche nach DHCP-Servern)
DHCP Offer                       | Ein oder mehrere Server antworten mit IP-Adressen
DHCP Request                  | Host sucht sich eine IP-Adresse aus und sendet Bestätigung an                                                 Server
DHCP Acknnowledgment | Server sendet Bestätigung mit allen Daten (IP, DNS usw.) zurück


`ip dhcp excluded-address {kleine Adresse} {höchste Adresse}`
-> Die vom Router ausschließen

`ip dhcp pool {Pool Name}`

`network {IP-Adresse} {Subnetmaske}`
`default-router {IP-Adresse Routr}`
`dns-server {IP-Adresse DNS Server}`
`domain-name {Domänenname}`
`end`

**Konfiguration überprüfen**

`show running-config | section dhcp`

**IP-Adresse für bestimmte MAC-Adresse reservieren**

`show ip dhcp binding`

`ip dhcp excluded-address 192.168.1.10`  

`ip dhcp pool CLIENT_10`  
`host 192.168.1.10 255.255.255.0`  
`client-identifier 0100.3412.1b0c.19`

