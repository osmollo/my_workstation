# post_install/ohermosa

## Acciones disponibles

| **TAG** | **DESCRIPCIÓN** | **REQUIERE Dropbox** | **REQUIERE `ask-vault-pass`** |
|------------|--------------|----------------------|-------------------------------|
| **post_install** | Ejecuta el role completo | :cloud: | :lock: |
| **post_del_default_dirs** | Borra los directorios predeterminados en `$HOME` que se crean en la instalación | | |
| **post_gnome_extensions** | Instala extensiones de Gnome disponibles en el repositorio | | |
| **post_gnome_conf** | Restaura la configuración de gnome guardada en **Dropbox** y obtenida con `dconf dump /` | | |
| **post_gnome** | Ejecuta todas las tareas relacionadas con gnome (`post_gnome_extensions` y `post_gnome_conf`) | | |
| **post_kde_restore** | Restaura la copia de seguridad los ficheros de configuración de **KDE** almacenados en **Dropbox**. Borra el original y crea un enlace simbólico al backup | :cloud: | |
| **pre_kde_backup** | Realiza una copia de seguridad de los ficheros de `$HOME/.config/*rc` en **Dropbox** | :cloud: | |
| **post_docker** | Restaura de **Dropbox** los login en repositorios de Docker y la configuración del demonio `docker` | :cloud: | |
| **post_crontab** | Restaura de **Dropbox** el crontab del usuario | :cloud: | |
| **post_environment** | Restaura de **Dropbox** los ficheros de configuración del entorno (`.bashrc`, `.bash_history`, `.zshrc`,...) | :cloud: | |
| **post_git** | Clona los repositorios indicados en el fichero de variables y configura el `user.email` y `user.name` en cada uno de ellos | :cloud: |
| **post_network** | Genera las configuraciones para las conexiones de red | | :lock: |
| **post_sublime** | Restaura la configuración de `Sublime Text` almacenada en **Dropbox** | :cloud: | |
| **post_gpg** | Importa llaves públicas GPG del keyserver | | |
| **post_firefox** | Personaliza `Firefox` | | |
| **post_secrets** | Crea los secretos específicos para el usuario _ohermosa_ | | :lock: |
| **post_megacmd** | Configura el cliente **MEGAcmd** | | :lock: |
| **post_hp** | Instala packetes para impresora **HP** | | |
| **post_vim** | Configura **Vim** | | |
| **post_gimp** | Configura **Gimp** | | |
| **post_pass** | Configura el gestor de secretos **Pass** | | |
| **ohermosa** | Ejecuta los post instalación de **ohermosa** | :cloud: | :lock: |

| :information_source: **WARNING**: algunos de los tags anteriores requieren que **Dropbox** esté totalmente sincronizado antes de ejecutarse |
| --- |

## Ejemplo de uso

```bash
ansible-playbook post_install.yml -t post_git [-e post_install_user=ohermosa]
```
