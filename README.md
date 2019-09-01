# Configuración de estación de trabajo con Ansible

- [Configuración de estación de trabajo con Ansible](#configuración-de-estación-de-trabajo-con-ansible)
  - [Software extra instalado](#software-extra-instalado)
  - [Prerequisitos](#prerequisitos)
  - [Instalación](#instalación)
  - [Post Instalación](#post-instalación)
  - [Ejecución de comandos ansible ad-hoc](#ejecución-de-comandos-ansible-ad-hoc)
  - [Uso de Vagrant](#uso-de-vagrant)

## Software extra instalado

| **WARNING**: Estos playbooks se han probado únicamente en **Ubuntu 18.04** y **Fedora 30** |
| --- |

Por defecto se instala el siguiente software:

| Aplicación | TAG/Variable |
|------------|--------------|
| [Docker](https://docs.docker.com/install/linux/docker-ce/) | install_docker |
| [Dropbox](https://www.dropbox.com/) | install_dropbox |
| [Visual Studio Code](https://code.visualstudio.com/) | install_code |
| [Spotify](https://www.spotify.com/es/premium/?checkout=false) | install_spotify |
| [Oh my ZSH!](https://ohmyz.sh/) | install_ohmyzsh |
| [Sublime Text](https://www.sublimetext.com/) | install_sublime |
| [Atom](https://atom.io/) | install_atom |
| [Gitkraken](https://www.gitkraken.com/git-client) | install_gitkraken |
| [Telegram Desktop](https://telegram.org/) | install_telegram |
| [Slack](https://datiodevelopers.slack.com/) | install_slack |
| [Forticlient VPN](https://www.fortinet.com/lat) | install_forticlientvpn |
| [TLP](https://linrunner.de/en/tlp/docs/tlp-linux-advanced-power-management.html) | install_tlp |
| [Virtualbox](https://www.virtualbox.org/) | install_virtualbox |
| [PyCharm Community](https://www.jetbrains.com/pycharm/download/#section=linux) | install_pycharm |

En caso de que no se quiera instalar alguna de las anteriores aplicaciones, se puede indicar a través de las `extravars` con la correspondiente **variable** a `false`. Por ejemplo, para instalar todo el software extra excepto *Spotify* y *Oh my zsh!*:

```bash
ansible-playbook install.yml --ask-become-pass -e "install_spotify=false install_ohmyzsh=false"
```

En caso contrario, si lo único que se quiere hacer es instalar alguna de las aplicaciones, hay que usar el **tag** correspondiente, que coincide con las variables anteriores. Por ejemplo, para instalar *Visual Studio Code*:

```bash
ansible-playbook install.yml --ask-become-pass -t "install_code"
```

## Prerequisitos

* La distribución del sistema debe ser [Ubuntu](https://ubuntu.com/download/desktop) o [Fedora](https://getfedora.org/es/workstation/)
* El usuario que ejecute los playbooks debe tener `sudo` activado e incluír `--ask-become-pass` para ejecutar el playbook con permisos de administrador
* Las tareas de este repositorio se ejecutan en local, por lo que para poder ejecutar los playbooks es necesario tener instalado `git` y `ansible`
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

El role `post_install` tiene como objetivo terminar de configurar el entorno personalizándolo como prefiera el usuario. Dentro del directorio del role, debe ir un subdirectorio con el nombre del usuario que también se pasará como variable a través de `extravars` con la variable `post_install_user`:

```bash
ansible-playbook post_install.yml -e "post_install_user=ohermosa" --ask-become-pass
```

Un ejemplo de cómo debe ser la jerarquía de directorios del role `post_install` es el siguiente:

```text
post_install
├── dsamaniego
│   ├── defaults
│   │   └── main.yml
│   ├── tasks
│   │   ├── main.yml
│   │   └── maki.yml
│   └── templates
│       └── burrito.j2
└── ohermosa
    ├── defaults
    │   └── main.yml
    ├── tasks
    │   ├── crontab.yml
    │   ├── docker.yml
    │   ├── environment.yml
    │   ├── git.yml
    │   ├── main.yml
    │   └── openvpn.yml
    └── templates
        ├── bbva_vpn.j2
        └── datio_mx_vpn.j2
```

## Ejecución de comandos ansible ad-hoc

```bash
ansible localhost -m shell -a "df -h"
```

## Uso de Vagrant

Para probar el código, se puede levantar una máquina con **Ubuntu** o **Fedora** usando [Vagrant](https://www.vagrantup.com/) y [Virtualbox](https://www.virtualbox.org/). Para ello, será necesario instalar *Virtualbox* usando el tag `--install_virtualbox`:

```bash
ansible-playbook install.yml --ask-become-pass -t install_virtualbox
```

A continuación, dentro del directorio del repo, hay que ejecutar:

```bash
vagrant init
```

Este comando creará un fichero `Vagrantfile` donde tendremos que sobreescribir la configuración de los ficheros existentes en el repo `Vagrantfile_ubuntu` o `Vagrantfile_fedora`:

```bash
cat Vagrantfile_ubuntu > Vagrantfile
```

A continuación, podemos levantar la máquina virtual:

```bash
vagrant up
```
