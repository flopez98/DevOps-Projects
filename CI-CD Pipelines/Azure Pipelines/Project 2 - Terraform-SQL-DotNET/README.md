# Simple .NET App with SQL Database on Azure

This repository contains a straightforward .NET application that interacts with a SQL database hosted in Azure. The application fetches data from this database and showcases it on the `index.html` page.

## Prerequisites

For a successful execution of this pipeline, ensure you have:

1. An Azure subscription - if you don't have one, create a free account.
2. A service principal in Azure - follow [these instructions](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal) to create one.
3. Azure DevOps Pipelines set up, with permissions to create variable groups.

## Azure DevOps Pipeline Configuration

The pipeline provided is designed to be compatible with Azure DevOps. To execute the pipeline, you need to configure a variable groups, 'Terraform' & 'sql-credentials'.

### 'Terraform' Variable Group

This group should contain the following variables related to your Azure storage account, which acts as the Terraform backend:

- `backendAzureRmContainerName`
- `backendAzureRmKey`
- `backendAzureRmResourceGroupName`
- `backendAzureRmStorageAccountName`
- `backendServiceArm`

### 'sql-credentials' Variable Group

This group should include the following variables:

- `SqlPassword`
- `SqlUsername`

These variables correspond to your SQL database credentials. Ensure that these are provided in line with your SQL database configuration.

## Running the Pipeline

After setting up the variable groups in your Azure DevOps pipeline, you can run the pipeline. The pipeline performs the following actions:

1. Builds the .NET application
2. Provisions the necessary infrastructure using Terraform
3. Deploys the application to Azure

## Application Behavior

The application is a straightforward .NET app that interacts with an Azure SQL database. It retrieves data from a specific database table and displays it on the `index.html` page.

Please note that the actual behavior might differ based on the specific SQL scripts and the .NET application code used.

## Project Structure

The main pipeline files are located in the 'Pipelines' folder. This folder contains YAML files that define the steps for building the application, provisioning the infrastructure, and deploying the application.