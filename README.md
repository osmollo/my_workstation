- [Configuración de estación de trabajo con Ansible](#configuración-de-estación-de-trabajo-con-ansible)
  - [Software extra instalado](#software-extra-instalado)
  - [Prerequisitos](#prerequisitos)
  - [Instalación](#instalación)
  - [Post Instalación](#post-instalación)

# Configuración de estación de trabajo con Ansible

## Software extra instalado

 * [Docker](https://docs.docker.com/install/linux/docker-ce/)
 * [Dropbox](https://www.dropbox.com/)
 * [Visual Studio Code](https://code.visualstudio.com/)
 * [Spotify](https://www.spotify.com/es/premium/?checkout=false)
 * [Oh my ZSH!](https://ohmyz.sh/)

## Prerequisitos

 * El usuario `ohermosa` debe estar creado en la máquina `sudo` activado
 * En la post instalación, se crearán enlaces simbólicos desde el directorio */home/{{ ansible_user }}/Dropbox/datio*, será necesario modificar este directorio si no es correcto

## Instalación

Para ejecutar el playbook de instalación, es necesario definir la variable `target` en el extravars con el nombre de la máquina que se quiere instalar

```bash
ansible-playbook -i inventory/workstation install.yml -e "target=eusebio" --ask-vault-pass --ask-become-pass
```

## Post Instalación

Para ejecutar el playbook de post instalación, es necesario definir la variable `target` en el extravars con el nombre de la máquina que se quiere instalar

```bash
ansible-playbook -i inventory/workstation post_install.yml -e "target=rufino" --ask-vault-pass --ask-become-pass
```
