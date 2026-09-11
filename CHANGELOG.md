# CHANGELOG

- [CHANGELOG](#changelog)
  - [10.1](#101)
  - [10.0](#100)
  - [VERSIONES ANTERIORES](#versiones-anteriores)
    - [Version 9](#version-9)
    - [Versión 8](#versión-8)
    - [Versión 7](#versión-7)
    - [Versión 6](#versión-6)
    - [Versión 5](#versión-5)
    - [Versión 4](#versión-4)
    - [Versión 3](#versión-3)
    - [Versión 2](#versión-2)
    - [Versión 1](#versión-1)

## 10.2

- Soporte para **Ubuntu 26.04 LTS**
- Borrado instalación de **Lexnet**
- Workflow de **Github** para checkear sintaxis antes de mergear PRs a `master`
- Nuevo playbook [zed_extensions.yml](playbooks/zed_extensions.yml) para instalar extensiones de **Zed**
- La variable `ansible_user_dir`se define mediante variable de entorno del sistema
- Cambios en `post_install`:
  - Corrección menos en post configuración de **Zed**
  - Configuración de **Opencode**
- Cambios en `work`:
  - Nueva entrada en `.ssh/config`
  - Fix typo en configuración ssh

## 10.1

- Soporte para **Fedora 44**
- Nuevo fichero [AGENTS.md](./AGENTS.md)
- Instalación de [SSHub](https://github.com/Petyok/SSHub)
- Modificación de **GitHub Action** para generación de release
- Cambios en `extra_software`:
  - **Zed** instalado por defecto
  - Instalación de **Claude CLI**
  - Instalación de **Open Code**
- Cambios en `post_install`:
  - Configuración de `netbird`
  - Configuración almacén de certificados en __Linux__
- Cambios en `work`:
  - Poder clonar todos los repos de un projecton con __extra_vars__ `clone_project`
- Correccción de errores:
  - Se regeneran los ficheros `gpg` de los roles `post_install` y `work` para que se encripten con la clave gpg correcta
  - Corrección detectando si se trata de **Ubuntu LTS**

## 10.0

- Creación de [role independiente](./roles/work) para configuraciones de trabajo
- Ya no se instala por defecto el gestor de contraseñas **Keeper**
- Instalación de [Zen Browser](https://zen-browser.app/)
- Actualizada la configuración por defecto de [Ghostty](https://ghostty.org/)
- Instalación del editor [Cursor](https://cursor.com/)
- Instalación de [Netbird](https://netbird.io/)
- Nuevas entradas en `.gitignore`
- Instalación de [Google Antigravity](https://antigravity.google.com/)
- Instalación de [Dangerzone](https://dangerzone.rocks/)
- Instalación de [ProtonVPN GUI](https://protonvpn.com/) en lugar de __CLI__
- Paquetes que ya no se instalan en **Fedora**: `srm` y `openvpn`
- Corrección de errores:
  - Definición de variables que habían desaparecido
  - Corrección instalacion de **MegaSYNC**
  - Fixed enlace instalación de **Kor**
  - El playbook `playbooks/prepare_post.yml` mueve al final el desencriptado de `defaults/main.yml.gpg` y lo hace tanto para `post_install` como para `work`
- Cambios en post_install:
  - Eliminada la configuración de **Gimp** (pertenecía a Gimp 2.0)
  - Cambio configuración agente **1Password**
  - Deja de usarse **Dropbox** en favor de **MegaSync**
  - Ya no se instala por defecto: `warp terminal`, `cursor`, `tailscale` y `zed`
  - Ya no se configura `megacmd` porque se usa la autenticación de `megasync`
  - Nuevo proyecto de repositorios de trabajo
  - Fix al crear links para la configuración de **dbeaver**
- Cambios en work:
  - Se han corregido errores de variables en el playbook
  - Errores corregidos en los links que se deben crear

## VERSIONES ANTERIORES

### [Version 9](changelog/v9.md)

### [Versión 8](changelog/v8.md)

### [Versión 7](changelog/v7.md)

### [Versión 6](changelog/v6.md)

### [Versión 5](changelog/v5.md)

### [Versión 4](changelog/v4.md)

### [Versión 3](changelog/v3.md)

### [Versión 2](changelog/v2.md)

### [Versión 1](changelog/v1.md)
