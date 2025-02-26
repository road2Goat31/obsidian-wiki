Wenn erhöhte Berechtigungen benötigt werden, wird das Element  ``become=true`` benutzt.

--> Kann man auf Playbook-Ebene oder Task-Ebene anwenden
--> in der .cfg-Datei kann es auch Global mit ```become_user=[UserName]``` gesetzt werden

Dem User Sudo-Rechte geben:
Die Sudoers-Datei mit einer Task bearbeiten

![](../04_cli-tools/Anhang/Pasted%20image%2020241021120319.png)

Sudoers-Datei unter ansible/files ablegen

![](../04_cli-tools/Anhang/Pasted%20image%2020241021120421.png)

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
