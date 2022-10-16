# CHANGELOG

## 7.2

- Instalación de **Zoom** usando __snap__ en **Ubuntu** y __flatpak__ en **Fedora**
- Instalación de [MarkText](https://github.com/marktext/marktext)
- Nuevos repositorios git para clonar
- Se deja de usar **1Password** en favor de **Bitwarden** en el `prepare_post.sh`
- Instalación de [Pano](https://github.com/oae/gnome-shell-pano) como gestor de portapapeles en **Gnome**
- Mejoras en la configuración de **Manjaro**
- En la instalación de **VSCode** y **VSCodium** en el role `extra_software` ya no se instalan extensiones
- Eliminación de los tags `post_*` del playbook `post_install.yml`
- Framework de configuración de **ZSH** por defecto pasa a ser [oh my zsh!](https://github.com/ohmyzsh/ohmyzsh)
- Corrección de errores
  - Entradas de ssh_config
  - Instalación de la última versión de **Kind** (la versión estaba hardcodeada)
  - Instalación de `vim plugins` si no se instala **Neovim**
  - Fix configuración plugin de **Neovim**
  - Fix post configuración de **librewolf**
  - Fix en instalación de paquetes de entornos de escritorio
  - Fix en instalación de **VSCode**
  - Fix en instalación de **Teamviewer**
  - Fix en instalación de **Gping**
  - Creación de `~/.zshrc` al instalar **Prezto** en el role `extra_software`
  - Configuración de las llaves gpg de los repositorios en ficheros separados de `trusted.gpg`
  - Fixes para **Debian**:
    - Actualización de paquetes de Python
    - Fix instalación **Docker**
    - Fixes instalación **Dropbox**
    - Fixes instalación **MegaCMD**
    - Instalación de **Spotify** con paquete deb en vez de snap
  - Fixes para **Manjaro**:
    - Ya no es necesario configurar el overlay en **Docker**
    - Priorización en la instalación de **Bitwarde** en el role `extra_software`
    - No se ejecuta `update-alternatives` para el binario de **Neovim**
    - Alias de **yay**
    - Fix instalación **megacmd**

## 7.1.1

- Corrección de errores

## 7.1

- Soporte para la distribución [Pop!_OS](https://pop.system76.com/)
- Instalación de [Neovim](https://neovim.io/) en **Ubuntu** desde el paquete [descargado de github](https://github.com/neovim/neovim/releases/latest)
- Instalación de [Librewolf](https://librewolf.net/)
- [Atom](https://atom.io/) ya no se encuentra disponible para instalar por su [fin de desarrollo](https://www.genbeta.com/desarrollo/github-anuncia-muerte-editor-codigo-atom-15-diciembre-su-atencion-se-centrara-vs-code)
- Subida de versión de ECS cli (0.3.17)
- Mejorada la config de **vim** y **neovim**
- Limpieza de llaves SSH
- Post instalación:
  - Cambios repositorios git
  - Nuevos alias bash
- Corrección de errores:
  - Fix de la condición para la ejecución del borrado de snaps
  - Guardar la apt-key de algunas apps en su propio fichero independiente
  - Instalación de **firefox** con .deb después de borrar su snap

## 7.0

- Soporte para **Ubuntu 22.04**
- Soporte para **Fedora 36**
- Eliminación de soporte de versiones anteriores a **Ubuntu 22.04**
- Eliminación de soporte de versiones anteriores a **Fedora 36**
- Eliminación de soporte de versiones anteriores a **Debian 11**
- Instalación de `neovim` en **Ubuntu** usando __PPA__
- Nuevo role `tools/get_latest_version` para obtener la última versión de paquetes alojados en [Github](https://github.com)
- Configuración de LSP en **Neovim**
- Instalación de **Firefox** desde __ppa__ en **Ubuntu** >= 22.04
- Instalación de [**Singlebox**](https://webcatalog.io/singlebox/)
- Corrección de errores:
  - Fix instalación `virtualenvwrapper` en **Arch**
  - Instalación de `libsecret` sólo en distros con **Gnome**
  - Instalación de `vlc` independientemente del entorno gráfico
  - Instalación de `yakuake` en distros con **KDE**
  - Fix permisos en ficheros de configuración creados/actualizados en `post_env`
  - Instalación del paquete `chrome-gnome-shell` para poder instalar extensiones de **Gnome Shell**
  - Fix permisos `~/.ssh` en post instalación
  - Instalación **Neovim** para **Ubuntu 22.04**
  - Instalación de **Virtualbox** para **Ubuntu 22.04**
- Post instalación:
  - Nuevos repositorios git

## VERSIONES ANTERIORES

- [Versión 6](changelog/v6.md)
- [Versión 5](changelog/v5.md)
- [Versión 4](changelog/v4.md)
- [Versión 3](changelog/v3.md)
- [Versión 2](changelog/v2.md)
- [Versión 1](changelog/v1.md)
