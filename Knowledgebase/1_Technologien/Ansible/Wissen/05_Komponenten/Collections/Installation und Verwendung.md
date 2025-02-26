# Installation einer Collection

```
ansible-galaxy collection install <namespace>.<collection_name>
```

# Verwendung einer Collection

```
- name: Verwende Modul aus einer Collection
  my_namespace.my_collection.my_module:
    param: value
```