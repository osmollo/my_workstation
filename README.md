- [Configuración de estación de trabajo con Ansible](#configuración-de-estación-de-trabajo-con-ansible)
  - [Ejecución](#ejecución)
  - [Documentación](#documentación)
- [Despliegue de aplicaciones con Docker](#despliegue-de-aplicaciones-con-docker)
  - [Despliegues disponibles](#despliegues-disponibles)
  - [Documentación](#documentación-1)


# Configuración de estación de trabajo con Ansible

## Ejecución

Dentro del directorio `ansible` se encuentran todas las herramientas necesarias para configurar una estación de trabajo con  **Ansible**. Allí se podrá encontrar toda la documentación necesaria para su ejecución.

Un ejemplo de ejecución de ansible para instalar todo el software disponible es el siguiente:

```bash
cd ansible
ansible-playbook install.yml --ask-become-pass
```

## Documentación

| **WARNING**: [La documentación de esta sección está disponible aquí](ansible/README.md) |
| --- |

# Despliegue de aplicaciones con Docker

Dentro del directorio `docker_deploys` se encuentra, organizado en subdirectorios, el despliegue de diversas aplicaciones usando **Docker** mediante el uso de la herramienta `docker-compose`. Para instalarla, puede ejecutar el siguiente comando:

```bash
cd ansible
ansible-playbook install.yml -t install_docker --ask-bacome-pass
```

## Despliegues disponibles

| **SUBDIRECTORIO** | **DESCRIPCIÓN** |
|-------------------|-----------------|
| [./vault](docker_deploys/vault) | Despliegue de `Vault` usando `Consul` como backend e incluyendo interfaz web y backup de datos |
| [./nextcloud](docker_deploys/nextcloud) | Despliegue de `Nextcloud` con `MariaDB` como base de datos |

## Documentación

| **WARNING**: [La documentación de esta sección está disponible aquí](docker_deploys/README.md) |
| --- |
