Wenn erhöhte Berechtigungen benötigt werden, wird das Element  ``become=true`` benutzt.

--> Kann man auf Playbook-Ebene oder Task-Ebene anwenden
--> in der .cfg-Datei kann es auch Global mit ```become_user=[UserName]``` gesetzt werden

Dem User Sudo-Rechte geben:

Sudoers-Datei unter ansible/files ablegen

ODER:

```
---
- name: Service User hinzufügen und Gruppe setzen
  hosts: all
  become: true
  tasks:
    - name: Füge den Service User "serviceuser" hinzu
      ansible.builtin.user:
        name: serviceuser
        shell: /sbin/nologin
        system: yes
        create_home: no
        state: present
        groups: servicegroup   # Fügt den Benutzer der Gruppe "servicegroup" hinzu

```
