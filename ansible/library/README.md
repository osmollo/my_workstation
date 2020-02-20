# library

- [library](#library)
  - [dconf_to_list](#dconf_to_list)
    - [INPUT](#input)
    - [OUTPUT](#output)
    - [Ejemplo de uso](#ejemplo-de-uso)
  - [get_go_latest](#get_go_latest)
    - [Ejemplo de uso](#ejemplo-de-uso-1)
  - [get_nomachine_latest](#get_nomachine_latest)
    - [Ejemplo de uso](#ejemplo-de-uso-2)
  - [github_repo](#github_repo)
    - [Ejemplo de uso](#ejemplo-de-uso-3)
  - [gitlab_repo](#gitlab_repo)
    - [Ejemplo de uso](#ejemplo-de-uso-4)
  - [yay](#yay)
    - [Ejemplo de uso](#ejemplo-de-uso-5)
  - [protonvpn_fastest](#protonvpn_fastest)
    - [Ejemplo de uso](#ejemplo-de-uso-6)

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

## get_go_latest

Este módulo parsea la [web de `GO`](https://golang.org/dl) para devolver cuál es la última versión estable de `GO`

### Ejemplo de uso

```yaml
- name: "get go version"
  get_go_latest:
  register: go_response

- debug: var=go_response.version
```

## get_nomachine_latest

Este módulo parsea la [web de `NoMachine`](https://www.nomachine.com/download/download&id=5) para devolver cuál es la última versión estable de `NoMachine`

### Ejemplo de uso

```yaml
- name: "get nomachine version"
  get_nomachine_latest:
  register: nomachine_response

- debug: var=nomachine_response.version
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
    state: "{{ repo_state | default(present) }}"
  register: result
```

## gitlab_repo

Este módulo crea o elimina un repositorio en [Gitlab](https://www.gitlab.com)

### Ejemplo de uso

```yaml
- gitlab_repo:
    gitlab_auth_key: "{{ gitlab_token }}"
    name: "{{ repo_name }}"
    visibility: "{{ visibility | default(private) }}"
    issues_enabled: "{{ issues_enabled | default(false) }}"
    wiki_enabled: "{{ wiki_enabled | default(false) }}"
    state: "{{ repo_state | default(present) }}"
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

## protonvpn_fastest

### Ejemplo de uso

```yaml
- uri:
    url: https://api.protonvpn.ch/vpn/logicals
    register: uri_response

- protonvpn_fastest:
    servers: '{{ uri_response.json["LogicalServers"] }}'
    tier: 0
    register: fastest_response

- debug: var=fastest_response.fastest
```
