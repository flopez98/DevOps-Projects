Project Name: Learning Packer

The Learning Packer project is aimed at providing a simple and quick way of creating and deploying Virtual Machine (VM) images to Microsoft Azure using Packer and Terraform. This project focuses on creating two different VM images, one running Linux and the other running Windows.

Project Description

The project involves creating two different VM images using Packer. The first image is a Linux VM in which we run the apt update command. The second image is a Windows VM in which we install the Chocolatey package manager. Once the images are built, we use Terraform to deploy them to Azure.
Prerequisites

Before starting with the project, ensure that you have the following software installed on your system:

- Packer
- Terraform
- Azure CLI

We must also create a service principal in Azure and modify the 'variables.auto.pkrvars.hcl' file.

Getting Started

To get started with the project, follow the steps below:

1. Generate an SSH key for the Linux VM. You can use the following command:

        ssh-keygen

   This will create an SSH key at the default path and name of ~/.ssh/id_rsa.

2. Change directory to the Lab3-Learning-Packer/Terraform/terraform-repo folder and run the following command to deploy a resource group named packer-rg.

        cd Lab3-Learning-Packer/Terraform/terraform-repo
        terraform init

3. Run the following command to create the resource group:

        terraform apply -auto-approve

4. Change directory to the Lab3-Learning-Packer/Packer/linux or Lab3-Learning-Packer/Packer/windows folder, depending on which image you want to build.

        cd ../Packer/linux

   or

        cd ../Packer/windows

5. Run the packer build . command to build the VM image and push it to Azure.

        packer build .

6. After successfully building the VM images, test them using Terraform. Navigate to the Lab3-Learning-Packer/Terraform/packer-tester folder and run the following commands:

        cd ../packer-tester
        terraform init
        terraform plan
        terraform apply -auto-approve

7. When connecting to the Linux VM via bastion, make sure that you provide the private SSH key located at ~/.ssh/id_rsa, the username is 'useradmin', unless changed in the Terraform code. For the Windows bastion connection, the password will be automatically created in a file named 'password.txt', username is 'useradmin'.

Congratulations! You have now successfully built and deployed two different VM images using Packer and Terraform.
Further Information

For more information on Packer and Terraform, refer to the following links:

    Packer: https://www.packer.io/
    Terraform: https://www.terraform.io/

For more information on Azure and Azure CLI, refer to the following links:

    Azure: https://azure.microsoft.com/
    Azure CLI: https://docs.microsoft.com/en-us/cli/azure/