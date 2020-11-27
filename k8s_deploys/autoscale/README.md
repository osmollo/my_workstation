Instalamos el __metrics-server__ en el cluster:

```bash
kubectl apply -f metrics/.
```

Creamos un nuevo namespace para el autoescalado:

```bash
kubectl create ns autoscale
```

Y desplegamos los manifiestos:

```bash
kubectl -n autoscale apply -f .
```

Vemos el estado de los objetos:

```bash
kubectl -n autoscale get all
NAME                            READY   STATUS              RESTARTS   AGE
pod/php-apache-5f58446c-f2j7m   0/1     ContainerCreating   0          50s
pod/php-apache-5f58446c-g6dq6   0/1     ContainerCreating   0          50s
pod/php-apache-5f58446c-g8lkr   0/1     ContainerCreating   0          50s

NAME                 TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/php-apache   NodePort   10.106.136.158   <none>        80:31500/TCP   10s

NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/php-apache   0/3     3            0           50s

NAME                                  DESIRED   CURRENT   READY   AGE
replicaset.apps/php-apache-5f58446c   3         3         0       50s

NAME                                             REFERENCE               TARGETS         MINPODS   MAXPODS   REPLICAS   AGE
horizontalpodautoscaler.autoscaling/php-apache   Deployment/php-apache   <unknown>/50%   1         10        3          50s
```
