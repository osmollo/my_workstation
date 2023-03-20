# Ansible

- [Ansible](#ansible)
  - [Distribuciones soportadas](#distribuciones-soportadas)
  - [Software extra instalado](#software-extra-instalado)
  - [¿Cómo se usa?](#cómo-se-usa)
    - [Post instalación](#post-instalación)
    - [Deshabilitar actualizaciones](#deshabilitar-actualizaciones)
  - [Otros playbooks](#otros-playbooks)
  - [Ejecución de comandos ansible ad-hoc](#ejecución-de-comandos-ansible-ad-hoc)
  - [Actualización de CHANGELOG.md](#actualización-de-changelogmd)
  - [Emoji Cheat Sheet](#emoji-cheat-sheet)
  - [Invítame a un café](#invítame-a-un-café)

## Distribuciones soportadas

| **DISTRIBUCIÓN** | **LINKS DE DESCARGA** |
|------------------|--------------|
| Ubuntu | [Enlace](https://ubuntu.com/download/desktop) |
| Fedora | [Enlace](https://getfedora.org/es/workstation/download/) |
| Debian | [Enlace](https://www.debian.org/distrib/netinst#smallcd) |
| Deepin | [Enlace](https://www.deepin.org/en/download/) |
| Linux Mint | [Enlace](https://www.linuxmint.com/download.php) |
| Pop!_OS | [Enlace](https://pop.system76.com/)
| KDE Neon | [Enlace](https://neon.kde.org/download) |
| Arch Linux | [Enlace](https://www.archlinux.org/releng/releases) |
| Manjaro | [Enlace](https://manjaro.org/download/) |

## Software extra instalado

Por defecto se instala el siguiente software:

| **APLICACIÓN** | **TAG** | **VARIABLE** | **GRUPO** | **DESCRIPCIÓN** |
|--|--|--|--|--|
| [1Password](https://support.1password.com/cs/getting-started-linux/) | 1password | install_1password | pass_managers | Instala gestor de contraseñas **1Password** |
| [Apache Directory Studio](https://directory.apache.org/studio/downloads.html) | apachedirectory | install_apachedirectory | dev | Cliente de LDAP |
| [Balena Etcher](https://www.balena.io/etcher/) | etcher | install_etcher | tools | Aplicación para quemar imágenes iso en usb |
| [Bat](https://github.com/sharkdp/bat) | bat | install_bat | tools | cat vitaminado |
| [Beekeeper Studio](https://www.beekeeperstudio.io/) | beekeeer | install_beekeeper | dev | Cliente gráfico para BBDD |
| [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner) | bfg | install_bfg | git | Herramienta para trabajar con el histórico de git |
| [Bitwarden](https://bitwarden.com/) | bitwarden | install_bitwarden | pass_managers | Gestor de contraseñas |
| [Brave](https://brave-browser.readthedocs.io/en/latest/index.html) | brave | install_brave | browsers | Navegador web |
| [Broot](https://github.com/Canop/broot) | broot | install_broot | tools | Terminal file browser |
| [Bottom](https://github.com/ClementTsang/bottom) | bottom | install_bottom | tools | top vitaminado |
| [Bucklespring](https://github.com/zevv/bucklespring) | bucklespring | install_bucklespring | tools | Herramienta para simular el ruido de un teclado mecánico |
| [Buttercup](https://buttercup.pw/) | buttercup | install_buttercup | pass_managers | Gestor de contraseñas |
| [Cherrytree](https://www.giuspen.com/cherrytree/) | cherrytree | install_cherrytree | editors | Editor de textos |
| [Chromium Browser](https://chromium.woolyss.com/download/es/) | chromium | install_chromium| browsers | Navegador web libre basado en Chrome |
| [Consul](https://learn.hashicorp.com/tutorials/consul/install-cli) | consul | install_consul | tools | Service discovery |
| [CopyQ](https://hluk.github.io/CopyQ/) | copyq | install_copyq | | Gestor de portapapeles |
| [curlie](https://github.com/rs/curlie) | curlie | install_curlie | tools | Curl vitaminado |
| [Deluge Torrent](https://deluge-torrent.org/) | deluge | install_deluge | desktop| Cliente de Torrent |
| [Docker](https://docs.docker.com/install/linux/docker-ce/) | docker | install_docker | containers | Gestión de contenedores Docker |
| [Draw.io](https://github.com/jgraph/drawio-desktop) | drawio | install_drawio | desktop | Editor de diagramas |
| [Dropbox](https://www.dropbox.com/) | dropbox | install_dropbox | storage | Cliente de almacenamiento en la nube |
| [Duf](https://github.com/muesli/duf) | duf | install_duf | tools | du vitaminado |
| [Element](https://element.io/) | element | install_element | social | cliente de mensajería para [matrix.org](https://matrix.org) |
| [ERDtree](https://github.com/solidiquis/erdtree) | erdtree | install_erdtree | tools | `tree` vitaminado | 
| [Ether Cloud Service Client](https://platform.bbva.com/en-us/developers/ether-cli/documentation/01-what-is) | ecs | install_ecs | tools | |
| [Franz](https://meetfranz.com/) | franz | install_franz | social | Administrador de clientes de mensajería |
| [FZF](https://github.com/junegunn/fzf) | fzf | install_fzf | tools | Buscador difuso de archivos |
| [Github CLI](https://github.com/cli/cli) | githubcli | install_githubcli | git | Cli de consola para [Github](https://github.com) |
| [Gitkraken](https://www.gitkraken.com/git-client) | gitkraken | install_gitkraken | git | Cliente gráfico de git |
| [GO](https://golang.org/doc/install/source) | go | install_go | dev | Compilador del lenguaje GO |
| [Google Chrome](https://www.google.com/intl/es/chrome/) | chrome | install_chrome | browsers | Navegador web |
| [Google Fonts](https://fonts.google.com/) | google_fonts | install_fonts | | Fuentes tipográficas de Google |
| [GOpass](https://github.com/gopasspw/gopass) | gopass | install_gopass | pass_managers | Gestor de contraseñas |
| [Gping](https://github.com/orf/gping) | gping | install_gping | tools | ping vitaminado |
| [Hashicorp stask](https://www.hashicorp.com/) | hashicorp | install_hashicorp | tools | Stack de aplicaciones de **Hashicorp**: **Vault**, **Terraform**, **Consul** y **Nomad** |
| [Hiri](https://www.hiri.com/) | hiri | install_hiri | mail | Cliente de correo |
| [Java](https://openjdk.java.net/) | java | install_java | dev | Lenguaje Java |
| [k8s_tools](https://kubernetes.io/docs/reference/tools/) | k8s_tools | install_k8s_tools | k8s | Herramientas de Kubernetes |
| [KDEnlive](https://kdenlive.org/es/descargar/)| kdenlive | install_kdenlive | desktop | Editor de video para KDE |
| [KeepassXC](https://keepassxc.org/download/) | keepass | install_keepass | pass_managers | Gestor de contraseñas |
| [Kodi](https://kodi.tv/) | kodi | install_kodi | media | Media center |
| [Lexnet](https://lexnet.justicia.es) | lexnet | install_lexnet | browsers | Firefox 50.1 + Java para acceder a Lexnet (sólo para abogados) |
| [Librewolf](https://librewolf.net/) | librewolf | install_librewolf | browsers | Navegador web Librewolf (fork de Firefox) |
| [LSD](https://github.com/Peltoche/lsd) | lsd | install_lsd | tools | binario para listar directorios |
| [Mailspring](https://getmailspring.com/) | mailspring | install_mailspring | mail | Cliente de correo electrónico |
| [MAME](https://www.mamedev.org/) | mame | install_mame | games | Emulador de juegos de recreativas |
| [MarkText](https://github.com/marktext/marktext) | marktext | install_marktext | editors | Editor de Markdown |
| [MEGA sync](https://mega.nz/sync) | megasync | install_megasync | storage | Cliente de almacenamiento en la nube de Mega |
| [MEGAcmd](https://mega.nz/cmd) | megacmd | install_megacmd | storage | Cliente de almacenamiento en la nube de Mega para terminal |
| [NeoVim](https://neovim.io/) | neovim | install_neovim | editors | Editor de texto |
| [NoMachine](https://www.nomachine.com/es/) | nomachine | install_nomachine | remotes | Cliente de escritorio remoto |
| [Nomad](https://learn.hashicorp.com/tutorials/nomad/install-cli) | nomad | install_nomad | tools | Orchestration tool for deploying and managing applications |
| [OBS Studio](https://obsproject.com/es) | obs | install_obs | media | Grabación de video y transmissión en vivo |
| [Oh my BASH!](https://ohmybash.nntoan.com/) | ohmybash | install_ohmybash | shell | Personalización de BASH |
| [Oh my ZSH!](https://ohmyz.sh/) | ohmyzsh | install_ohmyzsh | shell | Personalización de ZSH |
| [Podman](https://podman.io/) | podman | install_podman | containers | Gestor de contenedores |
| [Postman](https://www.getpostman.com) | postman | install_postman | dev | Cliente REST API |
| [Prezto](https://github.com/sorin-ionescu/prezto) | prezto | install_prezto | shell | Personalización de ZSH (fork mejorado de Oh my Zsh) |
| [PROCS](https://github.com/dalance/procs/releases/latest) | procs | install_procs | tools | Reemplazo de `ps` |
| [ProtonVPN](https://protonvpn.com/) | protonvpn | install_protonvpn | vpn | Cliente de VPN |
| [PyCharm Community](https://www.jetbrains.com/pycharm/download/#section=linux) | pycharm | install_pycharm | editors | IDE para Python |
| [Rambox](https://rambox.pro/#home) | rambox | install_rambox | social | Gestor de clientes de mensajería |
| [Rclone](https://rclone.org/) | rclone | install_rclone | storage | Tool de nubes de almacenamiento |
| [ripgrep](https://github.com/BurntSushi/ripgrep) | ripgrep | install_ripgrep | tools | grep vitaminado |
| [Skype](https://www.skype.com/es/) | skype | install_skype | social | Cliente de mensajería de Skype |
| [Slack](https://slack.com/intl/es-es/) | slack | install_slack | social | Cliente de mensajería para entornos de trabajo |
| [Singlebox](https://webcatalog.io/singlebox/) | singlebox | install_singlebox | social | Administrador de clientes de mensajería |
| [Spotify](https://www.spotify.com/es/premium/?checkout=false) | spotify | install_spotify | media | Cliente de Spotify |
| [Steam](https://store.steampowered.com/?l=spanish) | steam | install_steam | games | Cliente Steam para juegos de PC |
| [Sublime Merge](https://www.sublimemerge.com/) | sublimemerge | install_sublimemerge | git | Cliente gráfico de git |
| [Sublime Text](https://www.sublimetext.com/) | sublimetext | install_sublimetext | editors | Editor de textos |
| [Teamviewer](https://www.teamviewer.com/es/) | teamviewer | install_teamviewer | remotes | Cliente de escritorio remoto |
| [Telegram Desktop](https://telegram.org/) | telegram | install_telegram | social | Cliente de escritorio de mensajería Telegram |
| [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) | terraform | install_terraform | tools | Creación de infraestructura |
| [TLP](https://linrunner.de/en/tlp/docs/tlp-linux-advanced-power-management.html) | tlp | install_tlp | tools | Gestión de batería (sólo para Thinkpad) |
| [Tmux](http://www.sromero.org/wiki/linux/aplicaciones/tmux) | tmux | install_tmux | tools | Multiplexador de terminal avanzado |
| [Trivy](https://github.com/aquasecurity/trivy) | trivy | install_trivy | containers | Scanner de vulnerabilidades de contenedores docker |
| [Vault](https://learn.hashicorp.com/tutorials/vault/getting-started-install) | vault | install_vault | tools | Cliente/Servidor de gestión de secretos |
| [Vim plugins](https://vimawesome.com/) | vimplugins | install_vimplugins | editors | Instalación de plugins de VIM |
| [Virtualbox](https://www.virtualbox.org/) | virtualbox | install_virtualbox | virtualization | Virtualización (incluye Vagrant) |
| [Visual Studio Code](https://code.visualstudio.com/) | vscode | install_vscode | editors | Editor de textos |
| [Visual Studio Codium](https://vscodium.com/) | vscodium | install_vscodium | editors | Editor de textos libre pasado en VS Code |
| [Vivaldi](https://vivaldi.com/es/) | vivaldi | install_vivaldi | browsers | Navegador web |
| [Windscribe](https://windscribe.com/) | windscribe | install_windscribe | vpn | Cliente de VPN |
| [Wireguard](https://www.wireguard.com/) | wireguard | install_wireguard | vpn | Cliente de VPN |
| [WoeUSB](https://github.com/slacka/WoeUSB) | woeusb | install_woeusb | tools | Herramienta para quemar iso de windows en usb |
| [YakYak](https://github.com/yakyak/yakyak) | yakyak | install_yakyak | social | Cliente de mensajería para Hangouts |
| [yq](https://github.com/mikefarah/yq) | yq | install_yq | tools | Parseador json, yaml y xml |
| [Zoom](https://zoom.us/es-es/meetings.html) | zoom | install_zoom | social | Cliente de videoconferencia |

En caso de que no se quiera instalar alguna de las anteriores aplicaciones, se puede indicar a través de las `extravars` con la correspondiente **variable** a `false`. Por ejemplo, para instalar todo el software extra excepto *Spotify* y *Oh my zsh!*:

```shell
ansible-playbook install.yml -e "install_spotify=false install_ohmyzsh=false"
```

En caso contrario, si lo único que se quiere hacer es instalar alguna de las aplicaciones, hay que usar el **tag** correspondiente, que coincide con las variables anteriores. Por ejemplo, para instalar *Visual Studio Code*:

```shell
ansible-playbook install.yml -t "vscode,dropbox,spotify"
```

En el siguiente punto, se explica cómo generar una configuración específica de usuario con el software que se desea instalar

## ¿Cómo se usa?

- Las tareas de este repositorio se ejecutan en local, por lo que para poder ejecutar los playbooks es necesario tener instalado `git` y `ansible`:

```shell
# Para Fedora
sudo dnf install git ansible

# Para Ubuntu
sudo apt install git ansible

# Para Arch
sudo pacman -S git ansible
```

A continuación habrá que clonar este repositorio (da igual el directorio de destino):

```shell
git clone https://github.com/osmollo/my_workstation.git /tmp/repo
cd /tmp/repo/ansible
ansible-playbook install.yml
```

No todas las aplicaciones se instalan por defecto, este comportamiento se encuentra definido en el fichero `./roles/extra_software/defaults/main.yml` donde hay una serie de variables `install_` que indican si la correspondiente aplicación se instala o no. Para modificar este comportamiento, puede editarse dicho fichero o cambiar el valor de la variable por `extravars`:

```shell
ansible-playbook install.yml -t chromium -e install_chromium=true
```

### Post instalación

Las variables necesarias para la ejecución de este role se encuentran en `./roles/post_install/defaults/main.yml.gpg`

```shell
ansible-playbook playbooks/prepare_post.yml

ansible-playbook post_install.yml
```

[Aquí se puede consultar la documentación de la post instalación](roles/post_install/README.md)

### Deshabilitar actualizaciones

Una de las primeras tareas que se ejecutan es la actualización de los paquetes del sistema. Esta tarea no se lanzará si hace menos de una semana que se ha ejecutado pero también es posible deshabilitarla de las siguientes formas:

- Variable de entorno

Hay que exportar la variable `REPO_DISABLE_UPDATES` con valor *1*. Cualquier otro valor se considerará *false* y se actualizarán los paquetes

```shell
export REPO_DISABLE_UPDATES=1
```

- Extravars

```shell
ansible-playbook install.yml -e disable_updates=true
```

- Fichero

```shell
sudo touch /var/tmp/.update
```

## Otros playbooks

[Documentado aquí](playbooks/README.md)

## Ejecución de comandos ansible ad-hoc

```shell
ansible localhost -m shell -a "df -h"
```

## Actualización de CHANGELOG.md

Para poder actualizar el [CHANGELOG.md](CHANGELOG.md) con los cambios que se han realizado entre 2 tags hay que ejecutar el siguiente comando:

```shell
git log --pretty=oneline <tag_antiguo> <tag_nuevo>
```

Y entre el último tag y el último commit:

```shell
git log --pretty=oneline HEAD...tag
```

## Emoji Cheat Sheet

[Aquí](https://www.webfx.com/tools/emoji-cheat-sheet/) se puede encontrar la lista de emojis disponibles para **markdown**

## Invítame a un café

Si te ha sido de ayuda este repositorio, pero sobretodo si te apetece, puedes invitarme a un café

[![buy me a coffee](https://camo.githubusercontent.com/c3f856bacd5b09669157ed4774f80fb9d8622dd45ce8fdf2990d3552db99bd27/68747470733a2f2f7777772e6275796d6561636f666665652e636f6d2f6173736574732f696d672f637573746f6d5f696d616765732f6f72616e67655f696d672e706e67)](https://www.buymeacoffee.com/osmollo)
