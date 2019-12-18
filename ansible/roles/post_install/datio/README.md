# post_install/datio

## Acciones disponibles

| **TAG** | **DESCRIPCIÓN** | **REQUIERE `ask-vault-pass`** |
|---------|-----------------|-------------------------------|
| **post_del_default_dirs** | Borra los directorios predeterminados en `$HOME` que se crean en la instalación | |
| **post_gnome_extensions** | Instala extensiones de Gnome disponibles en el repositorio | |
| **post_docker** | Restaura de **Dropbox** los login en repositorios de Docker y la configuración del demonio `docker` | |
| **post_git** | Clona los repositorios indicados en el fichero de variables y configura el `user.email` y `user.name` en cada uno de ellos | |
| **post_network** <br> **post_vpn** | Genera las configuraciones para las conexiones de red | :lock: |
| **post_code** | Instalación de extensiones básicas de `Visual Studio Code` | |
| **post_env** <br> **post_environment** | Configura parámetros del entorno de usuario | :lock: |

## Ejemplo de uso

```bash
ansible-playbook post_install.yml -t post_git -e post_install_user=datio

ansible-playbook post_install.yml -t post_network -e post_install_user=datio --ask-vault-pass
```
