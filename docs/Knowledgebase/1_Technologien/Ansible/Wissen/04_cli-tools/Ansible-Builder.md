# Quellen

- [GH: shadowman-lab/Ansible-PAH (Alex Dworjan)](https://github.com/shadowman-lab/Ansible-PAH)
	- [GH: shadowman-lab/Ansible-PAH/blob/main/roles/build_creationee/defaults/main.yml](https://github.com/shadowman-lab/Ansible-PAH/blob/main/roles/build_creationee/defaults/main.yml)
- [YT: Alex Dworjan on EEs](https://www.youtube.com/watch?v=6HG8VXxL7a4)
	- <https://www.youtube.com/watch?v=6HG8VXxL7a4>
- Red Hat
	- [RH: The anatomy of automation execution environments](https://www.ansible.com/blog/the-anatomy-of-automation-execution-environments)
	- [RH-Dev: How to create execution environments using ansible-builder](https://developers.redhat.com/articles/2023/05/08/how-create-execution-environments-using-ansible-builder)

# Install

## upstream

- als `pip` install wird immer das upstream-Paket bezogen

```
pip3 install ansible-builder
```

## supported

- installiert aus den offiziellen AAP-Repos
	- `ansible-core`
	- `ansible-builder`
	- `ansible-navigator`

```
AAP_VERSION=2.4
RHEL_VERSION=8
sudo dnf install --enablerepo "ansible-automation-platform-$AAP_VERSION-for-rhel-$RHEL_VERSION-x86_64-rpms" ansible-core ansible-builder ansible-navigator -y
```

# Usage

```
ansible-builder < build | create >
```

- `build`
	- erstellt Contextfiles wie z.B. `Containerfile`
	- anhand der execution environment specs
	- **baut im Anschluss das Image für die EE**
- `create`
	- erstellt Contextfiles wie z.B. `Containerfile`
	- anhand der execution environment specs

## Image bauen

```
ansible-builder build -v3 -t ontap-ansible-ee:0.2
```

## Image in Registry Pushen

- Login für Container-Registry

```
podman login <container_registry>
```

- Tag vergeben, wenn nicht durch `ansible-builder` schon geschehen

```
IMAGE_HASH=c3b4be733509
VERSION_TAG=0.3
podman push $IMAGE_HASH gitlab330.shd-online.de:5050/automation-engineering/ansible/execution-environments/ontap-ansible-ee:$VERSION_TAG
# set latest
podman push $IMAGE_HASH gitlab330.shd-online.de:5050/automation-engineering/ansible/execution-environments/ontap-ansible-ee:latest
```

## EE-Image als tar für Transfer

```
podman save --format=oci-archive -o ontap-ansible-ee-0.3.tar ontap-ansible-ee:0.3
```