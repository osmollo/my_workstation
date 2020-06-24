# Docker Deploys

Para `docker-compose`, hay que ejecutar el siguiente comando:

```bash
cd ansible
ansible-playbook install.yml -t install_docker --ask-bacome-pass
```

## Despliegues disponibles

| **SUBDIRECTORIO** | **DESCRIPCIÓN** |
|-------------------|-----------------|
| [vault](vault/) | Despliegue de `Vault` usando `Consul` como backend |
| [nextcloud](nextcloud/) | Despliegue de `Nextcloud` con `MariaDB` como base de datos |
| [pi-hole](pihole/) | Despliegue de `PiHole` |
| [Jenkins](jenkins/) | Despliegue de `Jenkins` |
| [Gitea](gitea/) | Despliegue de `Gitea` con `MySQL` |
| [Bitwarden](bitwarden/) | Despliegue de `Bitwarden` |
| [Kafka](kafka/) | Despliegue de `Kafka` usando `Zookeeper` como backend |
| [Consul](consul/) | Despliegue de `Consul` |
| [Wireguard](wireguard/) | Despliegue del servicio VPN `Wireguard` |
| [torrent_raspi](torrent_raspi/) | Despliegue de sistema automático de descargas en **Raspberry** usando `transmission` y gestión de contenidos con `plex` |
