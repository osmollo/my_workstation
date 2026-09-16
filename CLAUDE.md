# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Qué es esto

Repositorio de bootstrap/configuración de estación de trabajo Linux basado en **Ansible**. No es una app o librería: los cambios aquí modifican el estado real de la máquina donde se ejecuta (paquetes, dotfiles, credenciales, configuración de escritorio), no un sandbox. Todos los playbooks corren contra `hosts: localhost` con `connection: local`.

`AGENTS.md` en la raíz ya documenta el contrato de este repo en detalle (wiring, comandos, gotchas) — léelo, es la referencia principal. Este fichero añade contexto complementario.

## Comandos principales

```shell
# Instalación base (paquetes comunes + software de terceros)
ansible-playbook install.yml

# Instalación de una app concreta por tag (coincide con la variable install_<tag>)
ansible-playbook install.yml -t "vscode,dropbox,spotify"

# Instalación de todo excepto ciertas apps
ansible-playbook install.yml -e "install_spotify=false install_ohmyzsh=false"

# Post-instalación personal (requiere sesión de 1Password activa: eval $(op signin))
ansible-playbook playbooks/prepare_post.yml
ansible-playbook post_install.yml

# Configuración de trabajo (mismo flujo que post_install)
ansible-playbook playbooks/prepare_post.yml
ansible-playbook work.yml

# Deshabilitar la actualización de paquetes del sistema en una ejecución
REPO_DISABLE_UPDATES=1 ansible-playbook install.yml
# o
ansible-playbook install.yml -e disable_updates=true
```

Verificación en CI (`.github/workflows/ansible-check.yml`): `ansible-playbook --syntax-check` sobre `install.yml`, `post_install.yml`, `work.yml`; y `ansible-lint --offline` sobre esos playbooks más `playbooks/` y `roles/` (usa `.github/ansible-lint.cfg`, que fija `roles_path` e `interpreter_python`; el `.ansible-lint` de la raíz excluye `library/`). No hay wrapper de test propio del repo: la forma de verificar un cambio es un `ansible-playbook` acotado por tag sobre el entrypoint más pequeño posible (p. ej. `ansible-playbook install.yml -t ssh_config --check`).

## Arquitectura

- **Entrypoints**: `install.yml` (paquetes base + software extra), `post_install.yml` (config personal), `work.yml` (config de trabajo). Los dos últimos dependen de `playbooks/prepare_post.yml` (importa claves GPG y desencripta los `.gpg` correspondientes) y de una sesión de 1Password activa (verificada por `playbooks/check_op.yml`, que exige `OP_SESSION_*` en el entorno y que `op account get` funcione).
- **Runtime wiring** (`ansible.cfg`): módulos custom en `./library`, helpers compartidos en `./module_utils`, lookup plugins en `./lookup_plugins`. No mover/renombrar estas rutas sin actualizar `ansible.cfg`.
- **Resolución de distro/escritorio**: `playbooks/load_distro_vars.yml` define los hechos `linux_distribution` y `desktop_environment` que consumen la mayoría de roles/tasks condicionales. Es un `import_playbook` con tag `always` en los tres entrypoints principales.
- **Roles** (`roles/`):
  - `common`: paquetes base de la distro, flujo de actualización de sistema, shells, cliente SSH. La actualización de paquetes es *stateful*: `roles/common/tasks/update_packages.yml` usa `/var/tmp/.update` con un check de antigüedad de una semana, así que el comportamiento puede variar entre ejecuciones idénticas.
  - `extra_software`: instalación de software de terceros por categoría; cada app se activa/desactiva con una variable `install_*` en `roles/extra_software/defaults/main.yml` y comparte el mismo nombre como tag.
  - `post_install`: personalización de usuario/escritorio tras el bootstrap (dotfiles, gnome/kde, git, gpg, shells...).
  - `work`: configuración específica de trabajo (clonado de repos, docker, odbc, etc.), estructura paralela a `post_install`.
  - `tools`: roles reutilizables invocados desde otros roles (crear alias, clonar repos, crear remotos en github/gitlab, instalar paquetes AUR, leer items de 1Password).
- **Secretos y ficheros generados**: `roles/post_install/defaults/main.yml.gpg` y `roles/work/defaults/main.yml.gpg` están versionados cifrados; `prepare_post.yml` los desencripta a `main.yml` (gitignored). `post_install.yml`/`work.yml` fallan explícitamente (`fail:`) si el `main.yml` correspondiente no existe todavía. No editar ni commitear esos `main.yml` desencriptados.
- **Módulos custom** (`library/*.py`): scrapers/wrappers para obtener últimas versiones de software (1Password, Go, NoMachine, Zoom, Terraform, Dropbox...) y para gestionar repos en GitHub/GitLab. Documentados con ejemplos en `library/README.md`.
- **Otros playbooks** (`playbooks/`): utilidades independientes — `delete_repos.yml` (borra repos en github/gitlab), `update_packages.yml`, `update_ansible.yml`, `kde_backup.yml`/`restore_desktop_config.yml`. Documentados en `playbooks/README.md`.
- **Changelog**: `CHANGELOG.md` se genera manualmente con `git log --pretty=oneline <tag_antiguo> <tag_nuevo>`; el release en GitHub (`.github/workflows/new_release.yml`) se dispara al modificar `release.json`/`CHANGELOG.md` en `master` y extrae automáticamente la sección correspondiente a la versión de `release.json`.

## Gotchas

- En distros Debian, la ejecución puede fallar pronto si el usuario no tiene sudo; `load_distro_vars.yml` indica ejecutar `playbooks/debian_sudo.yml` y reloguear.
- `install.yml` puede modificar `.git/config` (remote origin) y `~/.ssh/config` (IdentityAgent de 1Password) como `post_tasks`; evitar ejecuciones amplias cuando un run acotado por tag basta para verificar un cambio.
