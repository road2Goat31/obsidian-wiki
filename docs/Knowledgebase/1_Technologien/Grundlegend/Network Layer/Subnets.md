
# /24-Subnet

![](Anhang/Pasted%20image%2020250310114038.png)

# /16-Subnet
![](Anhang/Pasted%20image%2020250310114155.png)
![](Anhang/Pasted%20image%2020250310114212.png)

## Subnet-Bits
![](Anhang/Pasted%20image%2020250310114324.png)
# /8-Subnet

![](Anhang/Pasted%20image%2020250310115033.png)

## Subnet-Bits
![](Anhang/Pasted%20image%2020250310114538.png)

# effizient Subnetze planen

1) Anforderungen sammeln:  
   - Gegebene IP-Adresse und Subnetzmaske  
   - Anzahl Subnetze  
   - Anzahl Hosts pro Subnetz  

2) Subnetzmasken für die einzelnen Netze bestimmen:  
   - Subnetze nur so groß wie nötig wählen  
   - Netz 1: 4000 benötigte Hosts -> /20 = 4096 - 2 Adressen  
   - Netz 2: 500 benötigte Hosts -> /23 = 516 - 2 Adressen  
   
3) Netzwerkadressen und Broadcastadressen berechnen  
   - Der Größe nach die Netze berechnen (von groß nach klein)
   - Netz 1: 4096 / 256 = 16   
   - Bsp: 172.16.0.0 - 172.16.15.255 -> -1, da 0 basiert  
   - Netz 2: 516 / 256 = 2  
   - Bsp: 12.16.16.0 - 172.16.17.255

Beispiel:  
Netzwerk **192.168.0.0/16**  

- **Fakultät für Informatik:** 4.000 Hosts  
- **Fakultät für Ingenieurwissenschaften:** 2.000 Hosts  
- **Fakultät für Wirtschaft:** 1.000 Hosts  
- **Bibliothek:** 500 Hosts  
- **Studenten-WLAN:** 10.000 Hosts  
- **Mitarbeiter-Netzwerk:** 2.500 Hosts  
- **Server-Netzwerk:** 300 Hosts  
- **Administrations-Netzwerk:** 50 Hosts  

Bestimmen der Subnetzmasken:  
1. /20 
2. /21
3. /22
4. /23
5. /18
6. /20
7. /23
8. /26

Netzwerkadressen und Broadcastadressen:  

Studenten: 192.168.0.0 - 192.168.63.255  
Fakultät Informatik: 192.168.64.0 - 192.168.79.255  
Mitarbeiter Netzwerk: 192.168.80.0 - 192.168.95.255  
Fakultät Ingineurwissenschaften: 192.168.96.0 - 192.168.101.255  
Fakultät Wirtschaft: 192.168.102.0 - 192.168.105.255  
Bibliothek: 192.168.106.0 - 192.168.107.255  
Server-Netzwerk: 192.168.108.0 - 192.168.109.255  
Admin-Netzwerk: 192.168.110.0 - 192.168.110.63  
