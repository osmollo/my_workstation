# playbooks

- [playbooks](#playbooks)
  - [delete_repos.yml](#delete_reposyml)
  - [update_packages.yml](#update_packagesyml)
  - [update_ansible.yml](#update_ansibleyml)
  - [load_distro_vars.yml](#load_distro_varsyml)
  - [kde_backup.yml](#kde_backupyml)
  - [restore_desktop_config.yml](#restore_desktop_configyml)
  - [prepare_post.yml](#prepare_postyml)

## delete_repos.yml

Elimina los repositorios en **github**, **gitlab** o ambos que hay definidos en el playbook

```shell
ansible-playbook playbooks/delete_repos.yml -e git_target=github
```

## update_packages.yml

Actualiza los paquetes del sistema operativo.

```shell
ansible-playbook playbooks/update_packages.yml
```

## update_ansible.yml

Actualiza la versión de **Ansible** usando los repositorios oficiales

```shell
ansible-playbook playbooks/update_ansible.yml
```

## load_distro_vars.yml

Define las variables `linux_distribution` y `desktop_environment` que se usan en el repositorio.

```shell
ansible-playbook playbooks/load_distro_vars.yml
```

## kde_backup.yml

Realiza una copia de seguridad de la configuración de **KDE**. Ejecuta las tareas del fichero `post_install/$USER/tasks/kde_backup.yml`

```shell
ansible-playbook playbooks/kde_backup.yml
```

## restore_desktop_config.yml

Este playbook restaura la configuración de usuario

```shell
ansible-playbook playbooks/restore_desktop_config.yml
```

## prepare_post.yml

Este playbook importa las claves GPG y desencripta el fichero `roles/post_install/defaults/main.yml.gpg`

```shell
ansible-playbook playbooks/prepare_post.yml
```
