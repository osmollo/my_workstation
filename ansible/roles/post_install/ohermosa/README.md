# install/ohermosa

## Acciones disponibles

| **TAG** | **DESCRIPCIÓN** | **REQUIERE Dropbox** | **REQUIERE `ask-vault-pass`** |
|------------|--------------|----------------------|-------------------------------|
| **post_install** | Ejecuta el role completo | :cloud: | :lock: |
| **del_default_dirs** | Borra los directorios predeterminados en `$HOME` que se crean en la instalación | | |
| **gnome_extensions** | Instala extensiones de Gnome disponibles en el repositorio | | |
| **gnome_conf** | Restaura la configuración de gnome guardada en **Dropbox** y obtenida con `dconf dump /` | | |
| **gnome** | Ejecuta todas las tareas relacionadas con gnome (`gnome_extensions` y `gnome_conf`) | | |
| **kde_restore** | Restaura la copia de seguridad los ficheros de configuración de **KDE** almacenados en **Dropbox**. Borra el original y crea un enlace simbólico al backup | :cloud: | |
| **pre_kde_backup** | Realiza una copia de seguridad de los ficheros de `$HOME/.config/*rc` en **Dropbox** | :cloud: | |
| **docker** | Restaura de **Dropbox** los login en repositorios de Docker y la configuración del demonio `docker` | | |
| **crontab** | Restaura de **Dropbox** el crontab del usuario | | |
| **environment** <br> **env**| Restaura de **Dropbox** los ficheros de configuración del entorno (`.bashrc`, `.bash_history`, `.zshrc`,...) | :cloud: | |
| **git** | Clona los repositorios indicados en el fichero de variables y configura el `user.email` y `user.name` en cada uno de ellos | :cloud: |
| **network** | Genera las configuraciones para las conexiones de red | | :lock: |
| **sublime** | Restaura la configuración de `Sublime Text` y `Sublime Merge` almacenada en **Dropbox** | :cloud: | |
| **sublimetext** | Restaura la configuración de `Sublime Text` almacenada en **Dropbox** | :cloud: | |
| **sublimemerge** | Restaura la configuración de `Sublime Merge` almacenada en **Dropbox** | :cloud: | |
| **gpg** | Importa llaves públicas GPG del keyserver | | |
| **firefox** | Personaliza `Firefox` | | |
| **secrets** | Crea los secretos específicos para el usuario _ohermosa_ | | :lock: |
| **megacmd** | Configura el cliente **MEGAcmd** | | :lock: |
| **hp** | Instala packetes para impresora **HP** | | |
| **vim** | Configura **Vim** | | |
| **gimp** | Configura **Gimp** | | |
| **pass** | Configura el gestor de secretos **Pass** | | |
| **python** | Crea virtualenvs para repositorios git que tengan el fichero `requirements.txt` | :cloud: | |
| **prezto** | Personaliza la configuración de `prezto` | | |
| **protonvpn** | Configura el cliente **protonvpn** | | :lock: |
| **spotify** | Configura el cliente de **spotify** de consola | | |
| **ohermosa** | Ejecuta los post instalación de **ohermosa** | :cloud: | :lock: |

| :information_source: **WARNING**: algunos de los tags anteriores requieren que **Dropbox** esté totalmente sincronizado antes de ejecutarse |
| --- |

## Ejemplo de uso

```bash
ansible-playbook install.yml -t git
```
