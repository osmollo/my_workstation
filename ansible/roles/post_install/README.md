# Post Instalación

El role `post_install` tiene como objetivo terminar de configurar el entorno, personalizándolo como prefiera el usuario. Dentro del directorio del role debe ir un subdirectorio con el nombre del usuario. Cuando se ejecute el playbook `post_install.yml`, si no se indica el usuario mediante `extravars` con la variable `post_install_user`, se usará el usuario del sistema que ha ejecutado el playbook (usando la variable de entorno `$USER`)

```bash
ansible-playbook post_install.yml
```

Ó

```bash
ansible-playbook post_install.yml -e "post_install_user=ohermosa"
```

Un ejemplo de cómo debe ser la jerarquía de directorios del role `post_install` es el siguiente:

```text
├── datio
│   ├── defaults
│   │   └── main.yml
│   ├── files
│   │   ├── bancomer.p12
│   │   ├── bbva.p12
│   │   ├── datio.p12
│   │   ├── docker.config.json
│   │   └── gnome_extensions.tar.gz -> ../../ohermosa/files/gnome_extensions.tar.gz
│   ├── README.md
│   ├── tasks
│   │   ├── docker.yml
│   │   ├── gnome_extensions.yml
│   │   ├── main.yml
│   │   └── network.yml
│   ├── templates
│   │   ├── bancomer.ovpn.j2
│   │   ├── bancomer_vpn.j2
│   │   ├── bbva.ovpn.j2
│   │   ├── bbva_vpn.j2
│   │   ├── daemon.json.j2
│   │   └── datio.ovpn.j2
│   └── vars
│       └── secrets.yml
├── ohermosa
│   ├── defaults
│   │   └── main.yml
│   ├── files
│   │   ├── gimp_menurc
│   │   ├── gimp_sessionrc
│   │   └── gnome_extensions.tar.gz
│   ├── README.md
│   ├── tasks
│   │   ├── crontab.yml
│   │   ├── docker.yml
│   │   ├── environment.yml
│   │   ├── firefox.yml
│   │   ├── gimp.yml
│   │   ├── git.yml
│   │   ├── gnome_conf.yml
│   │   ├── gnome_extensions.yml
│   │   ├── gpg.yml
│   │   ├── hp.yml
│   │   ├── kde_backup.yml
│   │   ├── kde_restore.yml
│   │   ├── main.yml
│   │   ├── megacmd.yml
│   │   ├── network.yml
│   │   ├── secrets.yml
│   │   ├── sublime.yml
│   │   └── vim.yml
│   └── templates
│       ├── bbva_vpn.j2
│       └── datio_mx_vpn.j2
└── README.md
```

En la [configuarción de **ansible**](../../ansible.cfg) se establece la variable `become_ask_pass` a _True_ para que se solicite siempre la contraseña de sudo para ejecutar las tareas con permiso de _root_. Sin embargo, en este role muchas de las tareas, puesto que se trata de configuraciones de usuario, no requieren dichos permisos. El role debe ejecutarse en _plays_ sin permisos de root y asignarlos en las tareas que lo necesiten:

```yaml
- hosts: localhost
  connection: local
  vars:
    ansible_user: "{{ lookup('env', 'USER') }}"
    ansible_user_dir: "/home/{{ lookup('env', 'USER') }}"
    post_user: "{{ post_install_user | default(ansible_user) }}"
  roles:
    - "post_install/{{ post_user }}"

[...]

- name: "Create directory /var/spool/cron/crontabs if not exists"
  file:
    path: /var/spool/cron/crontabs
    state: directory
  when: not crontabs_exists.stat.exists
  become: true
  become_method: sudo
```
