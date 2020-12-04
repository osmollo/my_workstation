[Documento original](https://www.digitalocean.com/community/tutorials/how-to-install-nexus-on-kubernetes)

Creamos un namespace para nexus

```bash
kubectl create namespace nexus
```

Creamos el fichero [deploy.yml](./deploy.yml) con el siguiente contenido:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nexus
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nexus
  template:
    metadata:
      labels:
        app: nexus
    spec:
      containers:
      - name: nexus
        image: sonatype/nexus3:3.28.1
        ports:
          - name: http-port
            containerPort: 8081
        volumeMounts:
          - name: nexus-vol
            mountPath: /var/nexus_vol
      volumes:
        - name: nexus-vol
          emptyDir: {}
```

Y creamos el deployment:

```bash
kubectl create -f deploy.yml --namespace nexus
```

Ahora creamos el fichero [service.yml](./service.yml) con el siguiente contenido:

```yaml
kind: Service
apiVersion: v1
metadata:
  name: nexus-svc
spec:
  selector:
    app: nexus
  ports:
  - protocol: TCP
    port: 8081
    targetPort: 8081
```

Y creamos el servicio:

```bash
kubectl create -f service.yml -n nexus
```

Para acceder a nexus, ejecutamos el siguiente comando:

```bash
kubectl port-forward service/nexus-svc 8081:8081
```

Y en el navegador abrimos la url [http://localhost:8081](http://localhost:8081)
