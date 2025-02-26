Das Spanning Tree Protocol ist dafür zuständig loops in LANs zu verhindern bzw. diese zu erkennen und zu unterbinden.
Loops können durch redundante Netzwerkverbindungen entstehen.

Loops können durch folgende Frames entstehen durch:
- Unknown Unicasts
- Broadcasts
- Multicasts

Übersicht: `show spanning-tree interface {interface-id} detail`

BPDUs -> Bridge Protcol Data Units
= zum Austausch von Informationen über die Netzwerktopologie

![](Anhang/Pasted%20image%2020250220074224.png)
![](Anhang/Pasted%20image%2020250220074016.png)

RSTP auf einem Cisco Switch:
![](Anhang/Pasted%20image%2020250220074619.png)
![](Anhang/Pasted%20image%2020250220074634.png)

- Je niedriger die **Bridge ID**, desto wahrscheinlicher ist der Root-Bridge-Status
- **Root-Ports** sind die, die die wenigsten Kosten zur Root-Bridge verursachen
- **Edge-Ports** sind die, die mit einem End-Gerät verbunden sind
- Die Ports an der Root-Bridge sind alle Designated
- **Alternate-Ports** sind für Traffic ausgeschalten -> wenn die Hauptroute ausfällt, werden sie angeschaltet

STP-Probleme lösen:

- **BPDU-Guard -> loops von unautorisierten Switchen vermeiden
	- bei Access-Ports
	- Ports connected zu Server oder Virtualisierung-Hosts
	- ist meistens aktiviert, wenn PortsFast aktiviert ist
	- Global: `spanning-tree portfast bpduguard enable`
	- Interface: `spanning-tree bpduguard enable`
	
- **Root Guard
	- verhindert ungewollte Root-Bridge Änderung
	- der Root überwacht die BPDUs und wenn diese eine bessere BID enthalten, wird der Port abgeschaltet
	- wenn der andere Switch aufhört sich als Root zu bewerben wird der Port wieder angeschaltet
	- Switch zum Root machen: `spanning-tree vlan 1 root primary`
	- Root-Guard aktivieren: `**spanning-tree guard root**`
	- überprüfen: `show spanning-tree root`

Unnötiger BPDU-Traffic:
- **BPDU Filter** an Access-Ports -> BPDUs werden nicht an end devices weitergeleitet
- an Access-Ports verwendet
- Global: `spanning-tree portfast bpdufilter enable`
- Interface: `spanning-tree bpdufilter enable`

Loops durch beschädigte Verbindungen 
- **loop Guard**
- verhindert, dass alternate Ports oder root Ports  bei Punkt-zu-Punkt-Verbindungen designated Ports werden wegen Link failures
- Ein unidirektionaler Verbindungsfehler kann dazu führen, dass ein Switch keine Bridge Protocol Data Units (BPDUs) mehr von seinem Nachbarn auf dieser Verbindung empfängt. Wenn der Switch weiterhin Datenverkehr aus dem betroffenen Port weiterleitet, ohne BPDUs zu empfangen, kann er unbeabsichtigt eine Netzwerkschleife erstellen
- sollte auf allen Switchen-zu-Switch-Verbindungen aktiviert sein
- Global: `spanning-tree loopguard default`
- Interface: `spanning-tree guard loop`


STP auf Accessports ausschalten
- **PortFast** -> Pakete werden direkt forwarded
	- Global: `spanning-tree portfast default` -> PortFast an allen Access-Ports
	- Interface: `spanning-tree portfast`