# post_install

## Acciones disponibles

| **TAG** | **DESCRIPCIÓN** | **REQUIERE Dropbox** |
|------------|--------------|----------------------|
| **post_install** | Ejecuta el role completo | :cloud: |
| **del_default_dirs** | Borra los directorios predeterminados en `$HOME` que se crean en la instalación | |
| **gnome_extensions** | Instala extensiones de Gnome disponibles en el repositorio | |
| **gnome_conf** | Restaura la configuración de gnome guardada en **Dropbox** y obtenida con `dconf dump /` | |
| **gnome** | Ejecuta todas las tareas relacionadas con gnome (`gnome_extensions` y `gnome_conf`) | |
| **kde_restore** | Restaura la copia de seguridad los ficheros de configuración de **KDE** almacenados en **Dropbox**. Borra el original y crea un enlace simbólico al backup | :cloud: |
| **pre_kde_backup** | Realiza una copia de seguridad de los ficheros de `$HOME/.config/*rc` en **Dropbox** | :cloud: |
| **docker**/**post_docker** | Restaura de **Dropbox** los login en repositorios de Docker y la configuración del demonio `docker` | |
| **crontab** | Restaura de **Dropbox** el crontab del usuario | |
| **environment** <br> **env**| Restaura de **Dropbox** los ficheros de configuración del entorno (`.bashrc`, `.bash_history`, `.zshrc`,...) | :cloud: |
| **git** | Clona los repositorios indicados en el fichero de variables y configura el `user.email` y `user.name` en cada uno de ellos | :cloud: |
| **network** | Genera las configuraciones para las conexiones de red | |
| **sublime**/**post_sublime** | Restaura la configuración de `Sublime Text` y `Sublime Merge` almacenada en **Dropbox** | :cloud: |
| **sublimetext**/**post_sublimetext** | Restaura la configuración de `Sublime Text` almacenada en **Dropbox** | :cloud: |
| **sublimemerge**/**post_sublimemerge** | Restaura la configuración de `Sublime Merge` almacenada en **Dropbox** | :cloud: |
| **gpg** | Importa llaves públicas GPG del keyserver | |
| **firefox** | Personaliza `Firefox` | |
| **secrets** | Crea los secretos específicos para el usuario _ohermosa_ | |
| **megacmd**/**post_megacmd** | Configura el cliente **MEGAcmd** | |
| **hp** | Instala packetes para impresora **HP** | |
| **vim** | Configura **Vim** | |
| **gimp** | Configura **Gimp** | |
| **python**/**post_python**| Crea virtualenvs para repositorios git que tengan el fichero `requirements.txt` | :cloud: |
| **prezto**/**post_prezto** | Personaliza la configuración de `prezto` | |
| **protonvpn** | Configura el cliente **protonvpn** | |
| **spotify**/**post_spotify** | Configura el cliente de **spotify** de consola | |
| **ohermosa** | Ejecuta los post instalación de **ohermosa** | :cloud: |

| :information_source: **WARNING**: algunos de los tags anteriores requieren que **Dropbox** esté totalmente sincronizado antes de ejecutarse |
| --- |

## Paso previo

Antes de poder ejecutar el role, es necesario ejecutar el playbook `./playboks/prepare_post.yml`:

```shell
ansible-playbook playbooks/prepare_post.yml
```

Este playbook importa las claves GPGs y desencripta el fichero `roles/post_install/defaults/main.yml.gpg`.

## Ejemplo de uso

```shell
ansible-playbook post_install.yml -t git
```
