# Post Instalación

El role `post_install` tiene como objetivo terminar de configurar el entorno personalizándolo como prefiera el usuario. Dentro del directorio del role, debe ir un subdirectorio con el nombre del usuario que también se pasará como variable a través de `extravars` con la variable `post_install_user`:

```bash
ansible-playbook post_install.yml -e "post_install_user=ohermosa"
```

Un ejemplo de cómo debe ser la jerarquía de directorios del role `post_install` es el siguiente:

```text
post_install
├── dsamaniego
│   ├── defaults
│   │   └── main.yml
│   ├── tasks
│   │   ├── main.yml
│   │   └── maki.yml
│   └── templates
│       └── burrito.j2
└── ohermosa
    ├── defaults
    │   └── main.yml
    ├── tasks
    │   ├── crontab.yml
    │   ├── docker.yml
    │   ├── environment.yml
    │   ├── git.yml
    │   ├── main.yml
    │   └── openvpn.yml
    └── templates
        ├── bbva_vpn.j2
        └── datio_mx_vpn.j2
```

Puesto que muchas de las tareas que se ejecutan dentro de este role están orientadas a la configuración personalizada de cada usuario, seguramente no sea necesario ejecutar todas ellas como superusuario. Por ello, el playbook [post_install](../post_install.yml) se ejecuta como usuario normal y se deja a cada una de las tareas la opción de ejecutarse o no con permisos de administrador.

```yaml
- import_tasks: git.yml
  when: dropbox_response.stdout == "Actualizado"
  tags:
    - post_install
    - post_git

- import_tasks: vpn.yml
  become: true
  become_method: sudo
  tags:
    - post_install
    - post_vpn
```
