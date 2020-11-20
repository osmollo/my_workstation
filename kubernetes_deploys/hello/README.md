Creamos un namespace para realizar esta prueba:

```bash
kubectl create namespace pelado
```

Y a continuación desplegamos los objetos definidos en el fichero [deploy.yml](./deploy.yml):

```bash
kubectl -n pelado apply -f deploy.yml
```

Vemos cómo se crean los elementos:

```bash
kubectl -n pelado get all
NAME                            READY   STATUS              RESTARTS   AGE
pod/hello-v1-57cbdf9dd5-8d4zc   0/1     ContainerCreating   0          6s
pod/hello-v1-57cbdf9dd5-ftkbm   0/1     ContainerCreating   0          6s
pod/hello-v1-57cbdf9dd5-hjh9r   0/1     ContainerCreating   0          6s
pod/hello-v2-54c58bf4cf-9g8nx   0/1     ContainerCreating   0          6s
pod/hello-v2-54c58bf4cf-d7r5p   0/1     ContainerCreating   0          6s
pod/hello-v2-54c58bf4cf-llgkn   0/1     ContainerCreating   0          6s

NAME                   TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
service/hello-v1-svc   ClusterIP   10.109.100.177   <none>        80/TCP    6s
service/hello-v2-svc   ClusterIP   10.103.120.217   <none>        80/TCP    6s

NAME                       READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/hello-v1   0/3     3            0           6s
deployment.apps/hello-v2   0/3     3            0           6s

NAME                                  DESIRED   CURRENT   READY   AGE
replicaset.apps/hello-v1-57cbdf9dd5   3         3         0       6s
replicaset.apps/hello-v2-54c58bf4cf   3         3         0       6s
```

Y la regla de ingress:

```bash
kubectl -n pelado get ing
NAME              CLASS    HOSTS   ADDRESS     PORTS   AGE
example-ingress   <none>   *       localhost   80      38s
```

Para probar que se puede acceder desde fuera:

```bash
curl localhost/hello1
Hello, world!
Version: 1.0.0
Hostname: hello-v1-57cbdf9dd5-hjh9r

curl localhost/hello2
Hello, world!
Version: 2.0.0
Hostname: hello-v2-54c58bf4cf-d7r5p
```
