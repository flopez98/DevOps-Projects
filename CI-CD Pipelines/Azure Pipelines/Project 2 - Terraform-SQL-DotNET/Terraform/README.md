# Azure DevOps Pipeline: Terraform Deployment

This Terraform configuration script deploys a set of Azure resources required to run a .NET web application. The application is connected to an Azure SQL database and retrieves values from this database, displaying them on an `index.html` page.

## Prerequisites

To successfully execute this pipeline, you need to set up the following:

- Azure DevOps account with a pipeline configured
- Azure account with appropriate permissions
- Service principal in Azure for Terraform
- Azure DevOps variable group named 'Terraform'

## 'Terraform' Variable Group

This group should contain the following variables related to your Azure storage account, which acts as the Terraform backend:

- `backendAzureRmContainerName`
- `backendAzureRmKey`
- `backendAzureRmResourceGroupName`
- `backendAzureRmStorageAccountName`
- `backendServiceArm`

These values are obtained from your service principal in Azure.

## Resources Deployed

The Terraform script in `main.tf` deploys these main resources:

1. **Resource Group**: This is a logical container for resources deployed within an Azure subscription. It's a way to manage and organize resources based on lifecycle and other categorizations that make sense for your organization. 

2. **Service Plan**: An Azure App Service Plan dictates the size and scale of the resources available to your Web App. The size of these resources affects the cost of the service. This script creates a service plan with the "F1" Free tier.

3. **Web App**: The App Service Web App is a fully managed platform for building, deploying, and scaling your web apps. This script creates a Windows web app within the earlier defined service plan and resource group.

4. **SQL Server**: This is a fully managed relational database service in Azure that provides the broadest SQL Server engine compatibility. It allows you to manage your database without having to manage your server. 

5. **SQL Firewall Rule**: A firewall rule allows connections from specific IP addresses to your SQL server. This script creates a rule that allows all IP addresses to connect to the SQL Server.

6. **SQL Database**: The SQL Database is a fully managed and intelligent relational database service built for the cloud. It's a scalable service that can dynamically adapt to workload changes.

7. **Null Resource**: This is a resource that allows you to configure provisioners not directly associated with a single resource. This script uses a `null_resource` to execute a set of commands that set variables with the names of the resources created. These variables can be used in subsequent tasks in the pipeline.

Please note that this will incur charges on your Azure account.

## Cleaning Up

To destroy the resources created by Terraform, execute the `terraform-destroy.yml` pipeline. This will remove all resources created by this script and prevent further charges on your Azure account.