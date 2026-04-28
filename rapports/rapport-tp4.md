# TP4

**1. to 4.** Install kubectl and minikube, verify their respective versions, and start the local development cluster.  

```sh
minikube start --driver=docker
```

**5. & 6.** Load the required target image (kuard-amd64:blue) into the cluster's internal Docker registry to avoid ImagePullBackOff errors.  

```sh
minikube image load docker.io/jmutai/kuard-amd64:blue
```

**7. & 8.** Write a YAML manifest to deploy a Pod exposing port 8080 over HTTP, apply it, and verify accessibility via port-forwarding.  

```sh
kubectl port-forward pod/kuard 8080:8080
```

**9.** Add specific labels (app=kuard and environment=dev) to the running Pod and filter the cluster's Pod list using these identifiers.  

```sh
kubectl label pods kuard app=kuard environment=dev
```

**10. to 12.** Create a dedicated namespace named tp4, recreate the Pod within this namespace, retrieve its logs, and update the manifest to include liveness and readiness probes.  

```sh
kubectl create namespace tp4
```
