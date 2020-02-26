# Ansible

- [Ansible](#ansible)
  - [Distribuciones soportadas](#distribuciones-soportadas)
  - [Software extra instalado](#software-extra-instalado)
  - [Prerequisitos](#prerequisitos)
  - [Instalación y configuración](#instalación-y-configuración)
    - [Instalación **DATIO**](#instalación-datio)
    - [Deshabilitar actualizaciones](#deshabilitar-actualizaciones)
    - [Gestión de contraseñas](#gestión-de-contraseñas)
      - [Ficheros locales](#ficheros-locales)
      - [Ansible Vault](#ansible-vault)
        - [Fichero de contraseñas](#fichero-de-contraseñas)
        - [Contraseñas cifradas](#contraseñas-cifradas)
  - [Otros playbooks](#otros-playbooks)
  - [Ejecución de comandos ansible ad-hoc](#ejecución-de-comandos-ansible-ad-hoc)
  - [Uso de Vagrant](#uso-de-vagrant)
  - [Actualización de CHANGELOG.md](#actualización-de-changelogmd)
  - [Emoji Cheat Sheet](#emoji-cheat-sheet)

## Distribuciones soportadas

| **DISTRIBUCIÓN** | **LINKS DE DESCARGA** |
|------------------|--------------|
| Debian | **STABLE (10)**: [Enlace](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-10.2.0-amd64-netinst.iso) <br> **TESTING (11)**: [Enlace](https://cdimage.debian.org/cdimage/weekly-builds/amd64/iso-cd/debian-testing-amd64-netinst.iso) |
| Ubuntu 18.04 | **UBUNTU**: [Enlace](http://releases.ubuntu.com/18.04.3/ubuntu-18.04.3-desktop-amd64.iso) <br> **KUBUNTU**: [Enlace](http://cdimage.ubuntu.com/kubuntu/releases/18.04/release/kubuntu-18.04.3-desktop-amd64.iso) <br> **XUBUNTU**: [Enlace](http://ftp.uni-kl.de/pub/linux/ubuntu-dvd/xubuntu/releases/18.04.3/release/xubuntu-18.04.3-desktop-amd64.iso) |
| Fedora | **30**: [Enlace](http://mirror.uv.es/mirror/fedora/linux/releases/30/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-30-1.2.iso) <br> **31**: [Enlace](https://download.fedoraproject.org/pub/fedora/linux/releases/31/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-31-1.9.iso) |
| Linux Mint 19 | **CINNAMON**: [Enlace](https://mirror.dogecloud.org/Linux/Mint/stable/19.2/linuxmint-19.2-cinnamon-64bit.iso) |
| KDE Neon | [Enlace](https://files.kde.org/neon/images/user/20191024-1119/neon-user-20191024-1119.iso) |
| Arch Linux | **TORRENT**: [Enlace](https://www.archlinux.org/releng/releases/2019.10.01/torrent/) |
| Manjaro | **GNOME**: [Enlace](https://osdn.net/frs/redir.php?m=dotsrc&f=%2Fstorage%2Fg%2Fm%2Fma%2Fmanjaro%2Fgnome%2F18.1.2%2Fmanjaro-gnome-18.1.2-191028-linux53.iso) <br> **KDE**: [Enlace](https://osdn.net/frs/redir.php?m=dotsrc&f=%2Fstorage%2Fg%2Fm%2Fma%2Fmanjaro%2Fkde%2F18.1.2%2Fmanjaro-kde-18.1.2-191028-linux53.iso) <br> **XFCE**: [Enlace](https://osdn.net/frs/redir.php?m=dotsrc&f=%2Fstorage%2Fg%2Fm%2Fma%2Fmanjaro%2Fxfce%2F18.1.2%2Fmanjaro-xfce-18.1.2-191028-linux53.iso) |

## Software extra instalado

Por defecto se instala el siguiente software:

| **APLICACIÓN** | **TAG/VARIABLE** | **GRUPO** |
|----------------|------------------|-----------|
| [Google Chrome](https://www.google.com/intl/es/chrome/) | install_chrome | install_browsers |
| [Chromium Browser](https://chromium.woolyss.com/download/es/) | install_chromium | install_browsers |
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
| [Ether Cloud Service Client](https://platform.bbva.com/en-us/developers/ether-cli/documentation/01-what-is) | install_ecs | |
| [Postman](https://www.getpostman.com) | install_postman | |
| [Skype](https://www.skype.com/es/) | install_skype | install_socials |
| [Java](https://openjdk.java.net/) | install_java | |
| [Apache Directory Studio](https://directory.apache.org/studio/downloads.html) | install_apachedirectory | |
| [Rambox](https://rambox.pro/#home) | install_rambox | |
| [Franz](https://meetfranz.com/) | install_franz | |
| [Deluge Torrent](https://deluge-torrent.org/) | install_deluge | |
| [Cherrytree](https://www.giuspen.com/cherrytree/) | install_cherrytree | install_editors |
| [Kubectl](https://kubernetes.io/es/docs/tasks/tools/install-kubectl/#instalar-kubectl) | install_kubectl | |
| [MEGAcmd](https://mega.nz/cmd) | install_megacmd | install_mega |
| [MEGA sync](https://mega.nz/sync) | install_megasync | install_mega |
| [Vivaldi](https://vivaldi.com/es/) | install_vivaldi | install_browsers |
| [Brave](https://brave-browser.readthedocs.io/en/latest/index.html) | install_brave | install_browsers |
| [Bitwarden](https://bitwarden.com/) | install_bitwarden | install_pass_managers |
| [Firefox 'Lexnet Edition'](https://www.mozilla.org/es-ES/firefox/all/#product-desktop-esr) | install_firefox_lexnet | install_browsers |
| [Pass](https://www.passwordstore.org/) | install_pass | install_pass_managers |
| [Bucklespring](https://github.com/zevv/bucklespring) | install_bucklespring | |
| [ProtonVPN](https://protonvpn.com/) | install_protonvpn | |
| [Prezto](https://github.com/sorin-ionescu/prezto) | install_prezto | |
| [Balena Etcher](https://www.balena.io/etcher/) | install_etcher | |
| [WoeUSB](https://github.com/slacka/WoeUSB) | install_woeusb | |
| [GO](https://golang.org/doc/install/source) | install_go | |
| [FZF](https://github.com/junegunn/fzf) | install_fzf | |
| [Vim plugins]() | install_vimplugins | |

En caso de que no se quiera instalar alguna de las anteriores aplicaciones, se puede indicar a través de las `extravars` con la correspondiente **variable** a `false`. Por ejemplo, para instalar todo el software extra excepto *Spotify* y *Oh my zsh!*:

```bash
ansible-playbook install.yml -e "install_spotify=false install_ohmyzsh=false"
```

En caso contrario, si lo único que se quiere hacer es instalar alguna de las aplicaciones, hay que usar el **tag** correspondiente, que coincide con las variables anteriores. Por ejemplo, para instalar *Visual Studio Code*:

```bash
ansible-playbook install.yml -t "install_code,install_dropbox_install_spotify"
```

## Prerequisitos

- El usuario que ejecute los playbooks debe tener `sudo` activado (se puede configurar con el playbook `config_sudo.yml`)
- Las tareas de este repositorio se ejecutan en local, por lo que para poder ejecutar los playbooks es necesario tener instalado `git` y `ansible`:

```bash
# Para Fedora
sudo dnf install git ansible

# Para Ubuntu
sudo apt install git ansible

# Para Arch
sudo pacman -S git ansible
```

A continuación habrá que clonar este repositorio (da igual el directorio de destino):

```bash
git clone https://gitlab.com/ohermosa/my_workstation.git /tmp/repo
cd /tmp/repo/ansible
```

Para preparar el equipo antes de lanzar el playbook principal, hay que ejecutar `prepare.yml` para instalar todos los requisitos previos:

```bash
ansible-playbook playbooks/prepare.yml
```

Esto realiza las siguientes tareas:

- Instalación de **Python3** y sus módulos correspondientes
- Configuración de `sudo` para sistemas **Debian**
- Actualización de `ansible` para sistemas **Debian** y **Ubuntu**
- Actualización de paquetes

## Instalación y configuración

Hay que ejecutar el siguiente comando:

```bash
ansible-playbook install.yml --ask-vault-pass
```

En caso de querer instalar únicamente alguna de las [aplicaciones de terceros disponibles](#software-extra-instalado), hay que usar el tag correspondiente:

```bash
ansible-playbook install.yml -t install_atom
```

### Instalación **DATIO**

Para realizar una configuración general para un pc de trabajo en [Datio](www.datio.com), hay que ejecutar el siguiente playbook:

```bash
ansible-playbook datio.yml --ask-vault-pass
```

### Deshabilitar actualizaciones

Una de las primeras tareas que se ejecutan es la actualización de los paquetes del sistema. Esta tarea no se lanzará si hace menos de una semana que se ha ejecutado pero también es posible deshabilitarla de las siguientes formas:

- Variable de entorno

Hay que exportar la variable `REPO_DISABLE_UPDATES` con valor _1_. Cualquier otro valor se considerará _false_ y se actualizarán los paquetes

```bash
export REPO_DISABLE_UPDATES=1
```

- Extravars

```bash
ansible-playbook install.yml -e disable_updates=true
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

Para las siguientes opciones, es necesario indicar que se pida la contraseña de descifrado al ejecutar el playbook usando el flag `--ask-vault-pass`.

Es posible evitar esta incomodidad (hay que teclear la contraseña en cada ejecución del playbook), creando un fichero `$HOME/.vault_pass.txt` con la contraseña en texto plano (hay que dar permisos 600 al fichero para más seguridad) y declarando la variable `ANSIBLE_VAULT_PASSWORD_FILE` con la ruta de ese fichero:

```bash
echo "mi_contraseña" > $HOME/.vault_pass.txt
export ANSIBLE_VAULT_PASSWORD_FILE=$HOME/.vault_pass.txt
```

Con esto, ya no sería necesario incluir el flag `--ask-vault-pass`. Al finalizar la ejecución del playbook puede borrarse el fichero sin problema

##### Fichero de contraseñas

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
ansible-playbook post_install.yml -e "post_install_user=dsamaniego"  --ask-vault-pass
```

Para editar el fichero habría que usar el siguiente comando (o bien instalar alguna extensión en el editor de textos que permita trabajar con estos ficheros)

```bash
ansible-vault secrets/main.yml edit
Vault password:
```

La ventaja de este método es que podemos tener las contraseñas cifradas bajo el control de git sin riesgos de seguridad ya que no pueden ser vistas por otros usuarios

##### Contraseñas cifradas

Otra opción haciendo uso de `ansible-vault` es cifrar contraseñas con esta herramienta y pegar el hash dentro del fichero *defaults/main.yml* del role. Para ello, para cifrar una cadena de texto (la contraseña), hay que ejecutar el siguiente comando:

```bash
ansible-vault encrypt_string ceporro
New Vault password:
Confirm New Vault password:
!vault |
          $ANSIBLE_VAULT;1.1;AES256
          35393661323635626162626262626537626465313232666537616134353532376536363537366533
          3138343938353264346662333561333362653661376564370a343735373865613536356538393137
          62326139303938323664303432336164383732643735636536326365373733363066336565666536
          6161343931623434640a386664336236373035623466613839333339333733346264663861393364
          3937
Encryption successful
```

La salida del anterior comando se debe copiar dentro del fichero **defaults/main.yml** con el siguiente formato:

```yaml
ceporro: !vault |
  $ANSIBLE_VAULT;1.1;AES256
  35393661323635626162626262626537626465313232666537616134353532376536363537366533
  3138343938353264346662333561333362653661376564370a343735373865613536356538393137
  62326139303938323664303432336164383732643735636536326365373733363066336565666536
  6161343931623434640a386664336236373035623466613839333339333733346264663861393364
  3937
```

Para poder descrifrar esta contraseña al ejecutar el playbook, habrá que incluír el argumento `--ask-vault-pass` e indicar la contraseña que se usó en el paso anterior para cifrar la password:

```bash
ansible-playbook post_install -e post_install_user=--ask-vault-pass
```

## Otros playbooks

[Documentado aquí](playbooks/README.md)

## Ejecución de comandos ansible ad-hoc

```bash
ansible localhost -m shell -a "df -h"
```

## Uso de Vagrant

:information_source: El __usuario/contraseña__ de las máquinas virtuales es `vagrant/vagrant`

Para probar el código, se puede levantar una máquina virtual usando [Vagrant](https://www.vagrantup.com/) y [Virtualbox](https://www.virtualbox.org/). Para ello, será necesario instalar *Virtualbox* usando el tag `--install_virtualbox`:

```bash
ansible-playbook install.yml  -t install_virtualbox
```

A continuación, dentro del directorio del repo, hay que ejecutar el siguiente comando para levntar la máquina virtual:

```bash
vagrant up [mint|kubuntu|ubuntu|xubuntu|fedora30|fedora31|arch|manjaro|debian]
```

Cuando se inicie la máquina, se lanzará automáticamente el playbook `vagrant.yml` que instala el role `common` y `extra_software`. Si se quiere lanzar *ansible* desde el anfitrión, habrá que ejecutar el playbook correspondiente usando el inventario de la máquina vagrant que hayamos levantado:

```bash
ansible-playbook -i ansible_hosts vagrant/install.yml
ansible-playbook -i ansible_hosts vagrant/post_install.yml -e post_install_user=ohermosa
```

Y para destruir las máquinas:

```bash
vagrant destroy -f
```

## Actualización de CHANGELOG.md

Para poder actualizar el [CHANGELOG.md](CHANGELOG.md) con los cambios que se han realizado entre 2 tags hay que ejecutar el siguiente comando:

```bash
git log --pretty=oneline <tag_antiguo> <tag_nuevo>
```

Y entre el último tag y el último commit:

```bash
git log --pretty=oneline HEAD...tag
```

## Emoji Cheat Sheet

[Aquí](https://www.webfx.com/tools/emoji-cheat-sheet/) se puede encontrar la lista de emojis disponibles para **markdown**
