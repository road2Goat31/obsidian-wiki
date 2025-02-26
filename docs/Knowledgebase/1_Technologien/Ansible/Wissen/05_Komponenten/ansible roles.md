# neue role erstellen

- neue Ordnerstruktur für Ansible-Role mit ansible-galaxy erstellen

```
ansible-galaxy init test_role
```

- filestructure of an initialized role-repo

```
test_role/
├── README.md
├── defaults
│   └── main.yml
├── files
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── tasks
│   └── main.yml
├── templates
├── tests
│   ├── inventory
│   └── test.yml
└── vars
    └── main.yml
```

# Linux Supported Roles

- https://linux-system-roles.github.io/