# Kubernetes - Learning RBAC and Deploying an NGINX Pod

This project is a set of instructions to create a Kubernetes environment for an Nginx server, using Minikube. The instructions include creating ConfigMaps, Secrets, PersistentVolumes, and PersistentVolumeClaims, as well as creating a Kubernetes user, a context, and a role. The steps are detailed below:

## Requirements
- Minikube
- openssl

## Instructions

1. Start Minikube:
   ```
   minikube start
   ```

2. Create the following manifest files:
   - config-map.yaml
   - secret.yaml
   - pv.yaml
   - pvc.yaml
   - pod.yaml
   
3. Apply the manifest files using `kubectl apply -f` command in the following order:
   ```
   kubectl apply -f config-map.yaml
   kubectl apply -f secret.yaml
   kubectl apply -f pv.yaml
   kubectl apply -f pvc.yaml
   kubectl apply -f pod.yaml
   ```

4. Create a namespace named 'dev':
   ```
   kubectl create namespace dev
   ```

5. Edit the OpenSSL configuration file by commenting out the line 'RANDFILE	= $ENV::HOME/.rnd':
   ```
   sudo nano /etc/ssl/openssl.cnf
   ```

6. Create a private key:
   ```
   openssl genrsa -out emp.key 2048
   ```

7. Create a certificate:
   ```
   openssl req -new -key emp.key -out emp.csr -subj "/CN=emp/O=dev"
   ```

8. Generate the 'emp.crt' certificate:
   ```
   openssl x509 -req -in emp.csr -CA ~/.minikube/ca.crt -CAkey ~/.minikube/ca.key -CAcreateserial -out emp.crt -days 365
   ```

9. Create a Kubernetes user named 'emp':
   ```
   kubectl config set-credentials emp --client-key=emp.key --client-certificate=emp.crt
   ```

10. Create a context:
   ```
   kubectl config set-context dev-ctx --cluster=minikube --namespace=dev --user=emp
   ```
   To view the available contexts, use `kubectl config get-contexts`. To switch contexts, use `kubectl config use-context Name_of_context`.

11. Create a role named 'emp-role':
   ```
   kubectl create role emp-role --verb=get,list --resource=pods,deployments --namespace=dev
   ```

12. Bind the user 'emp' to the role 'emp-role':
   ```
   kubectl create rolebinding emp-bind --role=emp-role --user=emp --namespace=dev
   ```

13. Create an Nginx pod under 'dev-ctx' and 'dev' namespace:
   ```
   kubectl run nginx --image=nginx --namespace=dev --context=dev-ctx
   ```

14. Verify the running pod:
   ```
   kubectl --context=dev-ctx get pods -o wide
   ```

Note: Check `~/.minikube/` for `ca.key` and `ca.crt` files.