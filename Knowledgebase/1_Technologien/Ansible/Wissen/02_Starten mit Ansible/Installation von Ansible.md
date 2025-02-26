# Install

- [Docs: install via pip](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- [Docs: install via packagemanager](https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html)

## RHEL

- [Docs: Installing Ansible from EPEL](https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html#installing-ansible-from-epel)
- [How to Install Ansible on Rocky Linux 8 or Almalinux](https://linux.how2shout.com/how-to-install-ansible-on-rocky-linux-8-or-almalinux)
- Ansible kann über die EPEL-Repos bezogen werden

```bash
dnf install epel-release
```

- GPG-Key für Fedora epel akzeptieren

```bash
dnf install ansible
```

- Installation prüfen

```bash
ansible --version
```

## Debian

- [Docs: Installing Ansible on Debian](https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html#installing-ansible-on-debian)

```
apt install ansible
```