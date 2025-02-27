# Erweiterte Informationen zu IPv4

Diese Zusammenfassung geht über die absoluten Grundlagen hinaus und beleuchtet fortgeschrittene Aspekte und Herausforderungen von IPv4.

## CIDR und Subnetting
- **Flexible Adresszuweisung:**  
  Dank Classless Inter-Domain Routing (CIDR) werden starre Adressklassen abgelöst. Adressblöcke werden beispielsweise als `192.168.1.0/24` definiert, was eine präzisere und effizientere Nutzung des Adressraums ermöglicht.

- **Subnetting:**  
  Durch die Aufteilung eines Netzwerks in kleinere Subnetze (z. B. mit Masken wie `/26` oder `/28`) können Administratoren den verfügbaren Adressraum optimal verteilen. Dies hilft, sowohl die Routing-Tabelle zu verkleinern als auch Broadcast-Domänen zu begrenzen.

## NAT und seine Auswirkungen
- **Address Translation:**  
  Network Address Translation (NAT) kompensiert den begrenzten öffentlichen Adressraum, indem private IP-Adressen in eine oder wenige öffentliche Adressen übersetzt werden.  
- **Herausforderungen:**  
  NAT kann die direkte End-to-End-Konnektivität behindern und Probleme bei Anwendungen wie Peer-to-Peer-Verbindungen, VoIP oder VPNs verursachen. Verschiedene NAT-Methoden (statisch, dynamisch, PAT) bieten unterschiedliche Kompromisse zwischen Flexibilität und Komplexität.

## Fragmentierung und Netzwerkperformance
- **Fragmentierung:**  
  IPv4 erlaubt die Fragmentierung von Paketen, wenn diese die Maximum Transmission Unit (MTU) überschreiten.  
- **Auswirkungen:**  
  Fragmentierte Pakete können die Netzwerkleistung beeinträchtigen und die Fehlersuche erschweren. Moderne Netzwerke setzen oft auf Path MTU Discovery, um Fragmentierung zu vermeiden.

## Sicherheitsaspekte
- **Fehlende integrierte Sicherheit:**  
  Im Gegensatz zu IPv6 enthält IPv4 keine eingebauten Sicherheitsmechanismen wie IPSec. Dies erfordert zusätzliche Maßnahmen, um Datenverkehr abzusichern.
- **Komplexität durch NAT:**  
  Obwohl NAT als Adressknappheit-Lösung dient, führt es auch zu komplexeren Sicherheitsarchitekturen. Falsch konfigurierte NAT-Regeln oder Firewalls können Sicherheitslücken öffnen.

## Herausforderungen und der Übergang zu IPv6
- **Adressknappheit:**  
  Der 32-Bit-Adressraum von IPv4 (ca. 4,3 Milliarden Adressen) stößt in der modernen, global vernetzten Welt an seine Grenzen.  
- **Übergangslösungen:**  
  Techniken wie CIDR, Subnetting und NAT sind kurzfristige Maßnahmen. Langfristig ist jedoch der Übergang zu IPv6 notwendig, da dieser einen nahezu unerschöpflichen Adressraum und verbesserte Sicherheits- sowie Routingfunktionen bietet.


# Aufbau des IPv4-Headers

Ein IPv4-Header hat mindestens 20 Byte (ohne Optionen) und besteht aus mehreren Feldern, die in einer festen Reihenfolge angeordnet sind:

![](Anhang/Pasted%20image%2020250227153917.png)

### 1. Version und IHL (Internet Header Length)
- **Version (4 Bit):**  
  Gibt die Protokollversion an – bei IPv4 immer `4`.
- **IHL (4 Bit):**  
  Bestimmt die Länge des Headers in 32-Bit-Worten. Der Mindestwert ist 5 (5 × 4 Byte = 20 Byte). Ein höherer Wert zeigt das Vorhandensein von **Optionen** an.

### 2. Differentiated Services Field (DS Field)
- **DSCP (6 Bit):**  
  Dient zur Klassifizierung des Datenverkehrs für Quality of Service (QoS)-Zwecke.
- **ECN (2 Bit):**  
  Ermöglicht eine frühe Stauanzeige, indem Traffic-Management-Maßnahmen signalisiert werden (Explicit Congestion Notification).

### 3. Total Length (16 Bit)
- Gibt die Gesamtlänge des Pakets in Byte an (Header + Daten).  
  Werte reichen von 20 (nur Header) bis 65.535 Byte.

### 4. Identification (16 Bit)
- Ein eindeutiger Bezeichner, der zur Fragmentierung und späteren Wiederzusammenführung von Paketen verwendet wird.

### 5. Flags (3 Bit) und Fragment Offset (13 Bit)
- **Flags:**  
  - Bit 0: Reserviert (muss 0 sein)  
  - Bit 1: DF (Don't Fragment) – verhindert die Fragmentierung, wenn gesetzt.  
  - Bit 2: MF (More Fragments) – zeigt an, dass weitere Fragmente folgen.
- **Fragment Offset:**  
  Gibt an, an welcher Position die Daten des aktuellen Fragments im ursprünglichen Paket stehen. Die Einheit ist 8-Byte-Blöcke.

### 6. Time to Live (TTL) (8 Bit)
- Bestimmt, wie viele Router (Hop) ein Paket maximal passieren darf, bevor es verworfen wird. Dieser Wert wird bei jedem Durchgang um 1 reduziert, um Endlosschleifen zu verhindern.

### 7. Protocol (8 Bit)
- Gibt an, welches Protokoll im Payload (Datenbereich) verwendet wird (z. B. TCP = 6, UDP = 17, ICMP = 1).

### 8. Header Checksum (16 Bit)
- Eine Prüfsumme, die ausschließlich den Header abdeckt. Sie wird vom Sender berechnet und vom Empfänger überprüft, um Fehler im Header zu erkennen.  
  **Berechnung:**  
  - Alle 16-Bit-Wörter des Headers werden addiert.
  - Das Ergebnis wird invertiert (Bitweise NOT) und im Checksum-Feld abgelegt.
  - Bei der Überprüfung führt der Empfänger die gleiche Rechnung durch; ein Ergebnis von `0xFFFF` (oder 0 nach Invertierung) zeigt einen fehlerfreien Header an.

### 9. Source Address (32 Bit)
- Enthält die Quell-IP-Adresse des Pakets.

### 10. Destination Address 

