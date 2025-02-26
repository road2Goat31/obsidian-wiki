# Docker und Docker-Compose installieren

```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Quelle: ([Ubuntu | Docker Docs](https://docs.docker.com/engine/install/ubuntu/))

# Semaphore-Container erstellen

Docker-Datei erstellen:

```
nano docker-compose.yml
```

folgendes Einfügen und ggf. editieren:



```
services:
  # uncomment this section and comment out the mysql section to use postgres instead of mysql
  #postgres:
    #restart: unless-stopped
    #image: postgres:14
    #hostname: postgres
    #volumes: 
    #  - semaphore-postgres:/var/lib/postgresql/data
    #environment:
    #  POSTGRES_USER: semaphore
    #  POSTGRES_PASSWORD: semaphore
    #  POSTGRES_DB: semaphore
  # if you wish to use postgres, comment the mysql service section below 
  mysql:
    restart: unless-stopped
    image: mysql:8.0
    hostname: mysql
    volumes:
      - semaphore-mysql:/var/lib/mysql
    environment:
      MYSQL_RANDOM_ROOT_PASSWORD: 'yes'
      MYSQL_DATABASE: semaphore
      MYSQL_USER: semaphore
      MYSQL_PASSWORD: semaphore
  semaphore:
    restart: unless-stopped
    ports:
      - 3000:3000
    image: semaphoreui/semaphore:latest
    environment:
      SEMAPHORE_DB_USER: semaphore
      SEMAPHORE_DB_PASS: semaphore
      SEMAPHORE_DB_HOST: mysql # for postgres, change to: postgres
      SEMAPHORE_DB_PORT: 3306 # change to 5432 for postgres
      SEMAPHORE_DB_DIALECT: mysql # for postgres, change to: postgres
      SEMAPHORE_DB: semaphore
      SEMAPHORE_PLAYBOOK_PATH: /tmp/semaphore/
      SEMAPHORE_ADMIN_PASSWORD: changeme
      SEMAPHORE_ADMIN_NAME: admin
      SEMAPHORE_ADMIN_EMAIL: admin@localhost
      SEMAPHORE_ADMIN: admin
      SEMAPHORE_ACCESS_KEY_ENCRYPTION: gs72mPntFATGJs9qK0pQ0rKtfidlexiMjYCH9gWKhTU=
      SEMAPHORE_LDAP_ACTIVATED: 'no' # if you wish to use ldap, set to: 'yes' 
      SEMAPHORE_LDAP_HOST: dc01.local.example.com
      SEMAPHORE_LDAP_PORT: '636'
      SEMAPHORE_LDAP_NEEDTLS: 'yes'
      SEMAPHORE_LDAP_DN_BIND: 'uid=bind_user,cn=users,cn=accounts,dc=local,dc=shiftsystems,dc=net'
      SEMAPHORE_LDAP_PASSWORD: 'ldap_bind_account_password'
      SEMAPHORE_LDAP_DN_SEARCH: 'dc=local,dc=example,dc=com'
      SEMAPHORE_LDAP_SEARCH_FILTER: "(\u0026(uid=%s)(memberOf=cn=ipausers,cn=groups,cn=accounts,dc=local,dc=example,dc=com))"
      TZ: UTC
    depends_on:
      - mysql # for postgres, change to: postgres
volumes:
  semaphore-mysql: # to use postgres, switch to: semaphore-postgres
```

Docker-Container starten:

```
docker-compose up
```

Quelle: [Installation - Semaphore Docs](https://docs.semaphoreui.com/administration-guide/installation/#docker)
# Semaphore Web-GUI 

Das Web-GUI wird unter {Hostanmen}:3000 erreicht

Folgende Eingabemaske erscheint im Browser:
![](../../../praktische_Uebungen/Anhang/Pasted%20image%2020241022141908.png)

--> mit den in der "docker-compose.yml" definierten Credentials einloggen

# Repository einbinden

--> Projekt anlegen

1. im Register "Schlüsselspeicher" den privaten Key und die Passphrase hinterlegen
2. den öffentlichen Schlüssel im GitLab hinterlegen (Einstellungen/SSH Keys/)
3. im Register "Repository" das Repository mittel SSH-Adresse (git@gitlab330.shd-online.de:{User}/{Repository-Name}) + vorher hinterlegtem Schlüssel anlegen

![](../../../praktische_Uebungen/Anhang/Pasted%20image%2020241022143955.png)


# Playbooks abspielen

1. Inventar-Datei im Register "Inventar" hinterlegen -> Datei aus dem Repository nutzen
2. Im Register "Aufgabenvorlagen" eine neue Aufgabe erstellen (Ansible Playbook)
3. In der Aufgabe auf das Playbook im Repository verweisen sowie das Inventory angeben
4. den Button "Abspielen" betätigen