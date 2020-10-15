# post_install

- [post_install](#post_install)
  - [Propósito](#propósito)
  - [Gestión de contraseñas](#gestión-de-contraseñas)
    - [Ficheros locales](#ficheros-locales)
    - [Ansible Vault](#ansible-vault)
      - [Fichero de contraseñas](#fichero-de-contraseñas)
      - [Contraseñas cifradas](#contraseñas-cifradas)
  - [GPG](#gpg)
    - [Creación claves GPG](#creación-claves-gpg)
    - [Encriptación `defaults/main.yml`](#encriptación-defaultsmainyml)
    - [Desencriptación `defaults/main.yml`](#desencriptación-defaultsmainyml)

## Propósito

Dentro de este directorio, se creará un subdirectorio con el nombre del usuario que ejecuta el playbook para que al ejecutar el playbook `post_install.yml` se ejecuten las tareas desarrolladas en el mismo

```bash
ansible-playbook post_install.yml
```

## Gestión de contraseñas

Tanto en el directorio `defaults` como `vars` dentro del directorio de cada usuario, se definen las variables necesarias para la ejecución de las tareas. Estas variables pueden tener contenido sensible por lo que será necesario cifrarlas con `ansible-vault` puesto que el contenido del repositorio es público.

### Ficheros locales

Las contraseñas se pueden definir como variables en ficheros *"yml"* al igual que el resto de variables pero sin estar bajo el seguimiento de **git**. Para ello no es necesario tenerlo fuera del directorio del repositorio sino que basta con incluír el nombre del fichero donde tengamos las contraseñas en un fichero *.gitignore*.

```text
post_install
├── dsamaniego
    ├── secrets
    │   └── main.yml
```

Para usar el fichero de contraseñas, habrá que usar la siguiente tarea de Ansible:

```yaml
- name: "include secrets file"
  include_vars:
    file: "secrets/main.yml"
```

Podedmos incluír la ruta al *main.yml* en el *.gitignore* que hay en el raíz o crear uno nuevo en el mismo direscorio secrets:

```bash
cat roles/post_install/dsamaniego/.gitignore
secrets/main.yml
```

La ventaja de este método es que mantenemos las contraseñas fuera de **git** pero con la contrapartida de que el fichero es local, si en algún momento se clona el repositorio en otra máquina, habrá que copiar manualmente este fichero a ese ordenador. **Ojo cuidado**, que el fichero es local pero tendría las contraseñas en texto plano!

### Ansible Vault

Para las siguientes opciones, es necesario indicar que se pida la contraseña de descifrado al ejecutar el playbook usando el flag `--ask-vault-pass`.

Es posible evitar esta incomodidad (hay que teclear la contraseña en cada ejecución del playbook), creando un fichero `$HOME/.vault_pass.txt` con la contraseña en texto plano (hay que dar permisos 600 al fichero para más seguridad) y declarando la variable `ANSIBLE_VAULT_PASSWORD_FILE` con la ruta de ese fichero:

```bash
echo "mi_contraseña" > $HOME/.vault_pass.txt
export ANSIBLE_VAULT_PASSWORD_FILE=$HOME/.vault_pass.txt
```

Con esto, ya no sería necesario incluir el flag `--ask-vault-pass`. Al finalizar la ejecución del playbook puede borrarse el fichero sin problema

#### Fichero de contraseñas

Vault tiene una herramienta `ansible-vault` que permite cifrar ficheros (con AES256) donde almacenar contraseñas. El formato de estos ficheros es exactamente el mismo que otros donde se almacenan variables solo que hay que cifrarlo/descifrarlo para su uso con una contraseña que se establece en el momento de su creación.

```bash
ansible-vault secrets/main.yml create
New Vault password:
Confirm New Vault password:
```

Si hacemos un cat del fichero, no podremos ver el contenido:

```txt
cat secrets/main.yml
$ANSIBLE_VAULT;1.1;AES256
64643661633666333836396338656364383734636638626332623166656335623964616462616263
6237326165336231333037343136353664396265356635630a333231333238323863303832336661
30626366353162613539623962363264363532323934663862373136363163656537666533373833
6437346566356639360a666463643338656235393866626439353034336435663032643764393330
63626332616533303338396339653963633261326336353231393863623335346532
```

Para usar este fichero de variables, habría que usar la misma tarea de Ansible que en el caso anterior:

```yaml
- name: "include secrets file"
  include_vars:
    file: "secrets/main.yml"
```

Y para ejecutar el playbook hay que agregar el parámetro `--ask-vault-pass` para que pueda descrifrar el fichero de contraseñas:

```bash
ansible-playbook install.yml -e "post_user=dsamaniego"  --ask-vault-pass
```

Para editar el fichero habría que usar el siguiente comando (o bien instalar alguna extensión en el editor de textos que permita trabajar con estos ficheros)

```bash
ansible-vault secrets/main.yml edit
Vault password:
```

La ventaja de este método es que podemos tener las contraseñas cifradas bajo el control de git sin riesgos de seguridad ya que no pueden ser vistas por otros usuarios

#### Contraseñas cifradas

Otra opción haciendo uso de `ansible-vault` es cifrar contraseñas con esta herramienta y pegar el hash dentro del fichero *defaults/main.yml* del role. Para ello, para cifrar una cadena de texto (la contraseña), hay que ejecutar el siguiente comando:

```bash
ansible-vault encrypt_string ceporro
New Vault password:
Confirm New Vault password:
!vault |
          $ANSIBLE_VAULT;1.1;AES256
          35393661323635626162626262626537626465313232666537616134353532376536363537366533
          3138343938353264346662333561333362653661376564370a343735373865613536356538393137
          62326139303938323664303432336164383732643735636536326365373733363066336565666536
          6161343931623434640a386664336236373035623466613839333339333733346264663861393364
          3937
Encryption successful
```

La salida del anterior comando se debe copiar dentro del fichero **defaults/main.yml** con el siguiente formato:

```yaml
ceporro: !vault |
  $ANSIBLE_VAULT;1.1;AES256
  35393661323635626162626262626537626465313232666537616134353532376536363537366533
  3138343938353264346662333561333362653661376564370a343735373865613536356538393137
  62326139303938323664303432336164383732643735636536326365373733363066336565666536
  6161343931623434640a386664336236373035623466613839333339333733346264663861393364
  3937
```

Para poder descrifrar esta contraseña al ejecutar el playbook, habrá que incluír el argumento `--ask-vault-pass` e indicar la contraseña que se usó en el paso anterior para cifrar la password:

```bash
ansible-playbook install --ask-vault-pass
```

## GPG

Como segunda capa de seguridad, se puede encriptar con [GPG](https://gnupg.org/) los ficheros con contraseñas.

### Creación claves GPG

Para generar un par de claves público/privada habrá que seguir [este howto](https://www.redhat.com/sysadmin/creating-gpg-keypairs)

### Encriptación `defaults/main.yml`

```bash
rm -fr roles/post_install/ohermosa/defaults/main.yml.gpg
gpg --output roles/post_install/ohermosa/defaults/main.yml.gpg --encrypt --recipient ohermosa@gmail.com roles/post_install/ohermosa/defaults/main.yml
```

### Desencriptación `defaults/main.yml`

```bash
rm -fr roles/post_install/ohermosa/defaults/main.yml
gpg --output roles/post_install/ohermosa/defaults/main.yml --decrypt roles/post_install/ohermosa/defaults/main.yml.gpg
```
