# Docker + Consul + Vault

Usar `docker-compose` para desplegar una instancia de `vault` con backend de `consul`

*Fuente*: [www.marcolancini.it](https://www.marcolancini.it/2017/blog-vault/)

![Vault UI](https://www.marcolancini.it/images/posts/blog_vault_2.jpg)

## Uso

### Prerequisitos

Para generar el certificado de **Vault**: `openssl req -newkey rsa:2048 -nodes -keyout vault.key -x509 -days 365 -out vault.pem`

### Primera Ejecución

1. Levantar servicios: `docker-compose up`
2. Iniciar Vault:     `./_scripts/setup.sh`
3. Parar servicios:      `docker-compose down`

Los datos serán persistidos en el direcotrio `_data`

### Siguientes ejecuciones

1. Iniciar Servicios: `docker-compose up`
2. Unseal vault:   `_scripts/unseal.sh`

### Backup

1. Iniciar servicios: `docker-compose up`
2. Ejecutar backup:     `_scripts/backup.sh`

### Borrar todos los datos

1. Parar servicios: `docker-compose down --volumes`
2. Limpiar persistencias: `_scripts/clean.sh`
