Debemos tener **Helm** instalado:

```bash
cd ansible
ansible-playbook install.yml -t helm
```

Creamos un workspace para **Vault**:

```bash
kubectl create namespace vault
```

Añadimos el repositorio de **Hashicorp** a **Helm**:

```bash
helm repo add hashicorp https://helm.releases.hashicorp.com
```

Y comprobamos que tenemos acceso al chart de **Vault**:

```bash
helm search repo hashicorp/vault
NAME           	CHART VERSION	APP VERSION	DESCRIPTION                   
hashicorp/vault	0.8.0        	1.5.4      	Official HashiCorp Vault Chart
```

Vemos las versiones disponibles del chart de **Vault**:

```bash
helm search repo hashicorp/vault -l
NAME           	CHART VERSION	APP VERSION	DESCRIPTION                               
hashicorp/vault	0.8.0        	1.5.4      	Official HashiCorp Vault Chart            
hashicorp/vault	0.7.0        	1.5.2      	Official HashiCorp Vault Chart            
hashicorp/vault	0.6.0        	1.4.2      	Official HashiCorp Vault Chart            
hashicorp/vault	0.5.0        	           	Install and configure Vault on Kubernetes.
hashicorp/vault	0.4.0        	           	Install and configure Vault on Kubernetes.
```

E instalamos la última versión:

```bash
helm install vault hashicorp/vault --namespace vault --version 0.8.0
```

Personalizamos la configuracion de **Vault**:

```bash
helm install vault hashicorp/vault --namespace vault --set "server.ha.enabled=true" --set "server.ha.replicas=5" --dry-run
```

Revisamos todos los objetos que se han creado en el namespace `vault`:

```bash
kubectl -n vault get all
NAME                                        READY   STATUS    RESTARTS   AGE
pod/vault-0                                 0/1     Running   0          4m44s
pod/vault-agent-injector-6fcf464c66-b44c9   1/1     Running   0          4m45s

NAME                               TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
service/vault                      ClusterIP   10.111.52.87    <none>        8200/TCP,8201/TCP   4m45s
service/vault-agent-injector-svc   ClusterIP   10.104.167.33   <none>        443/TCP             4m45s
service/vault-internal             ClusterIP   None            <none>        8200/TCP,8201/TCP   4m45s

NAME                                   READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/vault-agent-injector   1/1     1            1           4m45s

NAME                                              DESIRED   CURRENT   READY   AGE
replicaset.apps/vault-agent-injector-6fcf464c66   1         1         1       4m45s

NAME                     READY   AGE
statefulset.apps/vault   0/1     4m45s
```

Será necesario inicializar **Vault**, para ello vemos los pods que hay corriendo:

```bash
kubectl -n vault get pods -o wide
NAME                                    READY   STATUS    RESTARTS   AGE   IP           NODE           NOMINATED NODE   READINESS GATES
vault-0                                 0/1     Running   0          10m   10.244.5.3   kind-worker5   <none>           <none>
vault-agent-injector-6fcf464c66-b44c9   1/1     Running   0          10m   10.244.3.2   kind-worker2   <none>           <none>
```

Y ejecutamos el siguiente comando:

```bash
kubectl -n vault exec -ti vault-0 -- vault operator init
Unseal Key 1: 9iQo+HMY6sEdMELIlBbNQIqvunkGCqlDLMYvEFK6+nBZ
Unseal Key 2: OeKLFvec/c3jovp0a0kdJ+vwP5r3KR8nZ2FJT9H9BrIF
Unseal Key 3: exzu39xb0CZcTffP4MgfBJHfsRSDZUE270dgBaMAyUsq
Unseal Key 4: bJ9eUdpHQhYTa0QoUx1pOiurQNwxfc/cRLzLpmuto4SA
Unseal Key 5: bTC+XXg1QNVk1xohfiwq8IHl4HWh+df6QPM+CjTBCrxy

Initial Root Token: s.D84NvI6kiMzR2bvS7It2qvcB

Vault initialized with 5 key shares and a key threshold of 3. Please securely
distribute the key shares printed above. When the Vault is re-sealed,
restarted, or stopped, you must supply at least 3 of these keys to unseal it
before it can start servicing requests.

Vault does not store the generated master key. Without at least 3 key to
reconstruct the master key, Vault will remain permanently sealed!

It is possible to generate new unseal keys, provided you have a quorum of
existing unseal keys shares. See "vault operator rekey" for more information.
```

Y para desellar el **Vault**:

```bash
kubectl -n vault exec -ti vault-0 -- vault operator unseal 9iQo+HMY6sEdMELIlBbNQIqvunkGCqlDLMYvEFK6+nBZ
Key                Value
---                -----
Seal Type          shamir
Initialized        true
Sealed             true
Total Shares       5
Threshold          3
Unseal Progress    1/3
Unseal Nonce       5f2a5f20-fc92-d2ca-6e89-3483ed8d4db5
Version            1.5.4
HA Enabled         false

kubectl -n vault exec -ti vault-0 -- vault operator unseal OeKLFvec/c3jovp0a0kdJ+vwP5r3KR8nZ2FJT9H9BrIF
Key                Value
---                -----
Seal Type          shamir
Initialized        true
Sealed             true
Total Shares       5
Threshold          3
Unseal Progress    2/3
Unseal Nonce       5f2a5f20-fc92-d2ca-6e89-3483ed8d4db5
Version            1.5.4
HA Enabled         false

kubectl -n vault exec -ti vault-0 -- vault operator unseal exzu39xb0CZcTffP4MgfBJHfsRSDZUE270dgBaMAyUsq
Key             Value
---             -----
Seal Type       shamir
Initialized     true
Sealed          false
Total Shares    5
Threshold       3
Version         1.5.4
Cluster Name    vault-cluster-cae97d55
Cluster ID      452d8f76-1e33-2238-f578-ee68cfb74106
HA Enabled      false
```

Y para acceder desde el navegador, ejecutamos:

```bash
kubectl -n vault port-forward service/vault 8200:8200 
```

Abriendo esta url [http://localhost:8200](http://localhost:8200) en el navegador podremos entrar a **Vault**:
