# CHANGELOG

## 6.1

- Nuevos alias en .bash_aliases
- Paginado del __CHANGELOG.md__ por versiones

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
