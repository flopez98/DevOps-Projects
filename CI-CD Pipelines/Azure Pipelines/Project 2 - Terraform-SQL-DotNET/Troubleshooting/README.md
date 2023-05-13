# Troubleshooting Guide for Azure Pipelines and Terraform Project

This guide provides solutions for common issues that you might encounter when using Azure Pipelines and Terraform in this project. 

## Issue: Pipeline Triggering Unexpectedly

**Symptom:** The pipeline is triggered by changes that should be ignored, such as changes to files in the 'Pipelines' and 'Terraform' folders.

**Possible Cause:** The trigger paths in the `azure-pipelines.yml` file might not be configured correctly.

**Solution:** Make sure that the `azure-pipelines.yml` file has the correct paths set in the `exclude` section under `paths`. Here's an example:

```yaml
trigger:
  branches:
    include:
    - main
  paths:
    exclude:
    - Pipelines
    - Terraform
    - Troubleshooting
```

## Issue: Terraform Locking Error

**Symptom:** Terraform fails to acquire a state lock, causing the pipeline to fail. The error message is: "Error acquiring the state lock".

**Possible Cause:** A previous Terraform operation might have failed or been interrupted, leaving the state locked.

**Solution:** You can manually unlock the state using the `terraform force-unlock` command, but this should be done with caution. A safer approach is to add an Azure Pipelines task that automatically forces unlock before running Terraform operations:

```yaml
- task: Bash@3
  inputs:
    targetType: 'inline'
    script: |
      # Write your commands here
                
      echo yes | terraform force-unlock LOCK-ID
    workingDirectory: '$(Build.SourcesDirectory)/Terraform'
```

## Issue: Terraform Scripts Not Found or Not Running Correctly

**Symptom:** Terraform scripts are not being found or not running as expected. The pipeline might fail during the Terraform steps, even though the Terraform files seem to be in the correct location.

**Possible Cause:** The `workingDirectory` specified for the Terraform tasks in the pipeline YAML might not be set to the correct path. The pipeline might be looking in the wrong directory for your Terraform scripts.

**Solution:** Make sure that the `workingDirectory` parameter for the Terraform tasks points to the correct directory where your Terraform files are located. In this project, the Terraform files are located in the 'Terraform' directory at the root of the repository. Therefore, the `workingDirectory` should be set to `'$(Build.SourcesDirectory)/Terraform'`.

```yaml
workingDirectory: '$(Build.SourcesDirectory)/Terraform'
```
## Issue: Deployment to Web App Task Failure

During the deployment phase, you may encounter a failure in the 'Deploy to Web App' task. This could occur due to several reasons, one of which may be due to not specifying the resource group that your web app belongs to.

#### Solution

In the Azure Web App task, specify the `resourceGroupName` and `deploymentMethod` as follows:

```yaml
- task: AzureWebApp@1
  inputs:
    azureSubscription: '$(ServicePrincipal)'
    resourceGroupName: $(rgpName) # *IMPORTANT*
    appType: 'webApp'
    appName: '$(appName)'
    package: '$(System.ArtifactsDirectory)/**/*.zip'
    deploymentMethod: runFromPackage # *IMPORTANT*
```

The `resourceGroupName` property is important to accurately direct the deployment to the right Azure resource group.

Additionally, using `deploymentMethod: runFromPackage` optimizes the time taken for the app service to restart and the changes to take effect as the package is directly mounted to the wwwroot folder.

## Issue: Trouble Referencing Environment Variables

This issue arises when you try to reference environment variables set by the Terraform script in subsequent stages of the Azure DevOps pipeline.

The problem lies in the Azure DevOps pipelines scope for referencing variables. Variables created in one job can't be referenced in subsequent jobs. However, they can be referenced in subsequent stages.

#### Solution

1. Use a `null_resource` with a `local-exec` provisioner in your Terraform file to set output variables using the `##vso[task.setvariable]` command:

    ```hcl
    resource "null_resource" "terraform-to-devops-vars" {
      triggers = {
        // always execute
        uuid_trigger = uuid()    
      }
      provisioner "local-exec" {
        command = <<EOT
          Write-Host "##vso[task.setvariable variable=SQL_SERVER_NAME;isOutput=true]${azurerm_mssql_server.sqlserver94569834.name}.database.windows.net"
          Write-Host "##vso[task.setvariable variable=RGP_NAME;isOutput=true]${azurerm_resource_group.az-test-webapp.name}"
          Write-Host "##vso[task.setvariable variable=APP_NAME;isOutput=true]${azurerm_windows_web_app.newapp59804305.name}"
          EOT
        interpreter = ["Powershell", "-Command"]
      }
    }
    ```

2. Ensure the task where the output variable is set has a `name` property. This is used to reference the task in subsequent stages. Here is an example:

    ```yaml
    - stage: TerraformStage
      jobs:
        - job: Infrastructure
          steps:
            - task: SampleTask@0
              name: setvarStep
    ```

    In the example above, `setvarStep` is the name of the task, and it is used when referencing the output variables in subsequent stages. Replace `setvarStep` with the actual name of your task.

3. Reference the output variables in subsequent stages using the `stageDependencies.<stageName>.<jobName>.outputs['<taskName>.<variableName>']` syntax. In this case, `<stageName>` is the name of the stage where the variable is set, `<taskName>` is the name of the task where the variable is set, and `<variableName>` is the name of the output variable:

    ```yaml
    - stage: NextStage
      dependsOn: TerraformStage
      jobs:
        - job: NextJob
          variables:
            rgpName: $[stageDependencies.TerraformStage.Infrastructure.outputs['setvarStep.RGP_NAME']]
            appName: $[stageDependencies.TerraformStage.Infrastructure.outputs['setvarStep.APP_NAME']]
            sqlServerName: $[stageDependencies.TerraformStage.Infrastructure.outputs['setvarStep.SQL_SERVER_NAME']]
    ```

This approach allows you to use environment variables set by the Terraform script in other stages of your Azure DevOps pipeline.

**Additional Information:** The official Microsoft documentation on [Output variables](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops&tabs=yaml%2Cbatch#output-variables) provides more details on this topic.

---

Remember, this guide is a living document. As we encounter new issues and solutions, we'll continue to update it. Contributions are welcome. If you have solutions for issues not yet documented, feel free to submit a pull request.