
Mehrere Ports zu einem logischen Port zusammenfassen

LACP oder PAgPals Protokoll

**Konfigurieren**

`configure Terminal`
`interface range fa0/1-3    -> oder andere Range`
`channel-group 1 mode active`
`exit`
`interface group-channel 1`
`switchport mode {access/trunk}`
`end`


**Überprüfen**

`show interfaces port-channel 1`

`show etherchannel summary`
