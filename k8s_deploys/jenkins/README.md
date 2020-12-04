[Documento original](https://www.digitalocean.com/community/tutorials/how-to-install-jenkins-on-kubernetes)

Creamos un namespace para jenkins

```bash
kubectl create namespace jenkins
```

Creamos el fichero [deploy.yml](./deploy.yml) con el siguiente contenido:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jenkins
spec:
  replicas: 1
  selector:
    matchLabels:
      app: jenkins
  template:
    metadata:
      labels:
        app: jenkins
    spec:
      containers:
      - name: jenkins
        image: jenkins/jenkins:lts
        ports:
          - name: http-port
            containerPort: 8080
          - name: jnlp-port
            containerPort: 50000
        volumeMounts:
          - name: jenkins-vol
            mountPath: /var/jenkins_vol
      volumes:
        - name: jenkins-vol
          emptyDir: {}
```

Y creamos el deployment:

```bash
kubectl create -f deploy.yml --namespace jenkins
```

Ahora creamos el fichero [service.yml](./service.yml) con el siguiente contenido:

```yaml
kind: Service
apiVersion: v1
metadata:
  name: jenkins-svc
spec:
  selector:
    app: jenkins
  ports:
  - protocol: TCP
    port: 8080
    targetPort: 8080
```

Y creamos el servicio:

```bash
kubectl create -f service.yml -n jenkins
```

Para acceder a jenkins, ejecutamos el siguiente comando:

```bash
kubectl -n jenkins port-forward service/jenkins-svc 8080:8080
```

Y en el navegador abrimos la url [http://localhost:8080](http://localhost:8080)

Nos pedirá contraseña de administrador, para lo que tenemos que ver los logs del pod de Jenkins:

```bash
kubectl logs pod/jenkins-794699f9bc-rzhvb
[...]
*************************************************************
*************************************************************
*************************************************************

Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

c867e88c87cb46678f4e50bfcafadf56

This may also be found at: /var/jenkins_home/secrets/initialAdminPassword

*************************************************************
*************************************************************
*************************************************************
[...]
```
