**Interface ein VLAN zuornden**

`configure Terminal`
`vlan10`
`name {Name vom VLAN}`
`end`

`configure Terminal`
`interface fa0/2`
`switchport mode {access/trunk}`
`switchport access vlan 10`
`end`

`show vlan summary`

`show vlan brief`


