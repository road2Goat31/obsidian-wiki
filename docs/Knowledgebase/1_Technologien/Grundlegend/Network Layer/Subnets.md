
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
   - Netz 1: 4096 / 256 = 16   
   - Bsp: 172.16.0.0 - 172.16.15.255 -> -1, da 0 basiert  
   - Netz 2: 516 / 256 = 2  
   - Bsp: 12.16.16.0 - 172.16.17.255  
