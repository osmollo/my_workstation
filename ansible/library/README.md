# library

- [library](#library)
  - [dconf_to_list](#dconf_to_list)
    - [INPUT](#input)
    - [OUTPUT](#output)
    - [Ejemplo de uso](#ejemplo-de-uso)
  - [github_repo](#github_repo)
    - [Ejemplo de uso](#ejemplo-de-uso-1)
  - [gitlab_repo](#gitlab_repo)
    - [Ejemplo de uso](#ejemplo-de-uso-2)
  - [yay](#yay)
    - [Ejemplo de uso](#ejemplo-de-uso-3)

## dconf_to_list

Este módulo sirve para parsear la configuración de **Gnome** generada con el comando `dconf dump /` a una lista de diccionarios que pueda ser importada con el módulo `dconf` de ansible

### INPUT

Al módulo se le debe pasar **obligatoriamente** el parámetro `dconf_file`, con la ruta al fichero de la configuración de Gnome. Este fichero se obtiene ejecutando:

```bash
dconf dump / > gnome_config.txt
```

Y tiene el siguiente formato:

```text
[system/proxy]
autoconfig-url='http://bbvapac.igrupobbva/accelerated_pac_base.pac'
mode='auto'

[/org/gnome/settings-daemon/peripherals/keyboard]
numlock-state='on'
```

En él se indica, para cada ruta, una serie de llaves-valor para la configuración de **Gnome** y diversas aplicaciones. No es necesario restaurar la configuración de todas las rutas obtenidas, por lo que en el parámetro `paths_to_restore` se pueden especificar las que se desean parsear.

La forma de invocar el módulo sería así:

```yaml
- name: "Parse dconf dump"
  dconf_to_list:
    dconf_file: "{{ dropbox_dir }}/datio/gnome_config"
    paths_to_restore: "{{ dconf_paths_to_restore }}"
```

### OUTPUT

La ejecución del módulo devuelve una lista de diccionarios con los campos `key` y `value` correspondientes a la configuración leída de `dconf_file`. Esta lista se puede usar para alimentar el módulo `dconf` de Ansible y así restaurar la configuración.

Un ejemplo de salida de `dconf_to_list` sería:

```json
    [
        {
            "key": "/system/proxy/autoconfig-url",
            "value": "'http://bbvapac.igrupobbva/accelerated_pac_base.pac'"
        },
        {
            "key": "/system/proxy/mode",
            "value": "'auto'"
        },
        {
            "key": "/org/gnome/settings-daemon/peripherals/keyboard/numlock-state",
            "value": "'on'"
        }
    ]
```

### Ejemplo de uso

```yaml
- name: "Parse dconf dump"
  dconf_to_list:
    dconf_file: "{{ dropbox_dir }}/datio/gnome_config"
    paths_to_restore: "{{ dconf_paths_to_restore }}"
  register: response

- name: "Import gnome config"
  dconf:
    key: "{{ item.key }}"
    value: "{{ item.value }}"
  loop: "{{ response.message }}"
```

## github_repo

Este módulo crea o elimina un repositorio en [Github](https://www.github.com)

### Ejemplo de uso

```yaml
- github_repo:
    github_auth_key: "{{ github_token }}"
    name: "{{ repo_name }}"
    private: "{{ repo_private | default(true) }}"
    has_issues: "{{ has_issues | default(false) }}"
    has_wiki: "{{ has_wiki | default(false) }}"
    has_downloads: "{{ has_downloads | default(false) }}"
    state: "{{ repo_action | default(present) }}"
  register: result
```

## gitlab_repo

Este módulo crea o elimina un repositorio en [Gitlab](https://www.gitlab.com)

### Ejemplo de uso

```yaml
- gitlab_repo:
    gitlab_auth_key: "{{ gitlab_token }}"
    name: "{{ repo_name }}"
    private: "{{ repo_private | default(true) }}"
    has_issues: "{{ has_issues | default(false) }}"
    has_wiki: "{{ has_wiki | default(false) }}"
    has_downloads: "{{ has_downloads | default(false) }}"
    state: "{{ repo_action | default(present) }}"
  register: result
```

## yay

**Documentación**: [Official Repo](https://github.com/mnussbaum/ansible-yay)

### Ejemplo de uso

```yaml
- name: "[ARCH] Install virtualbox"
  become: false
  yay:
    name: "{{ virtualbox_package }}"
    state: present
    update_cache: true
```
