Alle ungenutzten Ports deaktivieren

`configure Terminal`
`interface range fa0/8 - 24`
`shutdown`


**Port-Security:**
- Begrenzung der MAC-Adressen pro Port
- Schutz vor MAC-Flooding
- Automatische Abschaltung bei Verstößen

`configure terminal`
`interface fa0/5`
`switchport port-security`
`switchport mode access`
`switchport port security`
`end`

`show port-security interface fa0/5`


**Maximale MAC-Adress-Anzahl**

`configure terminal`
`interface fa0/5`
`switchport port-security maximum`

**Einzelne MAC-Adressen**

`configure terminal`
`interface fa0/5`
`switchport port-security mac-address {MAC-Adresse}`

**Dynamisch gelernt - sticky**

--> MAC-Adressen werden automatisch zur startup-config hinzugefügt und nach einem          reboot nicht vergessen


`configure terminal`
`interface fa0/5`
`switchport port-security mac-address sticky`


**Port Security Aging**

DIe MAC-Adressen werden nach einer festgelegten Zeit gelöscht --> ungenutzte Adressen belegen nicht dauerhaft den Speicher --> nützlich bei hoher Anzahl an dynamischen Geräten

Es gibt zwei Arten von Aging:

1. **Absolute Aging**: Hier wird eine MAC-Adresse nach einem festgelegten Zeitraum (z. B. 5 Minuten) unabhängig von ihrer Aktivität entfernt.

2. **Inactivity Aging**: Hier wird die MAC-Adresse nur entfernt, wenn sie für einen bestimmten Zeitraum inaktiv ist.

`configue terminal`
`interface fa0/5`
`switchport port-security aging {static / time (Zeit in min) / type (absolute/inactivity)}`
`end`

**Port Security Violation Mode**

`configure terminal` 
`interface fa0/5`
`switchport port-security violation {protect / restrict / shutdown}`


| Violation Mode | Verwift Traffic? | Sendet Syslog? | Erhöht Counter? | Schaltet Port aus? |
|---------------|-----------------|---------------|----------------|----------------|
| Protect       | Ja              | Nein          | Nein           | Nein           |
| Restrict      | Ja              | Ja            | Ja             | Nein           |
| Shutdown      | Ja              | Ja            | Ja             | Ja             |



**VLAN angriffe verhindern**

1. bei allen nicht trunk ports switch mode access
2. nicht genutzte Ports deaktivieren und ungenutztem VLAN zuordnen
3. nur die nötigen als Trunkports nutzen
4. Auto negotiations ausschalten bei trunkports `switchport nonegotiate`
5. natives VLAN nicht bei 1 lassen `switchport trunk native vlan 999`

**DHCP Attacken verhindern**

`configure terminal`
`ip dhcp snooping (rate 10)  --> maximal 10 DHCP-Nachrichten pro Sekunde`
`exit`


`ip dhcp snooping vlan 10,20,30-49`

`show ip dhcp snooping`


**ARP Angriffe verhindern**

--> es wird DHCP snooping benötigt

`ip dhcp snooping`
`ip dhcp snooping vlan 10`
`ip arp inspection vlan 10`
`interface fa0/5`
`ip dhcp snooping trust`  --> Ausnahme für Interface
`ip arp inspection trust`


**Spanning-tree Angriffe verhindern**

-> Portfast nicht zwischen Switches erlauben, ansonsten können loops entstehen

`configure terminal`
`switchport mode access`
`spanning-tree portfast`
`exit`

`spanning-tree portfast default`     --> Portfast Global aktivieren
`exit`

--> BPDU Guard

`configure terminal`
`spanning-tree bpduguard enable`
`exit`

`configure terminal`
`spanning-tree portfast bpduguard default`
`end`