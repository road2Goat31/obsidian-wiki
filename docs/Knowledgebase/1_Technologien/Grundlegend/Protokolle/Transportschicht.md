# Well-Known-Ports
![](Anhang/Pasted%20image%2020250228072042.png)

# TCP
## **Wichtige Merkmale:** 
- **Verbindungsorientiert:** Bevor Daten übertragen werden, muss eine Verbindung zwischen den beiden Kommunikationspunkten (Client und Server) aufgebaut werden. 
- **Zuverlässigkeit:** Garantiert, dass die Daten korrekt und in der richtigen Reihenfolge ankommen. Falls Pakete verloren gehen, werden sie erneut gesendet. 
- **Fehlerkorrektur:** Verwendet Prüfmechanismen (z.B. Prüfziffern, ACKs), um sicherzustellen, dass die Daten fehlerfrei übertragen werden. 
- **Datenflusssteuerung:** Steuert die Geschwindigkeit der Datenübertragung, um Überlastung zu vermeiden. 
- **Beispielprotokolle:** HTTP, HTTPS, FTP, SMTP, Telnet 

## **Vor- und Nachteile:** 
- **Vorteile:** 
	- Zuverlässige Datenübertragung. 
	- Verbindungsaufbau und Fehlerkorrektur sorgen für stabile Kommunikation. 
- **Nachteile:** 
	- Höherer Overhead durch Verbindungsmanagement und Fehlerbehebung.
	- Längere Latenz aufgrund der zusätzlichen Kontrolle. 
	
---

# UDP

## **Wichtige Merkmale:** 
- **Verbindungslos:** UDP benötigt keine Verbindung zwischen den Kommunikationspunkten. Daten werden direkt gesendet, ohne vorherige Vereinbarung. 
- **Unzuverlässigkeit:** Es gibt keine Garantie, dass die Daten korrekt oder in der richtigen Reihenfolge ankommen. Pakete können verloren gehen oder in falscher Reihenfolge ankommen  
- **Kein Fehlerhandling:** Es gibt keine Mechanismen für die Fehlerkorrektur oder die Bestätigung des Empfangs von Daten  
- **Schnelligkeit:** Wegen des geringen Overheads ist UDP schneller als TCP, eignet sich jedoch nicht für alle Anwendungen  
- **Beispielprotokolle:** DNS, DHCP, SNMP, Streaming-Dienste, VoIP
### **Vor- und Nachteile:** 
- **Vorteile:** 
	- Schnelle Datenübertragung ohne Verbindungsaufbau
	- Geringer Overhead, ideal für Echtzeitanwendungen wie VoIP und Streaming
- **Nachteile:** 
	- Keine Garantie für die Zustellung oder Reihenfolge der Pakete
	- Anwendungsprotokolle müssen selbst für Fehlerkorrektur sorgen, wenn erforderlich