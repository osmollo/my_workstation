# Configuración de estación de trabajo con Ansible


[![pipeline status](https://gitlab.com/ohermosa/my_workstation/badges/master/pipeline.svg)](https://gitlab.com/ohermosa/my_workstation/-/commits/master)

## Ejecución

Dentro del directorio [ansible](ansible) se encuentran todas las herramientas necesarias para configurar una estación de trabajo con  **Ansible**, así como la documentación del mismo

Un ejemplo de ejecución de `ansible` para instalar todo el software disponible es el siguiente:

```bash
cd ansible
ansible-playbook install.yml -t extra_software
```

## Documentación

| :information_source: [La documentación de esta sección está disponible aquí](ansible/README.md) |
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

| :information_source: [La documentación de esta sección está disponible aquí](docker_deploys/README.md) |
| --- |
