# Configuración de estación de trabajo con Ansible

- [Configuración de estación de trabajo con Ansible](#configuración-de-estación-de-trabajo-con-ansible)
  - [Software extra instalado](#software-extra-instalado)
  - [Prerequisitos](#prerequisitos)
  - [Actualización de paquetes](#actualización-de-paquetes)
  - [Instalación](#instalación)
  - [Post Instalación](#post-instalación)
    - [Gestión de contraseñas](#gestión-de-contraseñas)
      - [Ficheros locales](#ficheros-locales)
      - [Ansible Vault](#ansible-vault)
  - [Ejecución de comandos ansible ad-hoc](#ejecución-de-comandos-ansible-ad-hoc)
  - [Uso de Vagrant](#uso-de-vagrant)

## Software extra instalado

| **WARNING**: Estos playbooks se han probado únicamente en **Ubuntu 18.04** y **Fedora 30** |
| --- |

Por defecto se instala el siguiente software:

| **APLICACIÓN** | **TAG/VARIABLE** | **GRUPO** |
|----------------|------------------|-----------|
| [Google Chrome](https://www.google.com/intl/es/chrome/) | install_chrome | |
| [Docker](https://docs.docker.com/install/linux/docker-ce/) | install_docker | |
| [Dropbox](https://www.dropbox.com/) | install_dropbox | |
| [Visual Studio Code](https://code.visualstudio.com/) | install_code | install_editors |
| [Spotify](https://www.spotify.com/es/premium/?checkout=false) | install_spotify | |
| [Oh my ZSH!](https://ohmyz.sh/) | install_ohmyzsh | |
| [Sublime Text](https://www.sublimetext.com/) | install_sublime | install_editors |
| [Atom](https://atom.io/) | install_atom | |
| [Gitkraken](https://www.gitkraken.com/git-client) | install_gitkraken | |
| [Telegram Desktop](https://telegram.org/) | install_telegram | install_socials |
| [Slack](https://datiodevelopers.slack.com/) | install_slack | install_socials |
| [Forticlient VPN](https://www.fortinet.com/lat) | install_forticlientvpn | |
| [TLP](https://linrunner.de/en/tlp/docs/tlp-linux-advanced-power-management.html) | install_tlp | |
| [Virtualbox](https://www.virtualbox.org/) | install_virtualbox | |
| [PyCharm Community](https://www.jetbrains.com/pycharm/download/#section=linux) | install_pycharm | install_editors |
| [KeepassXC](https://keepassxc.org/download/) | install_keepass | install_pass_managers |
| [Buttercup](https://buttercup.pw/) | install_buttercup | install_pass_managers |
| [Windscribe](https://windscribe.com/) | install_windscribe | |
| [Teamviewer](https://www.teamviewer.com/es/) | install_teamviewer | install_remotes |
| [NoMachine](https://www.nomachine.com/es/) | install_nomachine | install_remotes |

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
* Para poder instalar *Telegram* o *Spotify*, es necesario tener actualizado **Ansible** a la versión 2.6 o superior. Para ello hay que ejecutar el siguiente playbook:

```bash
ansible-playbook update_ansible.yml --ask-become-pass
```

## Actualización de paquetes

Tanto si se ejecuta el playbook en **Ubuntu** como en **Fedora**, se pueden actualizar todos los paquetes con el siguiente playbook:

```bash
ansible-playbook update_packages.yml --ask-become-pass
```

Es recomemdable ejecutar este playbook nada más instalar el ordenador y antes de lanzar el resto de playbooks para que todos los paquetes se encuentren actualizados y no haya problema con dependencias

## Instalación

La primera tarea que ejecuta este playbook es actualizar los paquetes de la distribución que se esté usando dentro de la misma rama, nunca se actualiza la distribución a la siguiente versión disponible

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

### Gestión de contraseñas

En caso de que sea necesario usar contraseñas en alguna tarea de Ansible, hay varias opciones

#### Ficheros locales

Las contraseñas se pueden definir como variables en ficheros *"yml"* al igual que el resto de variables pero sin estar bajo el seguimiento de **git**. Para ello no es necesario tenerlo fuera del directorio del repositorio sino que basta con incluír el nombre del fichero donde tengamos las contraseñas en un fichero *.gitignore*.

```text
post_install
├── dsamaniego
    ├── secrets
    │   └── main.yml
```

Para usar el fichero de contraseñas, habrá que usar la siguiente tarea de Ansible:

```yaml
- name: "include secrets file"
  include_vars:
    file: "secrets/main.yml"
```

Podedmos incluír la ruta al *main.yml* en el *.gitignore* que hay en el raíz o crear uno nuevo en el mismo direscorio secrets:

```bash
cat roles/post_install/dsamaniego/.gitignore
secrets/main.yml
```

La ventaja de este método es que mantenemos las contraseñas fuera de **git** pero con la contrapartida de que el fichero es local, si en algún momento se clona el repositorio en otra máquina, habrá que copiar manualmente este fichero a ese ordenador. **Ojo cuidado**, que el fichero es local pero tendría las contraseñas en texto plano!

#### Ansible Vault

Vault tiene una herramienta `ansible-vault` que permite cifrar ficheros (con AES256) donde almacenar contraseñas. El formato de estos ficheros es exactamente el mismo que otros donde se almacenan variables solo que hay que cifrarlo/descifrarlo para su uso con una contraseña que se establece en el momento de su creación.

```bash
ansible-vault secrets/main.yml create
New Vault password:
Confirm New Vault password:
```

Si hacemos un cat del fichero, no podremos ver el contenido:

```txt
cat secrets/main.yml
$ANSIBLE_VAULT;1.1;AES256
64643661633666333836396338656364383734636638626332623166656335623964616462616263
6237326165336231333037343136353664396265356635630a333231333238323863303832336661
30626366353162613539623962363264363532323934663862373136363163656537666533373833
6437346566356639360a666463643338656235393866626439353034336435663032643764393330
63626332616533303338396339653963633261326336353231393863623335346532
```

Para usar este fichero de variables, habría que usar la misma tarea de Ansible que en el caso anterior:

```yaml
- name: "include secrets file"
  include_vars:
    file: "secrets/main.yml"
```

Y para ejecutar el playbook hay que agregar el parámetro `--ask-vault-pass` para que pueda descrifrar el fichero de contraseñas:

```bash
ansible-playbook post_install.yml -e "post_install_user=dsamaniego" --ask-become-pass --ask-vault-pass
```

Para editar el fichero habría que usar el siguiente comando (o bien instalar alguna extensión en el editor de textos que permita trabajar con estos ficheros)

```bash
ansible-vault secrets/main.yml edit
Vault password:
```

La ventaja de este método es que podemos tener las contraseñas cifradas bajo el control de git sin riesgos de seguridad ya que no pueden ser vistas por otros usuarios

## Ejecución de comandos ansible ad-hoc

```bash
ansible localhost -m shell -a "df -h"
```

## Uso de Vagrant

Para probar el código, se puede levantar una máquina con **Ubuntu** o **Fedora** usando [Vagrant](https://www.vagrantup.com/) y [Virtualbox](https://www.virtualbox.org/). Para ello, será necesario instalar *Virtualbox* usando el tag `--install_virtualbox`:

```bash
ansible-playbook install.yml --ask-become-pass -t install_virtualbox
```

A continuación, dentro del directorio del repo, hay que ejecutar el siguiente comando para levntar la máquina virtual:

```bash
vagrant up [ubuntu|fedora]
```
