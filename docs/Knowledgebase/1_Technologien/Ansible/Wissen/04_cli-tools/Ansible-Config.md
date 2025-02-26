# Files

```
/etc/ansible/
├── ansible.cfg     -> default ansible Config
├── hosts           -> default inventory-file for ansible
└── roles           -> global roles for the system
```

- globale Configs (bei Install über Package-Manager)
	- `/etc/ansible/ansible.cfg`
- projektspezifische Config
	- `./ansible.cfg`
	- **Ordner/File darf nicht world-writeable sein**
		- max `775`

# Commands

## Informationen ausgeben

- Version ausgeben

```
ansible-config --version
```

- alle Configs ausgeben

```
ansible-config list
```

- gesetzte Configs ausgeben

```
ansible-config dump
```

- geändert Configs ausgeben

```
ansible-config dump --changed-only
```

## Config erstellen

- bootstrap `ansible.cfg`

```
ansible-config init --disabled > ./ansible.cfg
```
