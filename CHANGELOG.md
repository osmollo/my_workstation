# CHANGELOG

## 6.2.2

- Cambio de username en todos mis repositorios de github/gitlab

## 6.2.1

- Fix [README.md](./README.md)

## 6.2

- Compatibilidad con **ElementaryOS** y **Pantheon**
- Instalación de [Trivy](https://github.com/aquasecurity/trivy)
- Instalación de [Ferdi](https://getferdi.com/)
- Instalación de [Station](https://getstation.com/)
- Instalación de [Neovim](https://neovim.io)
- Instalación de nuevas tipografías
- Instalación de [Cloudfare](https://1.1.1.1/) para Debian/Ubuntu
- Eliminados directorios `./docker_deploys` y `./k8s_deploys` y movido todo el contenido de `./ansible` al raíz
- Nuevos alias bash
- Nuevos repositorios para clonar
- Nuevos plugins para Neovim
- Corrección de errores:
  - Cambio repositorio git
  - Eliminación de entradas en `/etc/hosts`
  - Eliminación de entradas en `~/.ssh/config`

## 6.1.4

- Corrección de errores:
  - Ejecución de `playbooks/prepare.yml` desde `install.yml`
- Preparación de post configuración automatizada
- Eliminadas tareas/playbooks relacionados con importación de llaves gpg

## 6.1.3

- Corrección de errores:
  - Creación de link a `bash_history`
  - Corrección key de **1Password** en **Fedora**
  - Fix en el tag `ssh_config`
  - Fix **Firefox** que sólo se ejecute en distribuciones **Ubuntu**
  - Instalación de __cronie__ en **Fedora**
  - Fix ruta VPN en Dropbox
  - Fix configuración __Flatpak__
  - Fix post configuración __zsh__
- Cambios en la instalación de **1Password**:
  - Instalación del cli de **1Password**, nuevo tag `1password_cli`
  - Instalación de la beta de **1Password** en lugar de stable para **Fedora**
- Soporte **Fedora 35**
- Preparación post instalación


## 6.1.2

- Corrección de errores:
  - Desinstalación **Firefox** como snap
  - Eliminados algunos repositorios git a clonar
  - Ejecución de `git.yml` al final del role `post_install` para no retrasar el resto de configuraciones
  - Actualizados los credenciales del registry de docker
  - Instalación llave pública de **Secrethub** en la instalación de **Ubuntu**
  - Corrección en la ruta donde se instala la llave pública en la instalación de **1Password**
  - Actualización contraseña XE

## 6.1.1

- Corrección de errores:
  - Instalación de **Virtualbox 6.1**
  - Fix `install.yml`

## 6.1

- Nuevos alias en `.bash_aliases`
- Paginado del __CHANGELOG.md__ por versiones
- Soporte para **Ubuntu 21.10**
- Separación en playbooks `install.yml` y `post_install.yml`
- Correcciones de errores:
  - Fix gpg key instalación __1password__ en **Ubuntu**
  - Actualizado fichero `roles/extra_software/vars/ohermosa.yml`

## 6.0

- Unificación de los playbooks `install.yml` y `post_install.yml`
- Eliminación de los subroles dentro de `roles/post_install`
- Instalación de [OBS Studio](https://obsproject.com/es)
- Instalación de [CopyQ](https://hluk.github.io/CopyQ/)
- Instalación de las siguientes apps mediante paquete nativo en lugar de snap en **Ubuntu**:
  - Spotify
  - Pycharm
- Instalación de [Google Fonts](https://fonts.google.com/)
- Instalación independiente de las distintas `k8s_tools`
- Eliminación de **Forticlient VPN** porque ya existe un repo específico para eso
- Actualización versión `Apache Directory Studio`
- Corrección de errores:
  - Borrado del tema `Material` de la configuración de **Sublime Text**
- Cambios en `post_install/ohermosa`:
  - Nuevas entradas en `/etc/hosts`
  - Limpieza de alias de bash
  - Limpieza de configuración de ssh
  - Nuevos repositorios git
  - Refactor configuración VPN trabajo

# VERSIONES ANTERIORES

- [Versión 5](changelog/v5.md)
- [Versión 4](changelog/v4.md)
- [Versión 3](changelog/v3.md)
- [Versión 2](changelog/v2.md)
- [Versión 1](changelog/v1.md)
