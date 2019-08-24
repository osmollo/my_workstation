# Configuración de estación de trabajo con Ansible

- [Configuración de estación de trabajo con Ansible](#configuración-de-estación-de-trabajo-con-ansible)
  - [Software extra instalado](#software-extra-instalado)
  - [Prerequisitos](#prerequisitos)
  - [Instalación](#instalación)
  - [Post Instalación](#post-instalación)
  - [Ejecución de comandos ansible ad-hoc](#ejecución-de-comandos-ansible-ad-hoc)

## Software extra instalado

* [Docker](https://docs.docker.com/install/linux/docker-ce/)
* [Dropbox](https://www.dropbox.com/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Spotify](https://www.spotify.com/es/premium/?checkout=false)
* [Oh my ZSH!](https://ohmyz.sh/)

## Prerequisitos

* El usuario que ejecute los playbooks debe tener `sudo` activado e incluír `--ask-become-pass` para ejecutar el playbook con permisos de administrador
* En la post instalación, se crearán enlaces simbólicos desde el directorio */home/{{ ansible_user }}/Dropbox/datio*, será necesario modificar este directorio si no es correcto

## Instalación

```bash
ansible-playbook install.yml --ask-vault-pass --ask-become-pass
```

## Post Instalación

```bash
ansible-playbook post_install.yml --ask-vault-pass --ask-become-pass
```

## Ejecución de comandos ansible ad-hoc

```bash
ansible localhost -m shell -a "df -h"
```
