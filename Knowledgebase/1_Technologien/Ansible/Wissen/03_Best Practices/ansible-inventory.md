- [Ansible-Docs: How to build your inventory](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#inventory-directory)
	- [Ansible-Docs: How to build your inventory - Organizing inventory in a directory](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#organizing-inventory-in-a-directory)
# Inventory-Ordner anlegen

Darin befindet sich:
- hosts.yml
- host_vars
- group_vars

```
├── inventory
   ├── group_vars
   ├── hosts.yml
   └── host_vars

```
## Bennenung der Dateien in der `host_vars`

--> die einzelnen Dateien der Hosts in den `host_vars` müssen genauso heißen, wie die Hosts in der hosts.yml-Datei benannt sind
```
├── inventory
   ├── group_vars
   │   └── group1.yml
   ├── hosts.yml
   └── host_vars
	   └── host1.yml
```

## Definition des Inventory-Pfades

--> in der ansible.cfg muss das vermerkt sein

```
inventory = ./inventory
```


# die hosts.yml

```
all:
  children:
    portswitch:
      hosts:
        KonsolenSwitch:
          ansible_host: 172.20.1.1
          ansible_user: adminmks
          ansible_password: Install2024
          ansible_connection: ssh
    ports:
      hosts:
        port1:
          ansible_host: 172.20.16.244
          hostname: shd-x-1
          ansible_network_os: ios
        port2:
          ansible_host: 172.20.16.245
          hostname: shd-x-2
          ansible_network_os: ios
```

- Untergruppen mit `children:` anlegen
- Host spezifische Verbindungsvariablen definieren (alles andere in der host_vars) --> Hostname müsste in die host_vars beim Bsp.
- Variablen für die gnaze Gruppe können in der hosts.yml definiert werden (oder in der group_vars-Datei):
```
    ports:
      hosts:
      vars:
        ansible_user: admin  # Benutzername für die Switches
        ansible_password: mkspasswort  # Passwort für die Switches
        ansible_connection: network_cli  # Verbindung für die Switches
        
        port1:
          ansible_host: 172.20.16.244
          hostname: shd-x-1
          ansible_network_os: ios
```
