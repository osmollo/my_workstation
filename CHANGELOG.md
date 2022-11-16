# CHANGELOG

- [CHANGELOG](#changelog)
  - [8.1](#81)
  - [8.0.2](#802)
  - [8.0.1](#801)
  - [8.0](#80)
  - [VERSIONES ANTERIORES](#versiones-anteriores)
    - [Versión 7](#versión-7)
    - [Versión 6](#versión-6)
    - [Versión 5](#versión-5)
    - [Versión 4](#versión-4)
    - [Versión 3](#versión-3)
    - [Versión 2](#versión-2)
    - [Versión 1](#versión-1)

## 8.1

- Instegración con [1Password](https://1password.com/sign-up/eu/)
- Soporte para [Fedora 37](https://getfedora.org/es/workstation/) y fin de soporte a versiones anteriores
- Eliminación de **ACT**
- Instalación por defecto de **Sublime Text** y **Sublime Merge**
- Modificación de la ruta del repositorio `my_workstation` en el directorio actual, de __HTTPS__ a __SSH__
- Corrección de errores:
  - Fixes para **Linux Mint**
  - Fixes al obtener la última version de varias apps

## 8.0.2

- Corrección de errores:
  - La versión de [Vivaldi](https://vivaldi.com/es/) estaba hardcodeada, ahora se instala mediante repositorio en **Ubuntu** y **Fedora**
  - Corregido el orden en la instalación de **Typora**
  - Eliminación de la plantilla `docker-ce.repo.j2`
  - La versión de **Virtualbox Extension Pack** ya no está hardcodeada sino que se lee de la url [https://download.virtualbox.org/virtualbox/LATEST.TXT](https://download.virtualbox.org/virtualbox/LATEST.TXT)

## 8.0.1

- Corrección de errores:
  - Cambio del directorio de entornos virtuales de python
  - Playbook `prepare_post.yml` hace pausa antes de desencriptar `main.yml.gpg` para que se pueda copiar el passphrase
  - Eliminación de repositorios git
  - Instalación por defecto de **Trivy**

## 8.0

- Integración completa y gestión de secretos con [Bitwarden](https://bitwarden.com/)
  - Ya no se usa `ansible-vault` para el cifrado de secretos
- **Secrethub** ya no se encuentra disponible para su instalación debido a su [fin de vida](https://secrethub.io/)
- Cambios en repositorios git
- Configuración de [Ubuntu PRO](https://discourse.ubuntu.com/t/ubuntu-pro-beta-tutorial/31018) en el role `post_install`
- En el role `post_install` ya no se configura `pass` ni `oracle_cloud`
- Corrección de errores:
  - `~/.env` renombrado como `~/.environment`
  - Limpieza entadas `insecure_registries` de `/etc/docker/daemon.json`
  - Refactor de la configuración de **Docker** en el role `post_install`

## VERSIONES ANTERIORES

### [Versión 7](changelog/v7.md)
### [Versión 6](changelog/v6.md)
### [Versión 5](changelog/v5.md)
### [Versión 4](changelog/v4.md)
### [Versión 3](changelog/v3.md)
### [Versión 2](changelog/v2.md)
### [Versión 1](changelog/v1.md)
