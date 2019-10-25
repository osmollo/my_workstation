# common

- [common](#common)
  - [Acciones disponibles](#acciones-disponibles)

## Acciones disponibles

| **TAG** | **DESCRIPCIÓN** |
|------------|--------------|
| **common** | Ejecuta el role completo |
| **update_packages** | Actualiza todos los paquetes de la distribución |
| **install_packages** | Instala paquetes de los repositorios definidos en las variables |
| **ansible** | Instala la última versión de `Ansible` disponible |
| **python**/**python3** | Instala `Python3` y lo configura como intérprete por defecto de Python |
| **disable_selinux** | Deshabilita SElinux en Fedora |
| **delete_snap** | En **Ubuntu**, desinstala paquetes del sistema instalados con snap y los instala desde los repositorios |
| **resolv** | Añade a `/etc/hosts` las entradas definidas en las variables |
| **bash_history_size** | Añade a `/etc/profile` la configuración de historial de Bash |
