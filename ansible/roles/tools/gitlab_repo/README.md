# gitlab_repo

Esta tool crea/elimina repositorios en [Gitlab](https://gitlab.com/)

## Requisitos

El role puede recibir los siguientes parámetros:

| **PARÁMETRO** | **DESCRIPCIÓN** | **TIPO** | **OBLIGATORIO** |
|--|--|--|--|
| gitlab_token | token de acceso a **gitlab** con los permisos correctos | string | SÍ |
| repo_name | nombre del repositorio que se quiere crear o eliminar | string | SÍ |
| repo_private | si es privado | bool (default: __true__) | NO |
| repo_action | si debe crearse o borrarse | string (default: present) | NO
| has_issues | si se pueden crear issues | bool (default: false) | NO |
| has_downloads | | bool (default: false) | NO |

## Ejemplo

```yaml
```
