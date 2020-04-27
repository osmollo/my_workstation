# CHANGELOG

## 3.7

- Nuevos repositorios git en `post_install/ohermosa`:
  - [Terraform provider openstack flavors patch](https://globaldevtools.bbva.com/bitbucket/projects/MLYID/repos/mlyid_terraform_provider_openstack/browse)

## 3.6

- Soporte para **Ubuntu 20.04**:
  - Ñapas temporales para software de terceros que todavía no ha incorporado paquetes de __20.04__
  - Ya no se instalan paquetes de `python2` (no viene instalado por defecto en __20.04__)
  - `prepare.yml` adaptado
  - `WoeUSB` sólo es instalable en __18.04__
- Correcciones de errores:
  - Tabla [ansible/README.md](ansible/README.md)
  - Enlace a la última versión del gist `extensions.json` de **Code**
  - Errores de creación/borrado de repositorios en **github**/**gitlab**
  - Errores en la instalación de extensiones de **Code**/**Atom** cuando no se realizaba la instalación de estos editores
  - Errores en `post_install/ohermosa`:
    - Correcciones en `gimp.yml`, `hp.yml` y `pass.yml`
    - `crontab.yml` configurado con ansible en lugar de ser restaurado de **Dropbox**
    - `docker.yml` configuración de **docker** con ansible en lugar de ser restaurado de **Dropbox**
- Nuevo tag `code_extensions` para instalar extensiones en **Code**
- Nuevo tag `atom_extensions` para instalar paquetes de **Atom**
- Paquetes de **Atom** se obtienen de [gist de ohermosa](https://gist.githubusercontent.com/ohermosa/854b27da91246625596f8839cc365713/raw/packages.json) en lugar de fichero local
- Simplificación en instalación de extensiones de **Code**
- Instalación de tipografía [Fira code](https://github.com/tonsky/FiraCode/)
- Nuevos repositorios git en `post_install/ohermosa`:
  - [Docker Image Generator](https://github.com/tuxotron/docker-image-generator)
  - [GoPass](https://github.com/gopasspw/gopass.git)
- Nuevos despliegues con `Docker`:
  - [Kafka](docker_deploys/kafka)
  - [Consul](docker_deploys/consul)
- Instalación de [Typora](https://typora.io)
- Identificación en el nombre de tareas de `extra_software` y `post_install`

## 3.5

- Instalación de `Lens` con AppImage
- Instalación de `kdenlive` dentro del role `common`
- Instalación de `wireguard`
- Cambios en `post_install/ohermosa`:
  - Nuevos repositorios git:
    - [hetzner](https://gitlab.com:ohermosa/hetzner)
- Corrección de errores:
  - En configuración `OpenVPN` se elimina que todo el tráfico se redirija por la VPN

## 3.4

- Mejora de la documentación [README](ansible/README.md)
- Instalación de `rsync` en el role `common`
- Instalación de `Authy` para segundo factor de autenticación
- Instalación de `YakYak` para cliente de **Hangouts**
- Instalación de `Hiri` para cliente de correo **Outlook**
- Instalación de `Steam` para **Ubuntu**

## 3.3

- Configuración básica de cliente ssh
- Instalación de `Bitwarden CLI`
- Corrección de errores:
  - No se propagaban correctamente los tags de `post_install`
- Cambios en [README](README.md)
- Nuevos paquetes instalados en **ubuntu**
- Cambios en `post_install/ohermosa`:
  - Nuevos repositorios git:
    - [mkcert](https://github.com/FiloSottile/mkcert)
  - Corrección de errores al configurar `prezto`

## 3.2

- Eliminación del tag `ohermosa`
- Configuración del software instalado para cada usuario en `roles/extra_vars/vars/$USER.yml`
- Instalación de extensiones de **Code** en el role `extra_software` en vez de en `post_install/datio`
- Corrección de errores
- Se puede ejecutar el playbook `install.yml` sin que el usuario disponga de un subrole debajo de `post_install`
- Ahora `install.yml` falla si no se ha ejecutado previamente `playbooks/prepare.yml`
- Nuevo módulo para obtener los forks de un repositorio de **gitlab**
- Nuevo módulo para obtener los repositorios de la propia cuenta de **gitlab**
- Instalación de `certutil`
- Cambios en `post_install/ohermosa`:
  - Se crean __remotes__ para repositorios de **gitlab** que tengan forks

## 3.1

- Renombrado de los tags para quitar el `install_` y `post_`
- Cambios en instalación [Lexnet](https://lexnet.justicia.es/)
  - Instalación de certificados ACA
  - Instalación librerías
  - Renombrado del tag `install_firefox_lexnet` por `install_lexnet`

## 3.0

- Unificación de los playbooks `install.yml` y `post_install.yml`
- Unificación de los playbooks `config_sudo.yml`, `update_ansible.yml` y `update_packages.yml` en el playbook `prepare.yml`
- Corrección de errores:
  - Se estaba usando `yum` para instalar algunos paquetes en **debian** y derivados
  - Se elimina la caché de yum/apt después de instalar paquetes del sistema
  - Se incluye el fichero de variables correspondiente para instalar paquetes de python
  - Corregido error en instalación de prezto
  - Documentación actualizada

## 2.18.1

- Corrección de errores

## 2.18

- Instalación de cliente [**Spotify TUI**](https://www.genbeta.com/multimedia/alguien-ha-creado-cliente-spotify-para-terminal-linux-windows-macos-maravilla) por consola con tag `--install_spotify_cli`
- `requirements.txt` con todos los paquetes instalados en el repositorio para hacer pruebas
- Nuevos plugins de vim:
  - [AutoComplPop](https://github.com/vim-scripts/AutoComplPop)
  - [ctrlp](https://github.com/kien/ctrlp.vim)
- Cambios en `post_install/ohermosa`:
  - Wallpaper dinánimo [Mojave](https://www.omgubuntu.co.uk/2018/06/macos-mojave-dynamic-background-linux) para **ubuntu**
  - Configuración de **Spotify Tui**
  - Nuevos repositorios git:
    - [spotify-tui](https://github.com/Rigellute/spotify-tui/)

## 2.17

- Instalación de `FZF` con el tag `--install_fzf`
- Instalación de plugins de `vim`:
  - [vundle](https://github.com/VundleVim/Vundle.vim)
  - [lightline](https://github.com/itchyny/lightline.vim)
  - [nerdtree](https://github.com/preservim/nerdtree)
  - [colors solarized](https://github.com/altercation/vim-colors-solarized)
  - [ansibe](https://github.com/pearofducks/ansible-vim)
  - [vim](https://github.com/frazrepo/vim-rainbow)
  - [fzf](https://github.com/junegunn/fzf.vim)
  - [gitgutter](https://github.com/airblade/vim-gitgutter)
  - [multiple cursors](https://github.com/terryma/vim-multiple-cursors)
  - [ack](https://github.com/mileszs/ack.vim)
- Fix en la instalación de `NoMachine` para obtener la última versión
  - Nuevo módulo de ansible `get_nomachine_latest.py`
- Cambios en `post_install/ohermosa`:
  - Nuevos repositorios:
    - [cock_ansible](https://github.com/ohermosa/cock_ansible)
    - [fzf](https://github.com/junegunn/fzf)

## 2.16.2

- Nuevo módulo de ansible `protonvpn_fastest` para obtener la lista de los servidores de **protonvpn** más rápidos
- Cambios en `post_install/ohermosa`:
  - Creación de un perfil para **protonvpn** en el network manager del sistema

## 2.16.1

- Cambios en `post_install/ohermosa`:
  - Configuración de **ProtonVPN** con el nuevo tag `--post_protonvpn`
  - Nuevo repositorio git:
    - [protonvpn-cli-ng](https://github.com/ProtonVPN/protonvpn-cli-ng)

## 2.16

- Nuevo módulo `get_go_latest` para obtener la última versión disponible de `GO`
- Instalación de `GO`. Nuevo tag `--install_go`
- Instalación de `secure-delete` en el role `common`
- Refactor de la instalación de `Firefox Lexnet Edition`
- Instalación por defecto de varios paquetes de `Atom`

## 2.15

- Instalación de `Balena Etcher` para quemar imágenes iso en USB
- Instalación de `WoeUSB` para quemar imágenes de windows en USB
- Nuevo `docker_deploy/bitwarden` para probar `Bitwarden`
- Nuevo directorio `playbooks`
  - Ya no es necesario pasarle el fichero donde se encuentra el token de acceso al playbook `delete_repos.yml`
  - Nuevo playbook `get_secret.yml` para obtener el valor de variables cifradas
  - Nuevo playbook `kde_backup.yml` para hacer copia de seguridad de **KDE**. Ejecuta las tareas de `post_install/$USER/tasks/kde_backup.yml`

## 2.14

- Corrección de errores
  - se ha modificado la config de `prezto` para que funcione el autocompletado al ejecutar `cd ../`
  - se configura la carga del fichero `/etc/profile.d/apps-bin-path.sh` cada tras la instalación de `prezto` para **KDE**
  - actualización de las apps a instalar en los playbooks `datio.yml` y `vagrant/datio.yml`
- Cambios en `post_install/ohermosa`:
  - refactor de la personalización de la configuración de `prezto`
  - nuevo tag `deploy_fonts` para instalar las fuentes powerline para **Code**
  - nuevos repositorios git:
    - [fonts](https://github.com/powerline/fonts)
  - Corrección de errores:
    - Se mostraba por pantalla las contraseñas de `ansible-vault` al crear los ficheros `.vault_pass*.txt`

## 2.13

- Instalación del cliente `Proton VPN`
- Instalación de `Prezto`
- Cambios en `post_install/ohermosa`:
  - Actualizada la contraseña de **Mega**
  - Correciones de errores
  - Configuración `prezto` tras migrar de `oh my zsh` si estuviera instalado

## 2.12.1

- Se ha simplificado la forma de obtener el nombre de repositorio al crear los remotes de git en `post_install/ohermosa` para que sea independiente de la ruta

## 2.12

- Nuevo `docker_deploy/gitea` para probar `Gitea`
- Nuevas tools `tools/github_repo` y `tools/gitlab_repo` para crear/eliminar repositorios en **github** y **gitlab** correspondientemente
- Nuevo playbook `delete_repos.yml` para eliminar repositorios de **github** y **gitlab**. Coge los token del fichero pasado por `extravars` con el nombre `secrets`

```bash
ansible-playbook delete_repos.yml -e secrets=roles/post_install/ohermosa/defaults/main.yml [-e target=[all|gitlab|github]]
```

- Se instala el módulo de python `gitpython`
- Cambios en  `post_install/ohermosa`:
  - instalación cliente `protonvpn`
  - creación de virtualenvs de python para los repositorios git existentes
  - si se define la creación de un remote en un repositorio de gitlab que no existe, se crea
  - refactor de la variable `git_repositories` para simplificar la creación de __remotes__ de **git**. Ahora si alguno de los repositorios tiene una variable `remote` (con valores posibles __"gitlab"__ o __"github"__), se creará un repositorio con el mismo nombre en la plataforma correspondiente y se configurará como __remote__ del repositorio original
- Corrección de errores
  - Fixes en la instalación de `Pass`

## 2.11

- Se modifican los permisos de los *$HOME* de usuario a 750
- Instalación de [Firefox ESR](https://www.mozilla.org/es-ES/firefox/all/#product-desktop-esr)
- Instalación del gestor de contraseñas [Pass](https://www.passwordstore.org/)
- Instalación de `bucklespring` (tag `install_bucklespring`) para **Debian** y **Ubuntu**
- Cuando se instala `kubectl`, también se descarga `Hetzner-kube` (disponible el tag `--install_hetznerkube`)
- Cambios en `post_install/ohermosa`:
  - Nuevos repositorios git:
    - [hetzner-kube](https://github.com/xetys/hetzner-kube))
    - [awesome-hcloud](https://github.com/hetznercloud/awesome-hcloud)
  - Configuración de `Pass`
  - Nuevo tag `post_env` como abreviatura de `post_environment`
- Corrección de errores:
  - Se eliminan los binarios de la ruta `/usr/local/bin` antes de descargarlos para que se puedan actualizar

## 2.10

- Nuevo role `tools/telegram` para enviar mensajes de telegram
- Refactor en playbook `datio.yml` para pedir al usuario su XE
- Configuración de autocompletado de `kubectl` tras su instalación
- Cuando se instala `kubectl`, también se descarga `Helm` (disponible el tag `--install_helm`)
- Cambios en `post_install/ohermosa`:
  - Nuevo repositorio [Argos](https://gitlab.com/ohermosa/argos)
  - Nuevo repositorio [Hetzner K8S](https://gitlab.com/ohermosa/hetzner_k8s)
  - Fixes:
    - Corregido error al crear remotes en los repositorios
    - También se pueden crear remotes en los repositorios personales
- Instalación del módulo python `hcloud`

## 2.9

- Instalación del gestor de contraseñas `Bitwarden`
- Corrección de errores:
  - Fix en `/etc/profile` al cargar la variable `VAULT_TOKEN`. Se usa __kwalletcli__ o __secret-tool__ en función del entorno de escritorio
  - Fix en la tarea de actualización de paquetes
- Instalación de los módulos de python `mega.py` y `netaddr`
- Instalación de módulos de python como usuario sin privilegios
- Cambios en `post_install/ohermosa`:
  - Creación de `remote` en repositorios de trabajo

## 2.8

- Nuevo role `post_install/datio` para realizar una configuración general para un pc de trabajo de [Datio](www.datio.com)
  - Documentación
  - Nuevos playbooks `datio.yml` y `vagrant/datio.yml` para realizar todo el proceso de instalación (`common`, `extra_software` y `post_install`)
- Fixes:
  - `vagrant/install.yml` no tenía definida la variable `disable_updates`
  - Resueltas dependencias en **Ubuntu** para instalar extensiones de `Visual Code Studio`
- Instalación de `Bitwarden`

## 2.7.1

- Se ha replicado el __brexit__ en el playbook `vagrant/install.yml`

## 2.7

- Más personalizaciones en role `post_install/ohermosa`:
  - Instalación de paquetes para impresoras HP
  - Configuración de `VIM`
  - Configuración de `Gimp`
  - Nuevo repositorio git:
    - [onetimesecret](https://gitlab.com/ohermosa/onetimesecret)
- Instalación navegador `Brave`, tag  `install_brave`
- Nuevo tag `install_browsers` para instalar todos los navegadores disponibles

## 2.6

- Se han vuelto a separar las tareas de post instalación del playbook principal a `post_install.yml`
  - Documentación
- Instalación navegador `Vivaldi`

## 2.5.1

- Soporte para `Cinnamon` en el playbook `load_distro_vars.yml`
- Se ha templatizado la lógica para obtener el paquete de `MEGAsync` necesario en base al entorno de escritorio
- Fix al restaurar la configuración de **dconf**, diferenciando entre **Gnome** y **Cinnamon**

## 2.5

- Instalación del cliente de escritorio `MEGA sync`
  - Nuevo tag `install_megasync`
- Instalación del cliente `MEGAcmd`
  - Nuevo tag `install_megacmd`
  - Configuración de `MEGAcmd` en el role `post_install/ohermosa` con el tag `post_megacmd`
- Nuevo tag `install_mega` que engloba la instalación de `MEGAsync` y `MEGAcmd`

## 2.4.5.1

- Correcciones de errores

## 2.4.5

- Nuevo repo git para **ohermosa**:
  - [pepi](https://gitlab.com/ohermosa/pepi)
- Fix importando gpg keys para que solo muestre _CHANGED_ cuando se haya importado una llave nueva
- Quitadas entradas de _id2_ de `/etc/hosts` porque ahora está configurado en el `.ssh/config` guardado en **Dropbox**
- Se configura `changed_when` en tareas con `shell` cuando aplica
- `update_packages.yml` también actualiza el fichero `/var/tmp/.update` para no volver a actualizar paquetes si ya se hizo en la última semana
  - Actualizado el playbook `vagrant/update_packages.yml` para incluir actualización de **Arch** y el flag de actualización
- Eliminado play duplicado en `vagrant/install.yml` y eliminada definición de `ansible_user` porque ya está en el inventario dinámico

## 2.4.4

- El backup de **KDE** se hace de todos los ficheros del directorio `$HOME/.config`, no sólo de los _*rc_
- Nuevos repositorios git:
  - [mlyid_athens_lb](https://globaldevtools.bbva.com/bitbucket/projects/MLYID/repos/mlyid_athens_lb/browse)
  - [mlyid_dnsbased_ha](https://globaldevtools.bbva.com/bitbucket/projects/MLYID/repos/mlyid_dnsbased_ha/browse)
  - [mlyid_docker-gc](https://globaldevtools.bbva.com/bitbucket/projects/MLYID/repos/mlyid_docker-gc/browse)
  - [mlyid_gerrit](https://globaldevtools.bbva.com/bitbucket/projects/MLYID/repos/mlyid_gerrit/browse)
  - [mlyid_pgbackup](https://globaldevtools.bbva.com/bitbucket/projects/MLYID/repos/mlyid_pgbackup/browse)
  - [mlyid_postgresha](https://globaldevtools.bbva.com/bitbucket/projects/MLYID/repos/mlyid_postgresha/browse)

## 2.4.3

- Nuevo `docker-compose.yml` para **Vault**+**Consul**

## 2.4.2

- Cambios en `post_install/ohermosa`:
  - Fix entrada dashboard openstack
  - Nuevos repositorios git:
    - [pi-hole](https://github.com/pi-hole/pi-hole)
    - [docker-pi-hole](https://github.com/pi-hole/docker-pi-hole)
    - [awesome-sysadmin](https://github.com/kahun/awesome-sysadmin)
    - [quotes-simple-web](https://github.com/pando85/quotes-simple-web.git)
    - [oh my bash](https://gitlab.com/ohermosa/oh-my-bash)
    - [oh my zsh](https://gitlab.com/ohermosa/oh-my-zsh)
    - [docker compose cookbooks](https://github.com/robcowart/docker_compose_cookbook)
- Nuevo despliegue `docker_deploys/pihole`

## 2.4.1

- En el role `common` no se actualizarán los paquetes si hace menos de una semana que se ha ejecutado la actualización por última vez.

## 2.4

- Posibilidad de deshabilitar la actualizacion de paquetes mediante...
  - pasar por extravars la variable `disable_updates`
  - exportar la variable de entorno `REPO_DISABLE_UPDATES` a _1_

## 2.3.1

- Más personalizaciones para **firefox** en `post_install/ohermosa`:
  - Preguntar directorio de descarga
  - No guardar contraseñas

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
