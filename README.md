- [Configuración de estación de trabajo con Ansible](#configuración-de-estación-de-trabajo-con-ansible)
  - [Ejecución](#ejecución)
  - [Documentación](#documentación)
- [Despliegue de aplicaciones con Docker](#despliegue-de-aplicaciones-con-docker)
  - [Lanzar un deploy](#lanzar-un-deploy)
  - [Documentación](#documentación-1)


# Configuración de estación de trabajo con Ansible

## Ejecución

Dentro del directorio [ansible](ansible) se encuentran todas las herramientas necesarias para configurar una estación de trabajo con  **Ansible**. Allí se podrá encontrar toda la documentación necesaria para su ejecución.

Un ejemplo de ejecución de ansible para instalar todo el software disponible es el siguiente:

```bash
cd ansible
ansible-playbook install.yml --ask-become-pass
```

Si el fichero `docker-compose.yml` tuviera otro nombre:

```bash
cd <directory>
docker-compose -f vault.yml up -d
```

## Documentación

| **WARNING**: [La documentación de esta sección está disponible aquí](ansible/README.md) |
| --- |

# Despliegue de aplicaciones con Docker

Dentro del directorio [docker_deploys](docker_deploys) se encuentra, organizado en subdirectorios, el despliegue de diversas aplicaciones usando **Docker** mediante el uso de la herramienta `docker-compose`.

## Lanzar un deploy

```bash
cd <directory>
docker-compose up -d
```

Si el fichero `docker-compose.yml` tuviera otro nombre:

```bash
cd <directory>
docker-compose -f vault.yml up -d
```

## Documentación

| **WARNING**: [La documentación de esta sección está disponible aquí](docker_deploys/README.md) |
| --- |
