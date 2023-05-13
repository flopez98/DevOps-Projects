# Azure DevOps Pipeline for .NET Application Deployment to Azure

This repository presents an Azure DevOps Pipeline designed to build a .NET application, provision necessary Azure infrastructure using Terraform, and deploy the application. 

In order to maintain the readability and manageability of the pipeline, the YAML code is broken down into separate files, each corresponding to a specific stage in the pipeline.

## Pipeline Overview

The pipeline consists of three main stages: Build, Terraform, and Deployment.

1. **Build Stage**: This stage restores, builds, and publishes the .NET Core solution. The published artifacts are stored for use in the later Deployment stage. The YAML code for this stage can be found in the `build-pipeline.yml` file.

2. **Terraform Stage**: This stage provisions the required infrastructure on Azure using Terraform. It leverages the Azure Resource Manager (ARM) backend and executes `init`, `plan`, and `apply` commands to set up the infrastructure. The YAML code for this stage is in the `terraform-pipeline.yml` file.

3. **Deployment Stage**: This stage deploys the application to Azure Web App and updates the application settings. It also runs a SQL script on an Azure SQL Database. The YAML code for this stage is contained in the `deploy-pipeline.yml` file.

Additionally, a `terraform-destroy.yml` pipeline is included in order to clean up the Azure resources created by the Terraform stage when they are no longer needed. This helps prevent unnecessary Azure costs.

## Prerequisites

Before running the pipeline, you need to create a variable group in your Azure DevOps project named 'Terraform'. Here are the variables you'll need to include in this group:

**Terraform Variable Group**:
- `backendAzureRmContainerName`
- `backendAzureRmKey`
- `backendAzureRmResourceGroupName`
- `backendAzureRmStorageAccountName`
- `backendServiceArm`

These values are obtained from your service principal in Azure.

## Running the Pipeline

Once you have configured the variable group, you can run the pipeline. Ensure your Azure account has necessary permissions to create and manage resources.