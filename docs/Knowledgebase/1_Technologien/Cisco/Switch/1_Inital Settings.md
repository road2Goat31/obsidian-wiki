Mode Button: zwischen den verschiedenen Status-Modi wechseln

**Status LEDs:**
SYST:
- Grün: alles funktioniert
- Orange: Som, aber irgend etwas funktioniert nicht richtig
- Aus: Kein Strom

RPS: Redundant Power System
- Aus: RPS ist aus
- Grün: RPS funktioniert und kann redundant Strom liefern
- blinkt grün: RPS ist an, aber kann keinen redundanten Strom liefern, da anderes Gerät damit beliefert wird
- orange: Standby oder Fehler 
- blinkt Orange: interne Stromversorgung hat versagt und RPS liefert Strom

STAT:
- aus: kein Link
- grün: Link vorhanden
- blinkt grün: Netzwerkaktivität vorhanden
- orange: Port ist blockiert zum Überprüfen, dass kein Loop vorhanden ist
- blinkt orange: blockiert, um mögliche Loop zu unterbinden

DUPLEX:
- aus: Halb-Duplex
- grün: duplex mode aktiviert

SPEED:
- aus: 10 Mbps
- grün: 100 Mbps
- blinkt grün: 1000 Mbps

PoE:
- aus: PoE nicht aktiviert
- blinkt orange: PoE nicht aktiviert, aber ein Gerät benötigt PoE
- grün: PoE ist aktiviert
- Port aus: PoE aus
- Port grün: PoE an
- Port grün und orange: PoE wurde verhindert, da sonst die Gesamtkapazität des Switches überladen ist
- Port blinkt orange: PoE ist aus aufgrund eine Fehlers
- Port orange: PoE wurde für Port ausgeschaltet

**Nach Systemcrash:**
1. PC per Kabel anschließen
2. Stromkabel ziehen
3. Strom wieder anstecken und innerhalb von 15s den Mode-Button gedrückt halten
4. gedrückt halten bis es erst grün und dann orange geleuchtet hat
5. Terminal bedienen -> dir flash: OS boot-Datei auswählen
6. Boot=flash:{Boot-Datei}
   set
   boot

**Boot:**
boot system flash:/{flash device}/{OS_file_name}

![](Anhang/Pasted%20image%2020250219131534.png)

**Management-Zugriff**
Alle Ports sind standardmäßig dem VLAN 1 zugeordnet. Es wird empfohlen ein anderes VLAN für das Management des Switches zu nutzen, z.B. VLAN 99

``configure terminal
``interface vlan 99
``ip address {IP-adresse} {Subnetmaske}
``(ipv6 address {IPv6-Adresse})
``no shutdown
``end
``copy running-config startup-config

**Default Gateway:**

``configure Terminal
``ip default-gateway {ip-adresse}
``end
``copy running-config startup-config

**Konfiguration verifizieren:**

``show ip interface brief

**Sonstige Commands:**

`no ip address`

`default interface fa0/1`