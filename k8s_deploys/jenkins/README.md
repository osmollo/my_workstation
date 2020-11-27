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
  type: NodePort
  selector:
    app: jenkins
  ports:
  - protocol: TCP
    port: 8080
    targetPort: 8080
    nodePort: 30000
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
