# Kubernetes Microservices with Minikube: Node.js and Nginx Deployment

This project provides a hands-on demonstration of Kubernetes LoadBalancer service by deploying two distinct services: a custom Node.js Express application and an Nginx server.

The Node.js application not only displays a simple greeting from the host it is running on, but also fetches and displays the response from the Nginx server when accessed through a specific route. This setup illustrates the functioning of Kubernetes LoadBalancer service in effectively distributing network traffic among multiple deployed pods, thereby ensuring high availability and reliability of the services.

The use of Kubernetes LoadBalancer in this setup allows the application to handle varying loads and distribute network traffic to multiple instances of the application, showcasing the capabilities of Kubernetes in a microservices architecture.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Building the Docker Image](#building-the-docker-image)
- [Deploying to Kubernetes](#deploying-to-kubernetes)
- [Testing the Deployment](#testing-the-deployment)
- [Cleaning Up](#cleaning-up)

## Prerequisites

Before starting, ensure you have the following software installed on your machine:

- Docker
- Minikube
- kubectl CLI tool

## Building the Docker Image

The Dockerfile for creating the image of the Node.js application is assumed to be included in the root of the project directory. To build the Docker image and push it to DockerHub, use the following commands:

```bash
docker build -t your_dockerhub_username/k8s-web-to-nginx .
docker push your_dockerhub_username/k8s-web-to-nginx
```

Replace `your_dockerhub_username` with your DockerHub username.

## Deploying to Kubernetes

To deploy the services to Minikube, use the provided Kubernetes manifests. They will deploy two services:

1. `k8s-web-to-nginx`: A custom Node.js Express application that fetches and displays the response from the Nginx server.
2. `nginx`: A simple Nginx server.

Each service has a corresponding Kubernetes `Deployment` and `Service`. 

To apply the manifests, navigate to the directory containing the manifest file(s), then run:

```bash
kubectl apply -f file_name.yaml
```

Replace `file_name.yaml` with the name of your Kubernetes manifest file.

## Testing the Deployment

After applying the manifests, the services will be accessible via their respective Kubernetes service URLs.

To test the `k8s-web-to-nginx` service, run:

```bash
minikube service k8s-web-to-nginx
```

This will automatically open the `k8s-web-to-nginx` service in your default web browser.

To test the `/nginx` route of the `k8s-web-to-nginx` service which fetches the response from the Nginx server, simply append `/nginx` to the URL opened by the previous command in your browser.

**Note on Resource Management:**

This project deploys a total of 8 pods - 3 replicas of the Node.js application and 5 replicas of the Nginx server. Depending on your system configuration, the default CPU allocation for Minikube may not be sufficient to run all these pods simultaneously. 

If you encounter issues related to resource constraints, you have two options:

1. **Adjust the number of replicas in the Kubernetes manifest files:** The `replicas` field under the `spec` of each `Deployment` determines how many instances of that deployment (pods) should be running. You can reduce these values if your system cannot accommodate the current number of total pods.

2. **Increase the number of CPUs allocated to Minikube:** You can allocate more CPUs to Minikube using the `--cpus` flag during the start command, like so: `minikube start --driver=hyperkit --cpus 4`. This example assigns 4 CPUs to Minikube. Adjust this number based on the resources available on your system.

Remember, efficient resource management is crucial when working with Kubernetes and other container orchestration platforms. Make sure to balance the resources your applications need with what's available on your system to ensure smooth operation.

## Cleaning Up

To delete the Kubernetes resources created by the manifests, run:

```bash
kubectl delete -f file_name.yaml
```

Replace `file_name.yaml` with the name of your Kubernetes manifest file.

**Important:** While running in a local Minikube environment doesn't incur extra costs, it's good practice to clean up resources when they're no longer needed.