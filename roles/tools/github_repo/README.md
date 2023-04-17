# github_repo

Esta tool crea/elimina repositorios en [Github](https://github.com/)

## Requisitos

El role puede recibir los siguientes parámetros:

| **PARÁMETRO** | **DESCRIPCIÓN** | **TIPO** | **OBLIGATORIO** |
|--|--|--|--|
| github_token | token de acceso a **github** con los permisos correctos | string | SÍ |
| repo_name | nombre del repositorio que se quiere crear o eliminar | string | SÍ |
| repo_private | si es privado | bool (default: __true__) | NO |
| repo_state | si debe crearse o borrarse | string (default: __present__) | NO
| has_issues | si se pueden crear issues | bool (default: __false__) | NO |
| has_downloads | | bool (default: __false__) | NO |
| has_wiki | si debe tener wiki | bool (default: __false__) | NO |

## Ejemplo

```yaml
    - name: "Create github repositories"
      include_role:
        name: tools/github_repo
      vars:
        github_token: "{{ git_tokens.github }}"
        repo_name: "example_repo"
        repo_private: true
        repo_state: present
```
