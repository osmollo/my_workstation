# CHANGELOG

## 7.0

- Soporte para **Ubuntu 22.04**
- Eliminación de soporte de versiones anteriores a **Ubuntu 22.04**
- Eliminación de soporte de versiones anteriores a **Fedora 35**
- Eliminación de soporte de versiones anteriores a **Debian 11**
- Instalación de `neovim` en **Ubuntu** usando __PPA__
- Nuevo role `tools/get_latest_version` para obtener la última versión de paquetes alojados en [Github](https://github.com)
- Configuración de LSP en **Neovim**
- Instalación de **Firefox** desde __ppa__ en **Ubuntu** >= 22.04
- Corrección de errores:
  - Fix instalación `virtualenvwrapper` en **Arch**
  - Instalación de `libsecret` sólo en distros con **Gnome**
  - Instalación de `vlc` independientemente del entorno gráfico
  - Instalación de `yakuake` en distros con **KDE**
  - Fix permisos en ficheros de configuración creados/actualizados en `post_env`
  - Instalación del paquete `chrome-gnome-shell` para poder instalar extensiones de **Gnome Shell**
- Post instalación:
  - Nuevos repositorios git

## VERSIONES ANTERIORES

- [Versión 6](changelog/v6.md)
- [Versión 5](changelog/v5.md)
- [Versión 4](changelog/v4.md)
- [Versión 3](changelog/v3.md)
- [Versión 2](changelog/v2.md)
- [Versión 1](changelog/v1.md)
