# CHANGELOG

- [CHANGELOG](#changelog)
  - [8.3](#83)
  - [8.2](#82)
  - [8.1.1](#811)
  - [8.1](#81)
  - [8.0.2](#802)
  - [8.0.1](#801)
  - [8.0](#80)
  - [VERSIONES ANTERIORES](#versiones-anteriores)
    - [Versión 7](#versión-7)
    - [Versión 6](#versión-6)
    - [Versión 5](#versión-5)
    - [Versión 4](#versión-4)
    - [Versión 3](#versión-3)
    - [Versión 2](#versión-2)
    - [Versión 1](#versión-1)

## 8.3

- Ya no se soporta la instalación de **Ferdi** ni **Station** por abandono de dichos proyectos
- Simplificación en la lectura de secretos de [1Password](https://1password.eu/) sin usar módulos de **Ansible**
- Instalación de [yq](https://github.com/mikefarah/yq) para parsear __json__, __yaml__ y __xml__ de forma similar a como funciona **jq**
- Instalación de [Element](https://element.io/) como cliente de mensajería para [matrix.org](https://matrix.org)
- Instalación de [GOpass](https://github.com/gopasspw/gopass)
- Corrección de errores:
  - Cambio del directorio `$GOPATH` de `~/go` a `~/.local/share/go`

## 8.2

- Mejora en playbook `playbooks/check_op.yml`: a parte de la variable de entorno __OP_SESSION_*__, se comprueba que el comando `op` funciona correctamente
- Instalación de [rclone](https://rclone.org/)
- Nuevo módulo `onepassword` de **Ansible** para leer secretos de [1Password](https://1password.eu/)
- Eliminación de la configuración de **Github Actions** para ejecutar __ansible-lint__
- Eliminación de la configuración de OpenVPN de Trabajo
- Instalación de [oh-my-bash!](https://github.com/ohmybash/oh-my-bash)
- Instalación de `kubectl` por defecto
- Instalación de [tldr](https://tldr.sh/)
- Corrección de errores:
  - Fix [url mojave_dynamic.zip](https://files.osmollo.ovh/wallpapers/mojave_dynamic.zip) para el fondo de escritorio dinámico
  - Fix instalación paquetes **GNOME** en **Arch**
  - Fix repositorio git al instalar **oh-my-zsh** y **oh-my-bash** desde `post_install`
  - Fix alias `actualiza` en **Arch** para que también actualice paquetes instalados con **yay**
  - Fix alias `yay` en **Arch**
  - Importación de la configuración de **Tilix**
  - Fix generando `~/.gitconfig`
  - Instalación de paquetes/dependencias en **Arch**
  - Configurar `.ssh/config` para usar **1Password** como gestor de llaves SSH
  - Fix creación fichero `~/.vault_pass`
  - Limpieza de repositorios git para clonar

## 8.1.1

- Comprobación en `post_install.yml` si la variable `OP_SESSION_*` está definida como variable de entorno en el sistema

## 8.1

- Instegración con [1Password](https://1password.com/sign-up/eu/)
  - Configuración del agent-ssh para que use las llaves ssh de **1Password**
  - Instalación de la última versión del CLI2
  - Bash alias para obtener algunos secretos de 1Password
- Soporte para [Fedora 37](https://getfedora.org/es/workstation/) y fin de soporte a versiones anteriores
  - Uso de `dnf` en lugar de `yum` para las tareas de instalación de paquetes en **Fedora**
  - Mejora en la velocidad de `dnf` en **Fedora**
  - Se aplica workaround para evitar el problema de dependencias de **Dropbox** en esta versión de **Fedora**: se instala como flatpak
  - Se deshabilita el chequeo de GPG en el plaquete de instalación de **Etcher**
- Instalación de [kubecolor](https://github.com/hidetatz/kubecolor)
- Eliminación de **ACT**
- Instalación por defecto de **Sublime Text** y **Sublime Merge**
- Modificación de la ruta del repositorio `my_workstation` en el directorio actual, de __HTTPS__ a __SSH__
- [BuyMeACoffee](https://www.buymeacoffee.com/osmollo) en el [README](README.md)
- Corrección de errores:
  - Fixes para **Linux Mint**
  - Fixes al obtener la última version de varias apps
  - Eliminación del role `tools/telegram`
  - Eliminación del fichero `roles/extra_software/vars/secrets.yml`
  - Eliminadas las referencias a llaves SSH locales
  - Fixes versiones python
  - Fixes variables de entorno

## 8.0.2

- Corrección de errores:
  - La versión de [Vivaldi](https://vivaldi.com/es/) estaba hardcodeada, ahora se instala mediante repositorio en **Ubuntu** y **Fedora**
  - Corregido el orden en la instalación de **Typora**
  - Eliminación de la plantilla `docker-ce.repo.j2`
  - La versión de **Virtualbox Extension Pack** ya no está hardcodeada sino que se lee de la url [https://download.virtualbox.org/virtualbox/LATEST.TXT](https://download.virtualbox.org/virtualbox/LATEST.TXT)

## 8.0.1

- Corrección de errores:
  - Cambio del directorio de entornos virtuales de python
  - Playbook `prepare_post.yml` hace pausa antes de desencriptar `main.yml.gpg` para que se pueda copiar el passphrase
  - Eliminación de repositorios git
  - Instalación por defecto de **Trivy**

## 8.0

- Integración completa y gestión de secretos con [Bitwarden](https://bitwarden.com/)
  - Ya no se usa `ansible-vault` para el cifrado de secretos
- **Secrethub** ya no se encuentra disponible para su instalación debido a su [fin de vida](https://secrethub.io/)
- Cambios en repositorios git
- Configuración de [Ubuntu PRO](https://discourse.ubuntu.com/t/ubuntu-pro-beta-tutorial/31018) en el role `post_install`
- En el role `post_install` ya no se configura `pass` ni `oracle_cloud`
- Corrección de errores:
  - `~/.env` renombrado como `~/.environment`
  - Limpieza entadas `insecure_registries` de `/etc/docker/daemon.json`
  - Refactor de la configuración de **Docker** en el role `post_install`

## VERSIONES ANTERIORES

### [Versión 7](changelog/v7.md)
### [Versión 6](changelog/v6.md)
### [Versión 5](changelog/v5.md)
### [Versión 4](changelog/v4.md)
### [Versión 3](changelog/v3.md)
### [Versión 2](changelog/v2.md)
### [Versión 1](changelog/v1.md)
