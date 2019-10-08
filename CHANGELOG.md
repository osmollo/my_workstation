# CHANGELOG

- [CHANGELOG](#changelog)
  - [1.4.2](#142)
  - [1.4.1](#141)
  - [1.4](#14)
  - [1.3.1](#131)
  - [1.3](#13)
  - [1.2.1](#121)
  - [1.2](#12)
  - [1.1](#11)
  - [1.0.4](#104)
  - [1.0.3](#103)
  - [1.0.2](#102)
  - [1.0.1](#101)
  - [1.0](#10)

## 1.4.2

* creacion de ficheros vacíos para vault_pass en el post_install de *ohermosa*
* nuevos repositorios para clonar en el post_install de *ohermosa*
* se instala modulo de python `docker-py`
* documentación para el uso de cifrado de contraseñas en [README.md](README.md)

## 1.4.1

* Se mueve la lista de enlaces a crear en *post_install/environment* a lista de variables
* Se crea un nuevo enlace para cargar credenciales de `asgard` en el role *post_install*
* Se crea el directorio `$HOME/python-venv`
* Se incluyen los paquetes de desarrollo de python2 y python3 para instalar en common
* Se infiere la variable `ansible_user_dir` en todos los playbooks

## 1.4

* Instalación de `Cherrytree`
* CHANGELOG.md para registrar el historial de cambios para cada versión
* Uso del provider `virtualbox` para `vagrant` en lugar de `libvirt`
* Fix en el repositorio de `virtualbox` para `fedora`
* Fix en los box de `vagrant` para `fedora` y `ubuntu`
* Inventario dinámico para las máquinas de `vagrant`
* Borrardo de directorios predeterminados en el `$HOME` del usuario tras la instalación del sistema
* Actualizazción README con el comando para ver commits entre tags
* Instalación de la última versión de vagrant en ubuntu

## 1.3.1

* Corrección de errores en la instalación de docker, para **fedora** se estaba instalando virtualbox

## 1.3

* Instalación de codecs de autio y paquetes de utilidadeds
* Instalación de `deluge`
* Instalación de `chromium`

## 1.2.1

* Corregida la ruta de los repositorios para clonar en el post_install de **ohermosa**
* Corrección de errores en `post_install`
* Se corrige un problema con la variable `ansible_user` que no era consistente en todas las tasks

## 1.2

* Instalación de `franz`
* Instalación de `rambox`

## 1.1

* Instalación de `skype`
* Instalación de `postman`
* Instalación de `Java OpenJDK`
* Instalación de `Apache Directory Studio`
* post_install de `Apache Directory Studio` para **ohermosa**

## 1.0.4

* Correcciones en `Vagrantfile` y `README.md`

## 1.0.3

* Corrección de errores en la instalación de `Ether Cloud Services`
* Actualización de la versión de `No Machine` y corrección de errores en su instalación
* Se ha modificado el nombre de las tareas en el fichero *extra_software/tasks/main.yml*
* Corrección de errores en la instalación de `slack`
* Se han movido los playbooks para `vagrant` al subdirectorio *./vagrant*

## 1.0.2

* En **Ubuntu**, `ansible` se instala desde repositorio ppa en lugar de copiar el fichero del repositorio

## 1.0.1

* El repo de `virtualbox` se descarga de internet en lugar de generarse a partir de un template
* Se define la variable `virtualbox_packages` en base a la distribución usada y se incluyen dependencias para **Fedora**
* Se modifica la ruta a la llave privada ssh para que sea dinámica en lugar de ir a fuego
* Se documenta en el README.md cómo se usa Vagrant para pruebas

## 1.0

* Primera versión funcional
