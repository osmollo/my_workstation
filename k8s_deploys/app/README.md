Creamos un namespace para realizar esta prueba:

```bash
kubectl create namespace test
```

Y a continuación desplegamos los objetos definidos en el fichero [deploy.yml](./deploy.yml):

```bash
kubectl -n test apply -f deploy.yml
```

Vemos cómo se crean los elementos:

```bash
kubectl -n test get all
NAME          READY   STATUS              RESTARTS   AGE
pod/bar-app   0/1     ContainerCreating   0          5s
pod/foo-app   0/1     ContainerCreating   0          5s

NAME                  TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/bar-service   ClusterIP   10.98.113.100   <none>        5678/TCP   5s
service/foo-service   ClusterIP   10.97.182.114   <none>        5678/TCP   5s
```

Y la regla de ingress:

```bash
kubectl -n test get ing
NAME              CLASS    HOSTS   ADDRESS     PORTS   AGE
example-ingress   <none>   *       localhost   80      38s
```

Para probar que se puede acceder desde fuera:

```bash
curl localhost/foo
foo

curl localhost/bar
bar
```
