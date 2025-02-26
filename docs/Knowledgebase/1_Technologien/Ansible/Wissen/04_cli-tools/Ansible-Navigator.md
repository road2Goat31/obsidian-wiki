# Quellen

- [RH: Ansible Navigator Creator Guide](https://access.redhat.com/documentation/de-de/red_hat_ansible_automation_platform/2.0-ea/html-single/ansible_navigator_creator_guide/index)

# Zusammenfassung

Mit der Ansible Automation Platform (AAP) wurden Execution Environments (EEs) eingeführt, um benötigte Abhängigkeiten innerhalb eines Containers zu kapseln.  [ansible playbooks](../05_Komponenten/ansible%20playbooks.md) stellt keine Möglichkeit bereit, Playbooks innerhalb von EEs auszuführen. An dieser Stelle setzt der [Ansible-Navigator](Ansible-Navigator.md) an und ermöglicht unter anderem die Ausführung von Playbooks innerhlab von EEs.

# Config

- [Docs: ansible-navigator: general parameter](https://ansible.readthedocs.io/projects/navigator/settings/#general-parameters)
- `./ansible-navigator.yml`
	- projektweite Einstellungen
- `~/ansible-navigator.yml`
	- user-weite Einstellungen
- `ANSIBLE_NAVIGATOR_CONFIG`
	- Pfad zur Config via Environmentvariable

```
---
ansible-navigator:
  ansible:
    inventory:
      entries:
        - hosts.yml
  execution-environment:
    container-engine: podman
    enabled: true
    image: registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8:latest
  playbook-artifact:
    enable: false
```

# Commands

## run

- `run` entspricht `ansible-playbook` mithilfe einer EE

```
ansible-navigator run playbooks/select-aggregate.yml -m stdout --eei ontap-ansible-ee --tags aggregates --ask-vault-pass
```

- `-m (--mode) <mode>`
	- `stdout`
		- interaktiver Modus `stdin` und `stdout` werden direkt auf die CLI übertragen
		- ermöglicht `--ask-vault-pass`
- `--eei (--execution-environment-image) <ee_image>`
	- Ausführen des Runs mit bestimmter EE