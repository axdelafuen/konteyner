# TP6-7

Part 1: Q1. to Q6. Extract hardcoded environment variables (like API URLs) into a configmap-site.yaml file and refactor the Deployments to dynamically inject these variables using envFrom.  

Part 2: Q1. to Q4. Create a mongodb.secret.yaml file to safely store base64-encoded credentials, ensure it is ignored by version control (.gitignore), and reference it in the manifests utilizing secretKeyRef.  

Part 3: Q1. to Q11. Generate a base Helm chart structure, externalize environment-specific configurations into values.yaml, validate template rendering, and manage application lifecycle operations such as installation, upgrades, and rollbacks.  

```sh
helm install my-app ./mon-dossier/
```

Part 4: Q1. to Q2. Add the community Helm repository and install the kube-prometheus-stack to deploy Prometheus, Alertmanager, and Grafana.  

```sh
helm install kube-prom prometheus-community/kube-prometheus-stack
```

Part 4: Q3. to Q5. Access Grafana via port-forwarding, explore default Kubernetes resource dashboards, construct a custom dashboard using PromQL to track CPU and Memory metrics, and observe HPA behavior under simulated command-line load.  

```sh
kubectl port-forward svc/kube-prom-grafana 3001:80
```
