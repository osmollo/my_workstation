# My Workstation

[![pipeline status](https://gitlab.com/ohermosa/my_workstation/badges/master/pipeline.svg)](https://gitlab.com/ohermosa/my_workstation/-/commits/master)

- [My Workstation](#my-workstation)
  - [Configuración de estación de trabajo con Ansible](#configuración-de-estación-de-trabajo-con-ansible)
    - [Ejecución](#ejecución)
    - [Documentación](#documentación)
  - [Despliegue de aplicaciones con Docker](#despliegue-de-aplicaciones-con-docker)
    - [Lanzar un deploy con docker-compose](#lanzar-un-deploy-con-docker-compose)
    - [Documentación despliegues en Docker](#documentación-despliegues-en-docker)
  - [Despliegue de aplicaciones en Kubernetes](#despliegue-de-aplicaciones-en-kubernetes)
    - [Lanzar un deploy en kubernetes](#lanzar-un-deploy-en-kubernetes)
    - [Documentación despliegues en Kubernetes](#documentación-despliegues-en-kubernetes)

## Configuración de estación de trabajo con Ansible

### Ejecución

Dentro del directorio [ansible](ansible) se encuentran todas las herramientas necesarias para configurar una estación de trabajo con  **Ansible**, así como la documentación del mismo

Un ejemplo de ejecución de `ansible` para instalar todo el software disponible es el siguiente:

```bash
cd ansible
ansible-playbook install.yml -t extra_software
```

### Documentación

| :information_source: [La documentación de esta sección está disponible aquí](ansible/README.md) |
| --- |

## Despliegue de aplicaciones con Docker

Dentro del directorio [docker_deploys](docker_deploys) se encuentra, organizado en subdirectorios, el despliegue de diversas aplicaciones usando **Docker** mediante el uso de la herramienta `docker-compose`.

### Lanzar un deploy con docker-compose

```bash
cd <directory>
docker-compose up -d
```

Si el fichero `docker-compose.yml` tuviera otro nombre:

```bash
cd <directory>
docker-compose -f vault.yml up -d
```

### Documentación despliegues en Docker

| :information_source: [La documentación de esta sección está disponible aquí](docker_deploys/README.md) |
| --- |


## Despliegue de aplicaciones en Kubernetes

Dentro del directorio [k8s_deploys](./k8s_deploys/), se encuentran los directorios correspondientes a diferentes aplicaciones para desplegar en **Kubernetes**

### Lanzar un deploy en kubernetes

```bash
cd <directory>
kubectl apply -f .
```

### Documentación despliegues en Kubernetes

| :information_source: [La documentación de esta sección está disponible aquí](./k8s_deploys/README.md)
| --- |
