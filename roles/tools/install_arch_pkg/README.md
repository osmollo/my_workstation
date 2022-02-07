# install_arch_pkg

## Descripción

Este role sirve para instalar paquetes de **Arch Linux**. Los comandos equivalentes serían:

```bash
git clone {{ aur_url }}/{{ arch_package }}.git
cd {{ arch_package }}
makepkg -si --noconfirm
```

## Paquetes disponibles

Todos los paquetes que se pueden instalar con esta tool se encuentran en el **AUR** ([Arch User Repository](https://aur.archlinux.org/packages))

## Variables necesarias

| **Variable** | **Descripción** |
|--------------|-----------------|
| arch_package | Nombre del paquete de **Arch** que se desea instalar (tal cual aparece en la ruta del repositorio git correspondiente)|

## Ejemplo de uso

```yaml

- name: "[ARCH] install atom"
  import_role:
    name: tools/install_arch_pkg
  vars:
    arch_package: "atom-editor-bin"
```
