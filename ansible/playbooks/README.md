# playbooks

- [playbooks](#playbooks)
  - [get_secret.yml](#get_secretyml)
  - [delete_repos.yml](#delete_reposyml)
  - [update_packages.yml](#update_packagesyml)
  - [update_ansible.yml](#update_ansibleyml)
  - [load_distro_vars.yml](#load_distro_varsyml)
  - [kde_backup.yml](#kde_backupyml)

## get_secret.yml

Para obtener el valor de una variable que esté encriptada en cualquiera de los subdirectorios `defaults` o `vars` del repositorio

```bash
ansible-playbook playbooks/get_secret.yml -e secret=github_token_access --ask-vault-pass
```

## delete_repos.yml

Elimina los repositorios en **github**, **gitlab** o ambos que hay definidos en el playbook

```bash
ansible-playbook playbooks/delete_repos.yml -e git_target=github
```

## update_packages.yml

Actualiza los paquetes del sistema operativo.

```bash
ansible-playbook playbooks/update_packages.yml
```

## update_ansible.yml

Actualiza la versión de **Ansible** usando los repositorios oficiales

```bash
ansible-playbook playbooks/update_ansible.yml
```

## load_distro_vars.yml

Define las variables `linux_distribution` y `desktop_environment` que se usan en el repositorio.

```bash
ansible-playbook playbooks/load_distro_vars.yml
```

## kde_backup.yml

Realiza una copia de seguridad de la configuración de **KDE**. Ejecuta las tareas del fichero `post_install/$USER/tasks/kde_backup.yml`

```bash
ansible-playbook playbooks/kde_backup.yml
```
