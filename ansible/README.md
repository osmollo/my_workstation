# Ansible

- [Ansible](#ansible)
  - [Distribuciones soportadas](#distribuciones-soportadas)
  - [Software extra instalado](#software-extra-instalado)
  - [¿Cómo se usa?](#cómo-se-usa)
    - [Post instalación](#post-instalación)
    - [Deshabilitar actualizaciones](#deshabilitar-actualizaciones)
  - [Otros playbooks](#otros-playbooks)
  - [Ejecución de comandos ansible ad-hoc](#ejecución-de-comandos-ansible-ad-hoc)
  - [Uso de Vagrant](#uso-de-vagrant)
  - [Actualización de CHANGELOG.md](#actualización-de-changelogmd)
  - [Emoji Cheat Sheet](#emoji-cheat-sheet)

## Distribuciones soportadas

| **DISTRIBUCIÓN** | **LINKS DE DESCARGA** |
|------------------|--------------|
| Debian | **STABLE (10)**: [Enlace](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-10.2.0-amd64-netinst.iso) <br> **TESTING (11)**: [Enlace](https://cdimage.debian.org/cdimage/weekly-builds/amd64/iso-cd/debian-testing-amd64-netinst.iso) |
| Deepin | **20**: [Enlace](http://www.mediafire.com/file/re4yrj5o5uj1mh7/deepin-desktop-community-1002-amd64.iso.torrent/file) |
| Ubuntu 18.04 | **UBUNTU**: [Enlace](http://releases.ubuntu.com/18.04.3/ubuntu-18.04.3-desktop-amd64.iso) <br> **KUBUNTU**: [Enlace](http://cdimage.ubuntu.com/kubuntu/releases/18.04/release/kubuntu-18.04.3-desktop-amd64.iso) <br> **XUBUNTU**: [Enlace](http://ftp.uni-kl.de/pub/linux/ubuntu-dvd/xubuntu/releases/18.04.3/release/xubuntu-18.04.3-desktop-amd64.iso) |
| Ubuntu 20.04 | **UBUNTU**: [Enlace](https://releases.ubuntu.com/20.04/ubuntu-20.04-desktop-amd64.iso) <br> **KUBUNTU**: [Enlace](http://cdimage.ubuntu.com/kubuntu/releases/20.04/release/kubuntu-20.04-desktop-amd64.iso) <br> **XUBUNTU**: [Enlace](https://torrent.ubuntu.com/xubuntu/releases/focal/release/desktop/xubuntu-20.04-desktop-amd64.iso.torrent) |
| Fedora | **30**: [Enlace](http://mirror.uv.es/mirror/fedora/linux/releases/30/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-30-1.2.iso) <br> **31**: [Enlace](https://download.fedoraproject.org/pub/fedora/linux/releases/31/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-31-1.9.iso) <br> **32**: [Enlace](https://download.fedoraproject.org/pub/fedora/linux/releases/32/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-32-1.6.iso) <br> **33**: [Enlace](https://download.fedoraproject.org/pub/fedora/linux/releases/33/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-33-1.2.iso) <br> **34**: [Enlace](https://mirrors.xtom.de/fedora//releases/34/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-34-1.2.iso) <br> **35**: [Enlace](https://download.fedoraproject.org/pub/fedora/linux/releases/35/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-35-1.2.iso) |
| Linux Mint 19 | **CINNAMON**: [Enlace](https://mirror.dogecloud.org/Linux/Mint/stable/19.2/linuxmint-19.2-cinnamon-64bit.iso) |
| KDE Neon | [Enlace](https://files.kde.org/neon/images/user/20191024-1119/neon-user-20191024-1119.iso) |
| Arch Linux | **TORRENT**: [Enlace](https://www.archlinux.org/releng/releases/2019.10.01/torrent/) |
| Manjaro | **GNOME**: [Enlace](https://osdn.net/frs/redir.php?m=dotsrc&f=%2Fstorage%2Fg%2Fm%2Fma%2Fmanjaro%2Fgnome%2F18.1.2%2Fmanjaro-gnome-18.1.2-191028-linux53.iso) <br> **KDE**: [Enlace](https://osdn.net/frs/redir.php?m=dotsrc&f=%2Fstorage%2Fg%2Fm%2Fma%2Fmanjaro%2Fkde%2F18.1.2%2Fmanjaro-kde-18.1.2-191028-linux53.iso) <br> **XFCE**: [Enlace](https://osdn.net/frs/redir.php?m=dotsrc&f=%2Fstorage%2Fg%2Fm%2Fma%2Fmanjaro%2Fxfce%2F18.1.2%2Fmanjaro-xfce-18.1.2-191028-linux53.iso) |

## Software extra instalado

Por defecto se instala el siguiente software:

| **APLICACIÓN** | **TAG** | **VARIABLE** | **GRUPO** | **DESCRIPCIÓN** |
|--|--|--|--|--|
| [1Password](https://support.1password.com/cs/getting-started-linux/) | 1password | install_1password | pass_managers | Instala gestor de contraseñas **1Password** |
| [Act](https://github.com/nektos/act) | act | install_act | | Ejecuta localmente **Github Actions** |
| [Apache Directory Studio](https://directory.apache.org/studio/downloads.html) | apachedirectory | install_apachedirectory | | Cliente de LDAP |
| [Atom](https://atom.io/) | atom | install_atom | editors | Editor de texto |
| [Authy](https://authy.com/) | authy | install_authy | | Aplicación para 2FA |
| [Balena Etcher](https://www.balena.io/etcher/) | etcher | install_etcher | | Aplicación para quemar imágenes iso en usb |
| [Beekeeper Studio](https://www.beekeeperstudio.io/) | beekeeer | install_beekeeper | | Cliente gráfico para BBDD |
| [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner) | bfg | install_bfg | | Herramienta para trabajar con el histórico de git |
| [Bitwarden](https://bitwarden.com/) | bitwarden | install_bitwarden | pass_managers | Gestor de contraseñas |
| [Brave](https://brave-browser.readthedocs.io/en/latest/index.html) | brave | install_brave | browsers | Navegador web |
| [Bucklespring](https://github.com/zevv/bucklespring) | bucklespring | install_bucklespring | | Herramienta para simular el ruido de un teclado mecánico |
| [Buttercup](https://buttercup.pw/) | buttercup | install_buttercup | pass_managers | Gestor de contraseñas |
| [Cherrytree](https://www.giuspen.com/cherrytree/) | cherrytree | install_cherrytree | editors | Editor de textos |
| [Chromium Browser](https://chromium.woolyss.com/download/es/) | chromium | install_chromium| browsers | Navegador web libre basado en Chrome |
| [Consul](https://learn.hashicorp.com/tutorials/consul/install-cli) | consul | install_consul | | Service discovery |
| [CopyQ](https://hluk.github.io/CopyQ/) | copyq | install_copyq | | Gestor de portapapeles |
| [Deluge Torrent](https://deluge-torrent.org/) | deluge | install_deluge | | Cliente de Torrent |
| [Docker](https://docs.docker.com/install/linux/docker-ce/) | docker | install_docker | | Gestión de contenedores Docker |
| [Dropbox](https://www.dropbox.com/) | dropbox | install_dropbox | | Cliente de almacenamiento en la nube |
| [Ether Cloud Service Client](https://platform.bbva.com/en-us/developers/ether-cli/documentation/01-what-is) | ecs | install_ecs | | |
| [Ferdi](https://getferdi.com/) | ferdi | install_ferdi | | Administrador ded clientes de mensajería |
| [Franz](https://meetfranz.com/) | franz | install_franz | | Administrador de clientes de mensajería |
| [FZF](https://github.com/junegunn/fzf) | fzf | install_fzf | | Buscador difuso de archivos |
| [Github CLI](https://github.com/cli/cli) | githubcli | install_githubcli | | Cli de consola para [Github](https://github.com) |
| [Gitkraken](https://www.gitkraken.com/git-client) | gitkraken | install_gitkraken | | Cliente gráfico de git |
| [GO](https://golang.org/doc/install/source) | go | install_go | | Compilador del lenguaje GO |
| [Google Chrome](https://www.google.com/intl/es/chrome/) | chrome | install_chrome | browsers | Navegador web |
| [Google Fonts](https://fonts.google.com/) | google_fonts | install_fonts | | Fuentes tipográficas de Google |
| [Hashicorp stask](https://www.hashicorp.com/) | hashicorp | install_hashicorp | | Stack de aplicaciones de **Hashicorp**: **Vault**, **Terraform**, **Consul** y **Nomad** |
| [Hiri](https://www.hiri.com/) | hiri | install_hiri | | Cliente de correo |
| [Java](https://openjdk.java.net/) | java | install_java | | Lenguaje Java |
| [k8s_tools](https://kubernetes.io/docs/reference/tools/) | k8s_tools | install_k8s_tools | | Herramientas de Kubernetes |
| [KDEnlive](https://kdenlive.org/es/descargar/)| kdenlive | install_kdenlive | | Editor de video para KDE |
| [KeepassXC](https://keepassxc.org/download/) | keepass | install_keepass | pass_managers | Gestor de contraseñas |
| [Kodi](https://kodi.tv/) | kodi | install_kodi | | Media center |
| [Lexnet](https://lexnet.justicia.es) | lexnet | install_lexnet | | Firefox 50.1 + Java para acceder a Lexnet (sólo para abogados) |
| [Mailspring](https://getmailspring.com/) | mailspring | install_mailspring | | Cliente de correo electrónico |
| [MAME](https://www.mamedev.org/) | mame | install_mame | | Emulador de juegos de recreativas |
| [MEGA sync](https://mega.nz/sync) | megasync | install_megasync | mega | Cliente de almacenamiento en la nube de Mega |
| [MEGAcmd](https://mega.nz/cmd) | megacmd | install_megacmd | mega | Cliente de almacenamiento en la nube de Mega para terminal |
| [NoMachine](https://www.nomachine.com/es/) | nomachine | install_nomachine | remotes | Cliente de escritorio remoto |
| [Nomad](https://learn.hashicorp.com/tutorials/nomad/install-cli) | nomad | install_nomad | | Orchestration tool for deploying and managing applications |
| [OBS Studio](https://obsproject.com/es) | obs | install_obs | | Grabación de video y transmissión en vivo |
| [Oh my ZSH!](https://ohmyz.sh/) | ohmyzsh | install_ohmyzsh | | Personalización de ZSH |
| [Pass](https://www.passwordstore.org/) | pass | install_pass | pass_managers | Gestor de contraseñas |
| [Podman](https://podman.io/) | podman | install_podman | | Gestor de contenedores |
| [Postman](https://www.getpostman.com) | postman | install_postman | | Cliente REST API |
| [Prezto](https://github.com/sorin-ionescu/prezto) | prezto | install_prezto | | Personalización de ZSH (fork mejorado de Oh my Zsh) |
| [ProtonVPN](https://protonvpn.com/) | protonvpn | install_protonvpn | | Cliente de VPN |
| [PyCharm Community](https://www.jetbrains.com/pycharm/download/#section=linux) | pycharm | install_pycharm | editors | IDE para Python |
| [Rambox](https://rambox.pro/#home) | rambox | install_rambox | | Gestor de clientes de mensajería |
| [Secrethub](https://secrethub.io) | secrethub | install_secrethub | | Gestor de secretos |
| [Skype](https://www.skype.com/es/) | skype | install_skype | socials | Cliente de mensajería de Skype |
| [Slack](https://slack.com/intl/es-es/) | slack | install_slack | socials | Cliente de mensajería para entornos de trabajo |
| [Spotify](https://www.spotify.com/es/premium/?checkout=false) | spotify | install_spotify | | Cliente de Spotify |
| [Station](https://getstation.com/) | station | install_station | | Administrador de clientes de mensajería |
| [Steam](https://store.steampowered.com/?l=spanish) | steam | install_steam | | Cliente Steam para juegos de PC |
| [Sublime Merge](https://www.sublimemerge.com/) | sublimemerge | install_sublimemerge | sublime | Cliente gráfico de git |
| [Sublime Text](https://www.sublimetext.com/) | sublimetext | install_sublimetext | editors/sublime | Editor de textos |
| [Teamviewer](https://www.teamviewer.com/es/) | teamviewer | install_teamviewer | remotes | Cliente de escritorio remoto |
| [Telegram Desktop](https://telegram.org/) | telegram | install_telegram | socials | Cliente de escritorio de mensajería Telegram |
| [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) | terraform | install_terraform | | Creación de infraestructura |
| [TLP](https://linrunner.de/en/tlp/docs/tlp-linux-advanced-power-management.html) | tlp | install_tlp | | Gestión de batería (sólo para Thinkpad) |
| [Tmux](http://www.sromero.org/wiki/linux/aplicaciones/tmux) | tmux | install_tmux | | Multiplexador de terminal avanzado |
| [Trivy](https://github.com/aquasecurity/trivy) | trivy | install_trivy | | Scanner de vulnerabilidades de contenedores docker |
| [Typora](https://typora.io) | typora | install_typora | | Editor de textos especializado en Markdown |
| [Vault](https://learn.hashicorp.com/tutorials/vault/getting-started-install) | vault | install_vault | | Cliente/Servidor de gestión de secretos |
| [Vim plugins](https://vimawesome.com/) | vimplugins | install_vimplugins | | Instalación de plugins de VIM |
| [Virtualbox](https://www.virtualbox.org/) | virtualbox | install_virtualbox | | Virtualización (incluye Vagrant) |
| [Visual Studio Code](https://code.visualstudio.com/) | vscode | install_vscode | editors | Editor de textos |
| [Visual Studio Codium](https://vscodium.com/) | vscodium | install_vscodium | editors | Editor de textos libre pasado en VS Code |
| [Vivaldi](https://vivaldi.com/es/) | vivaldi | install_vivaldi | browsers | Navegador web |
| [Windscribe](https://windscribe.com/) | windscribe | install_windscribe | | Cliente de VPN |
| [Wireguard](https://www.wireguard.com/) | wireguard | install_wireguard | | Cliente de VPN |
| [WoeUSB](https://github.com/slacka/WoeUSB) | woeusb | install_woeusb | | Herramienta para quemar iso de windows en usb |
| [YakYak](https://github.com/yakyak/yakyak) | yakyak | install_yakyak | | Cliente de mensajería para Hangouts |
| [Zoom](https://zoom.us/es-es/meetings.html) | zoom | install_zoom | | Cliente de videoconferencia |

En caso de que no se quiera instalar alguna de las anteriores aplicaciones, se puede indicar a través de las `extravars` con la correspondiente **variable** a `false`. Por ejemplo, para instalar todo el software extra excepto *Spotify* y *Oh my zsh!*:

```bash
ansible-playbook install.yml -e "install_spotify=false install_ohmyzsh=false" --ask-vault-pass
```

En caso contrario, si lo único que se quiere hacer es instalar alguna de las aplicaciones, hay que usar el **tag** correspondiente, que coincide con las variables anteriores. Por ejemplo, para instalar *Visual Studio Code*:

```bash
ansible-playbook install.yml -t "vscode,dropbox,spotify" --ask-vault-pass
```

En el siguiente punto, se explica cómo generar una configuración específica de usuario con el software que se desea instalar

## ¿Cómo se usa?

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
ansible-playbook install.yml --ask-vault-pass
```

Un usuario puede personalizar las aplicaciones que desea instalar creando el fichero `ansible/roles/extra_software/vars/${USER}.yml`, se pueden usar los valores por defecto para generarlo y luego personalizarlo a su gusto:

```bash
grep "install_" ansible/roles/extra_software/defaults/main.yml > ansible/roles/extra_software/vars/${USER}.yml
```

Para instalar una aplicación que en este fichero se haya definido a `false`, es posible modificar el valor mediante `--extra-vars`:

```bash
ansible-playbook install.yml -t code -e install_vscode=true --ask-vault-pass
```

Igualmente, se pueden usar los tags específicos que cada usuario haya puesto en su role `post_install/$USER`

```bash
ansible-playbook install-yml -t env --ask-vault-pass
```

### Post instalación

```bash
ansible-playbook post_install.yml --ask-vault-pass
```

[Aquí se puede consultar la documentación de la post instalación](roles/post_install/README.md)

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

- Fichero

```bash
sudo touch /var/tmp/.update
```

## Otros playbooks

[Documentado aquí](playbooks/README.md)

## Ejecución de comandos ansible ad-hoc

```bash
ansible localhost -m shell -a "df -h"
```

## Uso de Vagrant

:information_source: El __usuario/contraseña__ de las máquinas virtuales es `vagrant/vagrant`

Para probar el código, se puede levantar una máquina virtual usando [Vagrant](https://www.vagrantup.com/) y [Virtualbox](https://www.virtualbox.org/). Para ello, será necesario instalar *Virtualbox* usando el tag `--virtualbox`:

```bash
ansible-playbook install.yml  -t virtualbox --ask-vault-pass
```

A continuación, dentro del directorio del repo, hay que ejecutar el siguiente comando para levntar la máquina virtual:

```bash
vagrant up [mint|kubuntu|ubuntu|xubuntu|fedora30|fedora31|fedora32|arch|manjaro|debian]
```

Para entrar a la máquina creada:

```bash
vagrant ssh [mint|kubuntu|ubuntu|xubuntu|fedora30|fedora31|fedora32|arch|manjaro|debian]
```

Una vez dentro de ella, hay que instalar `git` y `ansible`, clonar el repositorio y lanzar los playbooks correspondientes como en una máquina física.

```bash
vagrant ssh debian
sudo apt install git ansible
git clone https://gitlab.com/ohermosa/my_workstation.git
cd my_workstation/ansible
ansible-playbook install.yml --ask-vault-pass
```

Una vez terminadas las pruebas, para destruir las máquinas:

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
