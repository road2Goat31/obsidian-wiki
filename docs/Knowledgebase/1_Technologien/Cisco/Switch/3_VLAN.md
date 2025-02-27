# VLAN erstellen

`configure Terminal`
`interface vlan 1`
`ip address 192.158.1.1 255.255.255.0`
`no shutdown`
`name {Name vom VLAN}`
`end`


# Interface ein VLAN zuornden

`configure Terminal`
`interface fa0/2`
`switchport mode {access/trunk}`
`switchport access vlan 10`
`end`

`show vlan summary`

`show vlan brief`


