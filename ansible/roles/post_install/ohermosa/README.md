# post_install/ohermosa

- [post_install/ohermosa](#post_installohermosa)
  - [Acciones disponibles](#acciones-disponibles)
  - [Ejemplo de uso](#ejemplo-de-uso)

## Acciones disponibles

| **TAG** | **DESCRIPCIÓN** |
|------------|--------------|
| **post_install** | Ejecuta el role completo |
| **post_del_default_dirs** | Borra los directorios predeterminados en `$HOME` que se crean en la instalación |
| **post_gnome_extensions** | Instala extensiones de Gnome disponibles en el repositorio |
| **post_gnome_conf** | Restaura la configuración de gnome guardada en **Dropbox** y obtenida con `dconf dump /` |
| **post_gnome** | Ejecuta todas las tareas relacionadas con gnome (`post_gnome_packages`, `post_gnome_extensions` y `post_gnome_conf`) |
| **post_docker** | Restaura de **Dropbox** los login en repositorios de Docker y la configuración del demonio `docker` |
| **post_crontab** | Restaura de **Dropbox** el crontab del usuario |
| **post_environment** | Restaura de **Dropbox** los ficheros de configuración del entorno (`.bashrc`, `.bash_history`, `.zshrc`,...) |
| **post_git** | Clona los repositorios indicados en el fichero de variables y configura el `user.email` y `user.name` en cada uno de ellos |
| **post_vpn** | Genera las configuraciones para las VPNs (OpenVPN y VPNaaS) |
| **post_sublime** | Restaura la configuración de `Sublime Text` almacenada en **Dropbox** |
| **post_apachedirectory** | Restaura el lanzador de `Apache Directory Studio` para que apunte a la copia de **Dropbox** |
| **post_gpg** | Importa llaves públicas GPG del keyserver |

| **WARNING**: algunos de los tags anteriores requieren que **Dropbox** esté totalmente sincronizado antes de ejecutarse |
| --- |

## Ejemplo de uso

```bash
ansible-playbook post_install.yml --ask-become-pass -t post_apachedirectory -e post_install_user=ohermosa
```
