# Jugando con kubernetes

- [Jugando con kubernetes](#jugando-con-kubernetes)
  - [Creando un cluster de prueba](#creando-un-cluster-de-prueba)
  - [Ingress controler](#ingress-controler)
    - [Nginx ingress controller](#nginx-ingress-controller)
    - [Contour ingress controller](#contour-ingress-controller)
    - [Ambassador ingress controller](#ambassador-ingress-controller)
  - [Software Load Balancer](#software-load-balancer)
    - [Metallb (no desplegar)](#metallb-no-desplegar)
  - [Borrando el cluster](#borrando-el-cluster)
  - [Documentación](#documentación)

[KIND](https://kind.sigs.k8s.io/) es una solución oficial para desplegar un cluster de __Kubernetes__ dentro de contenedores **Docker**. Puede instalarse con el siguiente comando:

```bash
cd ../ansible
ansible-playbook install.yml -t kind
```

## Creando un cluster de prueba

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
- role: worker
- role: worker
- role: worker
- role: worker
- role: worker
```

Y para ejecutar el cluster:

```bash
kind create cluster --config kind.yml
```

## Ingress controler

Los __ingress controller__ permiten accecder a los servicios desplegados en Kubernetes desde fuera del cluster. Hay que instalar uno de los siguientes:

### Nginx ingress controller

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

### Contour ingress controller

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

### Ambassador ingress controller

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

## Software Load Balancer

### Metallb (no desplegar)

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

## Borrando el cluster

Para destruír el cluster, hay que ejecutar:

```bash
kind delete cluster
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
