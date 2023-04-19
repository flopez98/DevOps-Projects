Kubernetes Project Readme

This project includes the necessary configuration files to deploy a MongoDB and Mongo Express instance on a Kubernetes cluster.

Prerequisites

Before installing and running this project, you need to have the following prerequisites installed:

- Kubernetes: This project requires a Kubernetes cluster to run. You can use a cloud-based Kubernetes service or set up a local cluster using tools like Minikube.

- Minikube: If you are setting up a local Kubernetes cluster, you will need to install Minikube. Minikube is a tool that allows you to run a single-node Kubernetes cluster on your local machine.

To install Minikube, follow the instructions on the official Minikube documentation.

    https://minikube.sigs.k8s.io/docs/start/

To install Kubernetes, follow the instructions on the official Kubernetes documentation.

    https://kubernetes.io/docs/setup/

Make sure that both Kubernetes and Minikube are installed and running before proceeding with the installation of this project.

1. Installation

   Apply the configuration files using the following command:

        kubectl apply -f mongo.yaml -f mongo-secret.yaml -f mongo-express.yaml -f mongo-configmap.yaml

2. Configuration

    The project includes the following files:

    'mongo.yaml'

    This file contains the configuration for the MongoDB deployment and service. It specifies the number of replicas, container image, and environment variables required for the MongoDB instance.

    'mongo-secret.yaml'

    This file includes the MongoDB root username and password stored as a Kubernetes secret. It uses the base64 encoding to hide the actual values.

    'mongo-express.yaml'

    This file contains the configuration for the Mongo Express deployment and service. It specifies the number of replicas, container image, and environment variables required for the Mongo Express instance.

    'mongo-configmap.yaml'

    This file creates a ConfigMap containing the database URL used by the Mongo Express instance.

3. Usage

    After applying the configuration files, the MongoDB and Mongo Express instances will be available on the Kubernetes cluster.

    To access the Mongo Express UI, use the following command:

        minikube service mongo-express-service

    This will open a browser window with the Mongo Express UI.

    Note: The external IP for the Mongo Express service can be assigned using minikube.