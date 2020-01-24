# gitlab_repo

Esta tool crea/elimina repositorios en [Gitlab](https://gitlab.com/)

## Requisitos

El role puede recibir los siguientes parámetros:

| **PARÁMETRO** | **DESCRIPCIÓN** | **TIPO** | **OBLIGATORIO** |
|--|--|--|--|
| gitlab_token | token de acceso a **gitlab** con los permisos correctos | string | SÍ |
| repo_name | nombre del repositorio que se quiere crear o eliminar | string | SÍ |
| visibility | si es privado o público | string (default: __private__) | NO |
| repo_state | si debe crearse o borrarse | string (default: __present__) | NO
| issues_enabled | si se pueden crear issues | bool (default: __false__) | NO |
| wiki_enabled | si debe tener wiki | bool (default: __false__) | NO |

## Ejemplo

```yaml
```
