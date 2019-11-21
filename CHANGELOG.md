# CHANGELOG

## 2.4

- Corrección de errores en el despliegue de Consul y Vault

## 2.3

- Se configura `become_ask_pass` en el fichero `ansible.cfg` para que no sea necesario pasar la opción `--ask-become-pass` al ejecutar los playbooks

## 2.2.4.1

- Nuevo secreto para autenticación de artifactory

## 2.2.4

- Export de variable `VAULT_TOKEN` en `/etc/profile`
- Eliminación de tarea duplicada en `environment.yml`
- Creación de secretos para _ohermosa_:
  - Secretos del _gnome-keyring_ con `secret-tools`
  - Secretos de _kwallet_ con `kwalletcli`
  - Contraseñas de _ansible-vault_
- Corrección en backup/restore de **KDE** para esperar a que el directorio `{{ kde_backup_dir }}` esté sincronizado con **Dropbox**
- Instalación de `kwalletcli`

## 2.2.3.1

- Sólo se ejecuta `pre_kde_backup` cuando el entorno de escritorio sea **KDE**

## 2.2.3

- En `pre_kde_backup`, después de crear las copias de seguridad, se borran los originales y se crean enlaces a los backups

## 2.2.2

- Correcciones en la [documentación](README.md)

## 2.2.1

- Simplificado el proceso para obtener el fichero de preferencias de `firefox`

## 2.2

- Soporte para distribuciones basadas en **Debian**
  - Nuevo playbook `config_sudo.yml` para configurar `sudo` en distribuciones basadas en **Debian**
  - Se ha incluído las tasks necesarias en el playbook `update_ansible.yml` para actualizarlo
  - Se han adaptado los roles `common` y `extra_software` a **Debian**, creando enlaces en los ficheros comunes a **Ubuntu**
- Corrección de errores
- Documentación
- Se ha eliminado la instalación de `ansible` del role `common` puesto que ya es necesario tenerlo instalado para ejecutar los playbooks
- Personalización de **Firefox** en `post_install/ohermosa`
- Nuevo tag `post_firefox` para ejecutar la personalización de `firefox`

## 2.1

- Restauración del backup de la configuración de **KDE** (guardada en **Dropbox**) en el role `post_install/ohermosa`
  - Nuevo tag `post_kde_restore` para restaurar la configuración de **KDE** almacenada en **Dropbox**
  - Borrado de los ficheros originales y creación del link a la copia de seguridad
- Playbook `kde_backup.yml` (dentro de `post_install/ohermosa`) para realizar copia de seguridad de los ficheros de configuración de **KDE**
  - Nuevo tag `pre_kde_backup` para ejecutar un backup de los ficheros de configuración de **KDE**. Por defecto se almacenarán en `$DROPBOX/backups/kde`
  - Copia de los ficheros que no tengan backup (que no sean enlaces) al directorio de **Dropbox**

## 2.0

- Se han unificado los playbooks `install.yml` y `post_install.yml` (también los de **vagrant**)
  - Se han adaptado los playbooks del role `post_install/ohermosa` para que queden a la espera de que existan los ficheros que esperan encontrar en **Dropbox**. El tiempo máximo de espera está definido en la variable `wait_dropbox_sync` y está configurado en **1800 minutos**
  - Ya no se actualizan paquetes en post instalación puesto que se ejecuta en el role `common`
  - Se definie la variable `post_install_user` en `Vagrantfile` para que use la configuración `post_install/ohermosa`
- Se ha eliminado el playbook `post_install/ohermosa/tasks/apachedirectory.yml` porque se instala en `extra_software`
- Entrada en `.gitignore` para el playbook `test.yml` para poder hacer pruebas de desarrollo
- Ya no es obligatoria la definición de la variable `post_install_user` para la post instalación si el usuario que ejecuta el playbook (se obtiene de la variable de entorno `$USER`), tiene un subdirectorio de configuración en `roles/post_install`
- Corrección de errores
- Eliminado el índide del [CHANGELOG](CHANGELOG.md)
- Actualización de la [documentación](ansible/README.md)

## 1.9.5

- El tag `install_ohermosa` ha sido renombrado a `ohermosa` y se ha extendido a los roles `common`, `extra_software` y `post_install`
- Corregido el bug que no asignaba los permisos correctos (600) a todos los ficheros de `/home/ohermosa/.ssh/`

## 1.9.4

- Soporte para **XFCE**
- Simplificada la tabla de [Distribuciones soportadas](ansible/README.md#distribuciones-soportadas) en la [documentación](ansible/README.md)

## 1.9.3

- Correcciones para la instalación sobre **Manjaro**:
  - Cambio de repositorio de `ohmyzsh` (ahora apunta a gitlab) por problema con el enlace de descarga
  - Instalación de `ohmyzsh` de la forma tradicional en lugar de usar `yay`
  - instalación de `vagrant` usando `pacman`
  - nuevo tag `install_ohermosa` para mis mierdas
  - instala `zsh` en **arch**
  - quita el check de `dropbox` de `post_install/ohermosa`

## 1.9.2

- Tests sobre **Manjaro** para comprobar que está soportado correctamente
- Nuevas instancias de **Vagrant** para **Manjaro**, **Xubuntu** y **Fedora 31**

## 1.9.1

- Las entradas de `/etc/hosts` se mueven del role `common` al `post_install` y se incluyen registros para la red local de **ohermosa**
- Corrección de error en instalación de paquetes **KDE** para **ArchLinux**

## 1.9.0.1

- fix en el README de ansible

## 1.9

- Soporte para **Arch Linux**
- Módulo `yay` para instalar paquetes de **Arch**
- Separación de paquetes de entorno gráfico de los propios de la distribución
- Nuevo role `tools/install_arch_pkg` para instalar paquetes de **Arch**
- Corrección de errores

## 1.8.7

- En `post_install`, se saca la actualizacion de paquetes del role al playbook
- Detectadas las versiones de ubuntu (y derivadas) dedsde 18.04
- En `update_ansible.yml` se agrupa en bloques segun la distro base

## 1.8.6

- Clonado repositorio `iluvatar` en el `post_install` de **ohermosa**
- Se ignoran los posibles errores del clonado de repositorios de **ohermosa**

## 1.8.5.2

- Modificado el nombre de los perfiles de red de `NetworkManager`

## 1.8.5.1

- Primero se instala el módulo de python `setuptools` y luego el resto

## 1.8.5

- Se clona este mismo repositorio en el directorio `$HOME/git`
- Fix permisos en el directorio `.ssh` en el tag `post_environment`
- Corrección de errores en el tag `install_packages`
- Corrección de error en tag `post_git`

## 1.8.4

- Nuevos perfiles de red wifi en `post_install` de **ohermosa**

## 1.8.3

- Generación aleatoria del UUID de los perfiles para las VPNs del NetworkManager en el `post_install` de **ohermosa**

## 1.8.2

- Instalación de `net-tools` en ubuntu
- Eliminado debug en `post_install/ohermosa/tasks/main.yml`
- Configuración de ZSH para que las apps snap aparezcan en el menú KDE
- Instalación de `network-manager-openvpn` en paquetes de **Ubuntu** (es común para **GNOME** y **KDE**)

## 1.8.1

- Documentacion "primeros pasos" en README
- Definición de `kde_ubuntu_packages` y `kde_gnome_packages`
- Añadido posible mensaje de dropbox sincronizado en inglés para tareas dependientes (`dropbox_response.rc` es 0 tanto si está actualizado como si está sincronizando, así que hay que poner el mensaje de respuesta a fuego)

## 1.8

- Soporte para KDE
  - Definición de la variable `desktop_environment` para que tome el contenido `gnome` o `kde`
  - Instalación de paquetes de **Gnome** o **KDE** en función del escritorio utilizado
  - Se simplifica la invocación a `install_packages.yml` desde `roles/common/tasks/main.yml`
  - Corrección de errores en `include_tasks` cuyas subtareas no cogían los tags correctamente
  - Refactor de variables inferidas para distribuciones basadas en **Ubuntu**/**Fedora
- Nueva instancia de vagrant para `Kubuntu 18.04`
- `ansible_hosts` ya no es el inventario por defecto sino que se tiene que especificar cuando se quiere configurar una instancia de `vagrant`
- README.md actualizado con distribuciones compatibles

## 1.7.2

- Fix en la instalación de `Oh my Zsh!`
- Se configura en `ansible.cfg` que no se compruebe la llave ssh del host

## 1.7.1

- Se han agrupado en subdirectorios los ficheros de la ruta `roles/extra_software/tasks`
- Se ha corregido un error de instalación de `ecs`

## 1.7

- Nuevo directorio `docker_deploys` para el despliegue de aplicaciones en local con `Docker`
- Se ha movido todo lo relacionado con la configuración de la estación de trabajo al directorio `ansible`

## 1.6.4.3

- Añadidos repositorios de la CoP de Python

## 1.6.4.2

- Corregidas las IPs de las instancias vagrant

## 1.6.4.1

- Corrección de errores tipográficos
- Ya no se ejecuta por duplicado la tarea de actualización de paquetes cuando se ejecuta el playbook `install.yml`

## 1.6.4

- Importa llaves públicas gpg de ohermosa en el role `post_install`

## 1.6.3

- Instalación de `docker-compose` incluída en la de `docker`
- Restaura únicamente rutas de `dconf` que contengan la cadena indicada en `extravars`

## 1.6.2

- Instalación de `snap` y `snapd` para distribuciones basadas en **Ubuntu**

## 1.6.1

- Corrección de errores

## 1.6

- Nueva máquina **Linux Mint** en el `Vagrantfile`
- Se ha creado playbook para definir las variables `linux_distribution`, `ubuntu_codename`, `ubuntu_version` y `fedora_version` para poder trabajar con distribuciones basadas en **Ubuntu** y **Fedora**
- Se han adaptado todas las tareas para usar las variables definidas anteriormente
- Correcciones de errores

## 1.5

- instalación de kubectl

## 1.4.2

- creacion de ficheros vacíos para vault_pass en el post_install de *ohermosa*
- nuevos repositorios para clonar en el post_install de *ohermosa*
- se instala modulo de python `docker-py`
- documentación para el uso de cifrado de contraseñas en [README.md](README.md)

## 1.4.1

- Se mueve la lista de enlaces a crear en *post_install/environment- a lista de variables
- Se crea un nuevo enlace para cargar credenciales de `asgard` en el role *post_install*
- Se crea el directorio `$HOME/python-venv`
- Se incluyen los paquetes de desarrollo de python2 y python3 para instalar en common
- Se infiere la variable `ansible_user_dir` en todos los playbooks

## 1.4

- Instalación de `Cherrytree`
- CHANGELOG.md para registrar el historial de cambios para cada versión
- Uso del provider `virtualbox` para `vagrant` en lugar de `libvirt`
- Fix en el repositorio de `virtualbox` para `fedora`
- Fix en los box de `vagrant` para `fedora` y `ubuntu`
- Inventario dinámico para las máquinas de `vagrant`
- Borrardo de directorios predeterminados en el `$HOME` del usuario tras la instalación del sistema
- Actualizazción README con el comando para ver commits entre tags
- Instalación de la última versión de vagrant en ubuntu

## 1.3.1

- Corrección de errores en la instalación de docker, para **fedora** se estaba instalando virtualbox

## 1.3

- Instalación de codecs de autio y paquetes de utilidadeds
- Instalación de `deluge`
- Instalación de `chromium`

## 1.2.1

- Corregida la ruta de los repositorios para clonar en el post_install de **ohermosa**
- Corrección de errores en `post_install`
- Se corrige un problema con la variable `ansible_user` que no era consistente en todas las tasks

## 1.2

- Instalación de `franz`
- Instalación de `rambox`

## 1.1

- Instalación de `skype`
- Instalación de `postman`
- Instalación de `Java OpenJDK`
- Instalación de `Apache Directory Studio`
- post_install de `Apache Directory Studio` para **ohermosa**

## 1.0.4

- Correcciones en `Vagrantfile` y `README.md`

## 1.0.3

- Corrección de errores en la instalación de `Ether Cloud Services`
- Actualización de la versión de `No Machine` y corrección de errores en su instalación
- Se ha modificado el nombre de las tareas en el fichero *extra_software/tasks/main.yml*
- Corrección de errores en la instalación de `slack`
- Se han movido los playbooks para `vagrant` al subdirectorio *./vagrant*

## 1.0.2

- En **Ubuntu**, `ansible` se instala desde repositorio ppa en lugar de copiar el fichero del repositorio

## 1.0.1

- El repo de `virtualbox` se descarga de internet en lugar de generarse a partir de un template
- Se define la variable `virtualbox_packages` en base a la distribución usada y se incluyen dependencias para **Fedora**
- Se modifica la ruta a la llave privada ssh para que sea dinámica en lugar de ir a fuego
- Se documenta en el README.md cómo se usa Vagrant para pruebas

## 1.0

- Primera versión funcional
