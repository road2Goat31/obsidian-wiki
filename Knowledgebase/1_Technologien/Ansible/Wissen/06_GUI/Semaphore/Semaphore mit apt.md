
# Installation 

sudo adduser --system --group --home /home/semaphore semaphore

sudo apt install mariadb-server

sudo mysql_secure_installation
```
	kein root passwort eingeben
	unix_socket authentication: no
	Change root password: mkspasswort
	remove anonymous users: yes
	disallow root login remotely: yes
	remove test database: yes
	reload the priviledge table: yes
```


sudo mariadb
	CREATE DATABASE semaphore_db;
	GRANT ALL PRIVILIDGES ON semaphore_db.* TO semaphore_user@localhost IDENTIFIED ' mkspasswort';
	FLUSH PRIVILEGES

wget https://github.com/semaphoreui/semaphore/releases/download/v2.10.30/semaphore_2.10.30_linux_amd64.deb

sudo apt install ./semaphore_2.10.30_linux_amd64.deb

semaphore setup:

	default database
	no Hostname
	db USER: semaphore_user
	Passwort: mkspasswort
	db Name: semaphore_db
	Playbook Path: /home/maik/ansible
	no url
	no email alerts
	 ... no
	Config output directory:
	/etc/semaphore/semaphore_config_output


`sudo chown semaphore:semaphore config.json`

`sudo mkdir /etc/semaphore`

`sudo chown semaphore:semaphore /etc/semaphore`

`sudo mv config.json /etc/semaphore`

`semaphore server --config /etc/semaphore/config.json`

 --> Server ist unter dem Link erreichbar [Semaphore UI](http://172.20.17.1:3000/auth/login)
 --> aber nur so lange wie man den Befehl auf der CLI ausführt


--> deshalb wird ein Semaphore.service erstellt, der es im Hintergrund laufen lässt

`sudo nano /etc/systemd/system/semaphore.service`

```
[Unit]
Description=Ansible Semaphore
Documentation=htpps://docs.ansible-semaphore.com/
Wants=network-online.target
After=network-online.target

[Service]
Type=Simple
ExecStart=/usr/bin/semaphore server --config /etc/semaphore/config.json
ExecReload=/bin/kill -HUP $MAINPID
Restart=always
Restart=10s
User=semaphore
Group=semaphore

[Install]
WantedBy=multi-user.target
```


`sudo systemctl daemon-reload`

`systemctl status semaphore.service`

`sudo systemctl enable semaphore.service`

`sudo systemctl start semaphore.service`


--> Semaphore GUI ist über die IP-Adresse verfügbar (über den Port 3000)

