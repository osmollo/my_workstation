# Docker Deploys

Para `docker-compose`, hay que ejecutar el siguiente comando:

```bash
cd ansible
ansible-playbook install.yml -t install_docker --ask-bacome-pass
```

## Despliegues disponibles

| **SUBDIRECTORIO** | **DESCRIPCIÓN** |
|-------------------|-----------------|
| [vault](docker_deploys/vault) | Despliegue de `Vault` usando `Consul` como backend |
| [nextcloud](docker_deploys/nextcloud) | Despliegue de `Nextcloud` con `MariaDB` como base de datos |
| [pi-hole](docker_deploys/pihole) | Despliegue de `PiHole` |
| [Jenkins](docker_deploys/jenkins) | Despliegue de `Jenkins` |
| [Gitea](docker_deploys/gitea) | Despliegue de `Gitea` con `MySQL` |
| [Bitwarden](docker_deploys/bitwarden) | Despliegue de `Bitwarden` |
