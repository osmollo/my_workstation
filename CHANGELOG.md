# CHANGELOG

- [CHANGELOG](#changelog)
  - [9.6](#96)
  - [9.5](#95)
  - [9.4](#94)
  - [9.3.1](#931)
  - [9.3](#93)
  - [9.2](#92)
  - [9.1](#91)
  - [9.0](#90)
  - [VERSIONES ANTERIORES](#versiones-anteriores)
    - [Versión 8](#versión-8)
    - [Versión 7](#versión-7)
    - [Versión 6](#versión-6)
    - [Versión 5](#versión-5)
    - [Versión 4](#versión-4)
    - [Versión 3](#versión-3)
    - [Versión 2](#versión-2)
    - [Versión 1](#versión-1)

## 9.6

- Instalación de [Neovim](https://neovim.io/) en **Ubuntu** mediante repositorio ppa
- `bash_aliases` es renombrado a `shell_aliases`
- Soporte para **Linux Mint LMDE** basada en **Debian**
- Post_install:
  - Nuevo alias `logs_graphql`
  - Nuevos alias para conexiones ssh a grupos de servidores

## 9.5

- Instalación de [kube capacity](https://github.com/robscott/kube-capacity)
- Inicialización de **Neovim** después de su configuración
- Instalación de [Snyk CLI](https://snyk.io/)
- Instalación de [Rancher CLI](https://ranchermanager.docs.rancher.com/reference-guides/cli-with-rancher/rancher-cli)
- Downgrade de [GlobalProtect Openconnect](https://github.com/yuezk/GlobalProtect-openconnect/tree/1.x) a la versión 1.4.X por breaking changes en la actualización a la v2.X
- Corrección de errores:
  - Instalación de **oh-my-zsh** cuando la distro no sea **Arch**
  - Instalación definitiva de **Docker** y **MegaCMD** en **Fedora**
  - Instalación de **Snyk** de site oficial en vez de [Github](https://github.com/snyk/cli/releases)
- Post_install:
  - Nuevas entradas SSH
  - Configuración de **Helix Editor**
  - Nuevo alias `helix` para `hx`
  - Renovación tokens git
  - Cambio en la configuración de $SHELL
  - Nuevos repositorios git
  - Soporte para repositorios con el mismo nombre pero de distintos proyectos

## 9.4

- Instalación de [Poetry](https://python-poetry.org/) para **Python**
- Instalación de [Helix editor](https://helix-editor.com/)
- Nuevo playbook `playbooks/debian_sudo.yml` para configurar __sudo__
- Soporte para **Debian 13 (Trixie)**
- Instalación de **SoapUI** para **Debian** y **Ubuntu**
- **Debian** deja de usar **snap** en favor de **flatpak**
- Instalación de **kubectl** descargando el binario oficial en lugar de usar repositorios
- Instalación de [Kor](https://github.com/yonahd/kor) dentro de las __tools de k8s__
- Corrección de errores:
  - Fix configuración __bash__
  - Fix en la instalación de **lsd** porque ha cambiado el nombre del repositorio
  - Instalación de **DBeaver** y **Global Protect** en **Debian**
  - Instalación de **Spotify** en **Debian** como snap
  - Fixes para instalación en **Arch**
  - Instalación de versión **beta** de `1Password` en **Arch**
  - Fix creación directorio `/etc/docker` para **Docker**
  - Ya no se instala **Trivy** por defecto
  - `get_bitbucket_repositories` ya no devuelve sólo 25 repositorios
  - Configuración de usuario de **Astronvim** se pasa a `post_install`
  - Reintentos al descargar el paquete de **spotify-tui**
- Post_install:
  - Nuevas entradas configuración SSH
  - Comprueba que se haya desencriptado 'roles/post_install/defaults/main.yml.gpg' antes de ejecutar la post instalación
  - Fix en tags `git_work` y `git_legacy`
  - Borrado del directorio por defecto de **Syncthing**

## 9.3.1

- Corrección de errores:
  - Fix del tag `git_work`
  - Fix en la obtención de repositorios

## 9.3

- Instalación de [Prospect Mail](https://github.com/julian-alarcon/prospect-mail)
- Instalación de [Trilium Notes](https://github.com/zadam/trilium)
- Sin soporte para **Hiri** por estar sin mantenimiento desde 2018
- Nuevo playbook `user_config.yml` para las siguientes configuraciones de mi usuario:
  - alias de bash/zsh
  - configuración de ssh
  - clonación de repositorios git
- Nuevo módulo [get_bitbucket_repos](library/get_bitbucket_repos.py)
- Corrección de errores:
  - Creación de remote por defecto
  - Alias `decrypt_my_defaults` lee passphrase de 1Password
  - Uso de `--force` al pushear repositorios
- Post_install:
  - Nuevas configuraciones SSH
  - Actualiza los remotos de git después de crearlos
  - Nuevo grupo de repositorios en el clonado: `git.legacy`
  - Nuevos tags `git_work`, `git_home` y `git_legacy`
  - El tag `update` ya no ejecuta toda la instalación de **1Password** para actualizarla sino solo el _CLI_

## 9.2

- Instalación de [Thincast](https://thincast.com/en/)
- Instalación de [Pulsar](https://pulsar-edit.dev/)
- Instalación de [Gitnuro](https://gitnuro.jetpackduba.com/)
- Instalación de [Syncthing](https://syncthing.net)
- Corrección de errores:
  - **Sublime merge** ya no se instala por defecto
  - Instalación de **Spotify** en **Fedora** con flatpak
  - Instalación de extensiones en **Pulsar**
  - Instalación de librerías de **Python** con el argumento `--user`
- Post_install:
  - Nuevos repositorios git
  - Modificación del alias `actualiza` para que actualice también las apps de *Snap* (**Ubuntu**) o de *Flatpak* (**Fedora**)
  - Simplificación del clonado de repositorios git
  - Docker login con 2FA
  - Configuración de **Syncthing**
  - Nuevas entradas ssh_config

## 9.1

- Soportado [Fedora 38](https://docs.fedoraproject.org/en-US/releases/f38/)
- Soportado [Ubuntu 23.04](https://ubuntu.com/download/desktop)
- Instalación del plugin **compose** para docker, en lugar de `docker-compose`
- Actualizadas las versiones de algunos github actions
- Instalación de [SoapUI](https://www.soapui.org/)
- Subido a 20 el valor `max_parallel_downloads` en la configuración de __DNF__ para **Fedora**
- Instalación de [bat-extras](https://github.com/eth-p/bat-extras)
- Post_install:
  - Entradas en `~/.ssh/config`
  - Simplificación de las entradas de ssh
  - Nuevos repositorios git
  - Restauración de la configuración de **DBeaver**
  - Login en [Mega](https://mega.io/es/) con 2FA activado
  - Nuevo login en registry de docker
- Corrección de errores:
  - Instalación de **Postman** y **SoapUI** por defecto
  - No existe `docker-scan-plugin` para fedora

## 9.0

- Instalación de [AstroNvim](https://github.com/AstroNvim/AstroNvim) con **Neovim**
- Definición de la variable `GNOME_VERSION` en el playbook `load_distro_vars.yml`
- Instalación de [erdtree](https://github.com/solidiquis/erdtree) como reemplazo de `tree`
- Instalación de [procs](https://github.com/dalance/procs/releases/latest) como reemplazo de `ps`
- Instalación de [starship](https://starship.rs/es-ES/) para la gestión del prompt
- Instalación de [zoxide](https://github.com/ajeetdsouza/zoxide) como reemplazo de `cd`
- Instalación de [Microsoft Edge](https://www.microsoft.com/en-us/edge/download?form=MA13FW&ch)
- Nuevo role `tools/create_alias` para la creación de alias en `~/.bash_aliases`
- Eliminación de todas las configuraciones deprecadas de trabajo
- Instalación de [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software)
- Instalación de [GlobalProtect](https://github.com/yuezk/GlobalProtect-openconnect)
- Instalación de [DBeaver](https://dbeaver.io/)
- Instalación de **remmina** en el role `common` para conexión a escritorios remotos
- Corrección de errores:
  - Instalación de [Lens](https://docs.k8slens.dev/getting-started/install-lens/)
  - Varios fixes con `TODO` para revisar en el futuro
  - Instalación de `python-setuptools` en **Arch**
  - Repositorio configuración de usuario de **Astronvim** usa __https__ en vez de __ssh__
- Post_install:
  - Eliminación de la variable de entorno `HISTFILE` del fichero `~/.environment`
  - Limpieza repositorios personales
  - Creación del fichero `.repo` en la instalación de **Bottom**
  - Creación del fichero `.repo` en la instalación de **gping**
  - URLs del changelog corregidas
  - Optimización del clonado y configuración de repositorios
  - Configuración de llave SSH para la firma de commits en repositorios git en según sean repositorios personales o de trabajo
  - Ordenación de los tokens de git
  - Clonado `oh-my-zsh` y `oh-my-bash`
  - Nuevas entradas en `~/.ssh/config`
  - Cambio en el orden del playbook `prepare_post.yml` para desencriptar nada más importar la llave privada

## VERSIONES ANTERIORES

### [Versión 8](changelog/v8.md)
### [Versión 7](changelog/v7.md)
### [Versión 6](changelog/v6.md)
### [Versión 5](changelog/v5.md)
### [Versión 4](changelog/v4.md)
### [Versión 3](changelog/v3.md)
### [Versión 2](changelog/v2.md)
### [Versión 1](changelog/v1.md)
