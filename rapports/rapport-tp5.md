# TP5

**1. & 2.** Ensure all microservice images are present in the local registry and write a deplyoment manifest for each microservices instead of standalone pods

**3. & 4.** Update the front-end web image, modify the manifest tag, and perform a rolling update ensuring zero downtime configuration. Simulate a deployment failure using a non-existent tag and execute a rollback

```sh
kubectl rollout undo deployment/<site-deployment-name>
```

**5.** Create standard service object to establish communication channels between the microservices

**6.** Convert the MongoDB database deployment into a StatefulSet accompanied by a headless service (clusterIP: None) to guarantee data volume persistence across container restarts

**7.** Expose the main front-end service to the outside of the cluster and enable the metrics-server addon to monitor pod CPU and RAM

```sh
minikube addons enable metrics-server
```

**8. to 10.** Define liveness and readiness probes, configure appropriate CPU/Memory requests and limits, and deploy a Horizontal Pod Autoscaler (HPA) mechanism for the web site and APIs

