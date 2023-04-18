# CHANGELOG

- [CHANGELOG](#changelog)
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

## 9.1

- Actualizadas las versiones de algunos github actions
- Post_install:
  - Entradas en `~/.ssh/config`

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
