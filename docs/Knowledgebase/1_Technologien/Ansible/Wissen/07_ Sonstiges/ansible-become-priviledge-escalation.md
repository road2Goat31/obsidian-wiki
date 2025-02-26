# Infos

- [Ansible: Credentials](https://docs.ansible.com/automation-controller/latest/html/userguide/credentials.html)
- [Red Hat: Hardening SSH connections to managed hosts with Red Hat Ansible Automation Platform](https://www.redhat.com/en/blog/hardening-ssh-connections-ansible-automation-platform)

## srv-ansible

### create user

- service-user on remotes (also used for `become`)

```
useradd srv-ansible
```

### grant sudo

```
echo '%srv-ansible ALL=(ALL:ALL) ALL' > /etc/sudoers.d/srv-ansible
```

# pam_ssh_agent_auth

## Target

- `sudo -i` via ssh-agent for ansibles (used by directive `become: true`)
	- user `root` can't be used by ansible for authentication against the system
	- `ask_pass` can't be used in an interactive manner
- there is the pam-module `pam_ssh_agent_auth` which allows auth via ssh-agent
- should provide [secure priviledge escalation for ansible](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_privilege_escalation.html)

## install

- install module

```
dnf install -y pam_ssh_agent_auth
```

## sudo via ssh-agent

- enable `sudo` via `ssh-agent` (ForwardAgent)
- allow auth with key from specific user
	- `~svc-ansible/` user-pinning who is able to use his set keys for `sudo`
- `/etc/pam.d/sudo`
	- **problem:** active ssh-agent needed

```
auth       sufficient   pam_ssh_agent_auth.so file=/root/.ssh/authorized_keys
```

## allow root-login

- `/etc/pam.d/sshd`
	- **problem:** this is only for direct root-login
		- same as planting the key in `/root/.ssh/authorized_keys`

```
auth       sufficient   pam_ssh_agent_auth.so file=/root/.ssh/super_authorized_key
```


Wenn erhöhte Berechtigungen benötigt werden, wird das Element  ``become=true`` benutzt.

- Kann man auf Playbook-Ebene oder Task-Ebene anwenden
- in der .cfg-Datei kann es auch Global mit ```become_user=[UserName]``` gesetzt werden

Dem User Sudo-Rechte geben:
Die Sudoers-Datei mit einer Task bearbeiten

```

```

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
