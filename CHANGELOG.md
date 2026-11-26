# CHANGELOG

- [CHANGELOG](#changelog)
  - [11.0](#110)
  - [VERSIONES ANTERIORES](#versiones-anteriores)
    - [Version 10](#version-10)
    - [Version 9](#version-9)
    - [Versión 8](#versión-8)
    - [Versión 7](#versión-7)
    - [Versión 6](#versión-6)
    - [Versión 5](#versión-5)
    - [Versión 4](#versión-4)
    - [Versión 3](#versión-3)
    - [Versión 2](#versión-2)
    - [Versión 1](#versión-1)

## 11.0

- ~~Soporte para **Ubuntu 26.04 LTS**~~
- Soporte para distribuciones atómicas:
  - [**Fedora Kinoite**](https://fedoraproject.org/atomic-desktops/kinoite/)
- Soporte para distribuciones basadas en **Ubuntu** pero que no usan paquetes __snap__ (**Linux Mint**, **Pop!_OS** y **Elementary OS**)
- Borrado instalación de **Lexnet**
- Workflow de **Github** para checkear sintaxis antes de mergear PRs a `master`
- La variable `ansible_user_dir`se define mediante variable de entorno del sistema
- Instalación de **Claude Code** en **Ubuntu**
- Añadido [CLAUDE.md](./CLAUDE.md)
- Ya no se guardan en variables las URLs de los paquetes **Flatpak** sino que se usan directamente los IDs en las correspondientes tareas
- Ya no se instala el plugin de **MegaSync** para cada gestor de ficheros
- Soporte **WSL**
- Instalación de **Wezterm** en el host Windows.
- Corrección de errores:
  - Fix en la instalación de **Claude**
  - Corrección enlaces de descarga de múltiples [tools](roles/extra_software/tasks/tools/)
- Cambios en `post_install`:
  - Sincronización de extensiones de **Zed**
  - Configuración de **Opencode**
  - Configuración de **Claude**
  - Fichero independiente para **Netbird**
  - Variables de entorno para deshabilitar envío de datos de **Claude Code** y otras herramientas
- Cambios en `work`:
  - Nueva entrada en `.ssh/config`
  - Fix typo en configuración ssh
  - Excepción clonado repositorios git `ccdd-portainer-stack
  - Fix certificado Artifactory
  - Fix ssh_config para WSL
  - Alias `ssh`, `ssh-add` y `scp` para **wsl**

## VERSIONES ANTERIORES

### [Version 10](changelog/v10.md)

### [Version 9](changelog/v9.md)

### [Versión 8](changelog/v8.md)

### [Versión 7](changelog/v7.md)

### [Versión 6](changelog/v6.md)

### [Versión 5](changelog/v5.md)

### [Versión 4](changelog/v4.md)

### [Versión 3](changelog/v3.md)

### [Versión 2](changelog/v2.md)

### [Versión 1](changelog/v1.md)
