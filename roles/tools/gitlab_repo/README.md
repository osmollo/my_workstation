# gitlab_repo

Esta tool crea/elimina repositorios en [Gitea](https://gitea.com/)

## Requisitos

El role puede recibir los siguientes parámetros:

| **PARÁMETRO** | **DESCRIPCIÓN** | **TIPO** | **OBLIGATORIO** |
|--|--|--|--|
| gitea_token | token de acceso a **gitlab** con los permisos correctos | string | SÍ |
| repo_name | nombre del repositorio que se quiere crear o eliminar | string | SÍ |
| visibility | si es privado o público | string (default: __private__) | NO |
| repo_state | si debe crearse o borrarse | string (default: __present__) | NO
