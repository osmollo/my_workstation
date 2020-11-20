Creamos un namespace para Wordpress:

```bash
kubectl create namespace wordpress
```

Creamos el fichero [mysql-deploy.yml](./mysql-deploy.yml) con el siguiente contenido:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mysql-svc
  labels:
    app: wordpress
spec:
  ports:
    - port: 3306
  selector:
    app: wordpress
  clusterIP: None

---

apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: mysql
  labels:
    app: wordpress
spec:
  selector:
    matchLabels:
      app: wordpress
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: wordpress
    spec:
      containers:
      - image: mysql:5.6
        name: mysql
        env:
        - name: MYSQL_ROOT_PASSWORD
          value: password1234
        ports:
        - containerPort: 3306
          name: mysql
        volumeMounts:
        - name: mysql-persistent-storage
          mountPath: /var/lib/mysql
      volumes:
        - name: mysql-persistent-storage
          emptyDir: {}
```

Y lo desplegamos:

```bash
kubectl -n wordpress apply -f mysql-deploy.yml
```

Ahora creamos el fichero [wordpress-deploy.yml](./wordpress-deploy.yml) con el siguiente contenido:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: wordpress-svc
  labels:
    app: wordpress
spec:
  ports:
    - port: 80
      targetPort: 80
      nodePort: 31000
  selector:
    app: wordpress
  type: NodePort

---

apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: wordpress
  labels:
    app: wordpress
spec:
  selector:
    matchLabels:
      app: wordpress
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: wordpress
    spec:
      containers:
      - image: wordpress:4.8-apache
        name: wordpress
        env:
        - name: WORDPRESS_DB_HOST
          value: mysql-svc
        - name: WORDPRESS_DB_PASSWORD
          value: password1234
        ports:
        - containerPort: 80
          name: wordpress
```

Y lo desplegamos:

```bash
kubectl -n wordpress apply -f wordpress-deploy.yml
```

Vemos los objetos que se han creado:

```bash
kubectl -n wordpress get all -o wide
NAME                             READY   STATUS    RESTARTS   AGE    IP           NODE           NOMINATED NODE   READINESS GATES
pod/mysql-674c86db65-sklkt       1/1     Running   0          108m   10.244.5.2   kind-worker5   <none>           <none>
pod/wordpress-596457999c-tdp8t   1/1     Running   0          108m   10.244.1.2   kind-worker    <none>           <none>

NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE    SELECTOR
service/mysql-svc       ClusterIP   None            <none>        3306/TCP       108m   app=wordpress
service/wordpress-svc   NodePort    10.110.117.57   <none>        80:31000/TCP   108m   app=wordpress

NAME                        READY   UP-TO-DATE   AVAILABLE   AGE    CONTAINERS   IMAGES                 SELECTOR
deployment.apps/mysql       1/1     1            1           108m   mysql        mysql:5.6              app=wordpress
deployment.apps/wordpress   1/1     1            1           108m   wordpress    wordpress:4.8-apache   app=wordpress

NAME                                   DESIRED   CURRENT   READY   AGE    CONTAINERS   IMAGES                 SELECTOR
replicaset.apps/mysql-674c86db65       1         1         1       108m   mysql        mysql:5.6              app=wordpress,pod-template-hash=674c86db65
replicaset.apps/wordpress-596457999c   1         1         1       108m   wordpress    wordpress:4.8-apache   app=wordpress,pod-template-hash=596457999c
```

Y para acceder desde el navegador, ejecutamos:

```bash
kubectl -n wordpress port-forward service/wordpress-svc 8181:80
```

Abriendo esta url [http://localhost:8181](http://localhost:8181) en el navegador podremos entrar a **wordpress**:

```bash
kubectl -n wordpress port-forward service/wordpress-svc 8181:80
```
