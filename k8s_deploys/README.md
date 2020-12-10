# Jugando con kubernetes

- [Jugando con kubernetes](#jugando-con-kubernetes)
  - [Minikube](#minikube)
  - [Creando un cluster](#creando-un-cluster)
    - [Escalar cluster](#escalar-cluster)
    - [Desescalar cluster](#desescalar-cluster)
    - [Borrar el cluster](#borrar-el-cluster)
    - [Activar dashboard](#activar-dashboard)
    - [Ingress](#ingress)
  - [Kind](#kind)
    - [Creando un cluster de prueba](#creando-un-cluster-de-prueba)
    - [Borrando el cluster](#borrando-el-cluster)
    - [Ingress controler](#ingress-controler)
      - [Nginx ingress controller](#nginx-ingress-controller)
      - [Contour ingress controller](#contour-ingress-controller)
      - [Ambassador ingress controller](#ambassador-ingress-controller)
    - [Software Load Balancer](#software-load-balancer)
      - [Metallb (no desplegar)](#metallb-no-desplegar)
  - [Documentación](#documentación)

## Minikube


[Minikube](https://kubernetes.io/es/docs/tasks/tools/install-minikube/) es una solución oficial para poder desplegar __kubernetes__ en un entorno local mediante **Docker**, **Virtualbox**... Puede instalarse mediante el siguiente comando:

```bash
cd ../ansible
ansible-playbook install.yml -t minikube
```

## Creando un cluster

Para crear un cluster de un sólo nodo, simplemente hay que ejecutar el comando:

```bash
minikube start [--nodes=N]
```

### Escalar cluster

Para escalar el cluster y añadir más nodos, hay que ejecutar:

```bash
minikube node add
```

### Desescalar cluster

Para eliminar un nodo del cluster, primero tenemos que listar los nodos existentes:

```bash
minikube node list
minikube        192.168.49.2
minikube-m02    192.168.49.3
minikube-m03    192.168.49.4
minikube-m04    192.168.49.5
```

A continuación, borramos el nodo que queramos:

```bash
minikube node delete minikube-m04
```

### Borrar el cluster

Para destruir el cluster tenemos que ejecutar:

```bash
minikube stop
```

### Activar dashboard

Para poder acceder al dashboard de __kubernetes__ hay que ejecutar el siguiente comando:

```bash
minikube dashboard
```

Automáticamente se abrirá un navegador con la [url del dashboard](http://127.0.0.1:33747/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/#/overview)


### Ingress

Para habilitar el addon para __ingress__:

```bash
minikube addons ingress enable
```

## Kind

[KIND](https://kind.sigs.k8s.io/) es otra solución oficial para desplegar un cluster de __Kubernetes__ dentro de contenedores **Docker**. Puede instalarse con el siguiente comando:

```bash
cd ../ansible
ansible-playbook install.yml -t kind
```

### Creando un cluster de prueba

Hay que crear un fichero [kind.yml](./kind.yml) (o el nombre que se quiera), donde se definen los nodos del cluster:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP
  image: kindest/node:v1.19.4
- role: worker
  image: kindest/node:v1.19.4
- role: worker
  image: kindest/node:v1.19.4
- role: worker
  image: kindest/node:v1.19.4
- role: worker
  image: kindest/node:v1.19.4
```

Y para ejecutar el cluster:

```bash
kind create cluster --config kind.yml
```

### Borrando el cluster

Para destruír el cluster, hay que ejecutar:

```bash
kind delete cluster
```

### Ingress controler

Los __ingress controller__ permiten accecder a los servicios desplegados en Kubernetes desde fuera del cluster. Hay que instalar uno de los siguientes:

#### Nginx ingress controller

Para instalar el ingress de **Nginx**, ejecutamos el siguiente comando:

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/kind/deploy.yaml
```

Para ver todos los elementos que se están creando se puede ejecutar:

```bash
kubectl -n ingress-nginx get all
```

Con el siguiente comando reconfiguramos ingress para que espere hasta que el pod esté listo para recibir peticiones:

```bash
kubectl wait --namespace ingress-nginx --for=condition=ready pod --selector=app.kubernetes.io/component=controller --timeout=90s
```

#### Contour ingress controller

Hay que instalar el controlador:

```bash
kubectl apply -f https://projectcontour.io/quickstart/contour.yaml
```

```bash
kubectl -n demo-contour apply -f https://raw.githubusercontent.com/vOrcunus/random-work/master/kind/deploy-demoapp.yaml
kubectl -n demo-contour apply -f https://raw.githubusercontent.com/vOrcunus/random-work/master/kind/contour-httpproxy-demoapp.yaml
```

Por último, hay que aplicar un parche específico de **Kind** para reenviar el tráfico de los hostPorts al ingress controller:

```bash
kubectl patch daemonsets -n projectcontour envoy -p '{"spec":{"template":{"spec":{"nodeSelector":{"ingress-ready":"true"},"tolerations":[{"key":"node-role.kubernetes.io/master","operator":"Equal","effect":"NoSchedule"}]}}}}'
```

#### Ambassador ingress controller

Primero instalamos los CDRs:

```bash
kubectl apply -f https://github.com/datawire/ambassador-operator/releases/latest/download/ambassador-operator-crds.yaml
```

A continuación, instalamos el manifiesto específico de **Ambassador** para **Kind**:

```bash
kubectl apply -n ambassador -f https://github.com/datawire/ambassador-operator/releases/latest/download/ambassador-operator-kind.yaml
kubectl wait --timeout=180s -n ambassador --for=condition=deployed ambassadorinstallations/ambassador
```

Cuando se realice el despliegue del ingress, hay que crear esta anotación cambiando el nombre del ingress:

```bash
kubectl annotate ingress $INGRESS_NAME kubernetes.io/ingress.class=ambassador
```

### Software Load Balancer

#### Metallb (no desplegar)

Para poder crear `LoadBalancer` en el cluster, es necesario instalar **MetalLB** con los siguientes comandos:

```bash
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.9.5/manifests/namespace.yaml
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.9.5/manifests/metallb.yaml

# Sólo para la primera ejecución
kubectl create secret generic -n metallb-system memberlist --from-literal=secretkey="$(openssl rand -base64 128)"
```

Tenemos que comprobar el rango de la red `bridge` de **Docker** que están usando los contenedores de kind (los nodos de kubernetes), para poder asignar IPs a los LBs:

```bash
docker network inspect bridge | jq '.[0].IPAM.Config[0].Subnet'
"172.17.0.0/16"
```

Así que creamos el manifiesto:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  namespace: metallb-system
  name: config
data:
  config: |
    address-pools:
    - name: default
      protocol: layer2
      addresses:
      - 172.17.255.1-172.17.255.250
```

Y lo desplegamos:

```bash
kubectl apply -f metallb_config.yml
```

## Documentación

* Kind:
  * [Local kubernetes setup with kind](https://www.danielstechblog.io/local-kubernetes-setup-with-kind/)
  * [Creating test Kubernetes clusters with Kind](https://octopus.com/blog/testing-with-kind)
* Ingress controller:
  * [Ambassador](https://www.getambassador.io/docs/latest/)
  * [Contour](https://projectcontour.io/docs/v1.10.0/)
  * [More KinD with Contour as Ingress Controller](https://orcunuso.wordpress.com/2020/05/18/more-kind-with-contour-as-ingress-controller/)
* MetalLB:
  * [Documentación oficial](https://metallb.universe.tf/installation/)
  * [Using metallb with kind](https://mauilion.dev/posts/kind-metallb/)
  * [KIND and Load Balancing with MetalLB on Mac](https://www.thehumblelab.com/kind-and-metallb-on-mac/)
