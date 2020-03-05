# create_remote

Esta tool crea remotos de git

## Requisitos

El role puede recibir los siguientes parámetros:

| **PARÁMETRO** | **DESCRIPCIÓN** | **TIPO** | **OBLIGATORIO** |
|--|--|--|--|
| remote.name | nombre del remote | string | SÍ |
| remote.url | url del remoto | string | SÍ |
| remote.directory | directorio local del repositorio donde crear el remoto |string | SÍ |
| repo_state | si debe crearse o borrarse | string (default: __present__) | NO

## Ejemplo

```yaml
    - name: "Create remote"
      include_role:
        name: tools/create_remote
      vars:
        remote:
          name: my_workstation
          url: git@gitlab.com:balzar/my_workstation.git
          directory: "{{ ansible_user_dir }}/git/my_workstation"
```
