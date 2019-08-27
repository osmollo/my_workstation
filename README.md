# Configuración de estación de trabajo con Ansible

- [Configuración de estación de trabajo con Ansible](#configuración-de-estación-de-trabajo-con-ansible)
  - [Software extra instalado](#software-extra-instalado)
  - [Prerequisitos](#prerequisitos)
  - [Instalación](#instalación)
  - [Post Instalación](#post-instalación)
  - [Ejecución de comandos ansible ad-hoc](#ejecución-de-comandos-ansible-ad-hoc)

## Software extra instalado

Por defecto se instala el siguiente software:

* [Docker](https://docs.docker.com/install/linux/docker-ce/)
* [Dropbox](https://www.dropbox.com/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Spotify](https://www.spotify.com/es/premium/?checkout=false)
* [Oh my ZSH!](https://ohmyz.sh/)
* [Sublime Text](https://www.sublimetext.com/)
* [Atom](https://atom.io/)
* [Gitkraken](https://www.gitkraken.com/git-client)
* [Telegram Desktop](https://telegram.org/)
* [Slack](https://datiodevelopers.slack.com/)

En caso de que no se quiera instalar alguna de las anteriores aplicaciones, se puede indicar a través de las `extravars` con la correspondiente variable a `false`:

* install_docker
* install_dropbox
* install_code
* install_spotify
* install_ohmyzsh
* install_sublime
* install_atom
* install_gitkraken
* install_telegram
* install_slack

Por ejemplo, para instalar todo el software extra excepto *Spotify* y *Oh my zsh!*:

```bash
ansible-playbook install.yml --ask-become-pass -e "install_spotify=false install_ohmyzsh=false"
```

En caso contrario, si lo único que se quiere hacer es instalar alguna de las aplicaciones, hay que usar el tag correspondiente, que coincide con las variables anteriores. Por ejemplo, para instalar *Visual Studio Code*:

```bash
ansible-playbook install.yml --ask-become-pass -t "install_code"
```

## Prerequisitos

* La distribución del sistema debe ser [Ubuntu](https://ubuntu.com/download/desktop) o [Fedora](https://getfedora.org/es/workstation/)
* El usuario que ejecute los playbooks debe tener `sudo` activado e incluír `--ask-become-pass` para ejecutar el playbook con permisos de administrador
* En la post instalación, se crearán enlaces simbólicos desde el directorio */home/{{ ansible_user }}/Dropbox/datio*, será necesario modificar este directorio si no es correcto
* Para poder instalar *Telegram* o *Spotify*, es necesario tener actualizado **Ansible** a la versión 2.6 o 2.8, respectivamente. Para ello hay que ejecutar el siguiente playbook:

```bash
ansible-playbook update_ansible.yml --ask-become-pass
```

## Instalación

```bash
ansible-playbook install.yml --ask-become-pass
```

## Post Instalación

```bash
ansible-playbook post_install.yml --ask-become-pass
```

## Ejecución de comandos ansible ad-hoc

```bash
ansible localhost -m shell -a "df -h"
```
