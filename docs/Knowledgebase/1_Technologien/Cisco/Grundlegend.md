
**Frame-Forwarding-Methoden**
- Store-and-Forward-Switchung
	- speichert den gesamten Frame und überprüft auf Fehler -> CRC(Cycling Redundancy Check) = Prüfsumme
	- wenn kein Fehler vorhanden, dann wird es weitergeleitet
	- wenn Fehler, dann wird Paket verworfen
	- wird für QoS benötigt
- Cut-Through-Switching
	- leitet schon weiter, obwohl noch nicht der gesamte Frame da ist
	- Fast-Forward-Switching -> leitet sofort weiter
	- Fragment-Free-Switching -> speichert die ersten 64 bytes und überprüft auf Fehler

**Speicherung**
- Port-Based-Speicher -> Frames mit Port verlinkt gespeichert
- Shared Memory -> speichert alle Frame sin einen Speicher, ports sind dynamisch verlinkt

**Automatisch Ausgehandelt**
- Speed (10/100/1000 Mbps)
- Half-/Fullduplex

Gigabit Ethernet ports funktionieren nur in Fullduplex


![](Anhang/Pasted%20image%2020250219125029.png)
````
enable
disable
configure terminal (conf)
exit -> aus conf raus
end

? -> help
````

![Hotkeys](Anhang/Pasted%20image%2020250219130130.png)

Geräteinformationen
![](Anhang/Pasted%20image%2020250219130552.png)