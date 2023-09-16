terraform {
  required_providers {
    azuredevops = {
      source = "microsoft/azuredevops"
      version = "0.9.1"
    }
  }
}

provider "azuredevops" {
  org_service_url        = var.org_service_url
  personal_access_token  = var.personal_access_token
}

resource "azuredevops_variable_group" "var1" {
  project_id   = var.project_id
  name         = "Terraform"
  description  = ""
  allow_access = false

  variable {
    name  = "backendAzureRmContainerName"
    value = ""
  }
  variable {
    name  = "backendAzureRmKey"
    value = ""
  }

  variable {
    name  = "backendAzureRmResourceGroupName"
    value = ""
  }
  variable {
    name  = "backendAzureRmStorageAccountName"
    value = ""
  }

  variable {
    name  = "backendServiceArm"
    value = ""
  }
}

resource "azuredevops_variable_group" "var2" {
  project_id   = var.project_id
  name         = "sql-credentials"
  description  = ""
  allow_access = false

  variable {
    name  = "SqlPassword"
    value = ""
  }
  variable {
    name  = "SqlUsername"
    value = ""
  }
}

resource "azuredevops_variable_group" "var3" {
  project_id   = var.project_id
  name         = "shared-vars"
  description  = ""
  allow_access = false

  variable {
    name  = "skipBuildStage"
    value = "false"
  }
  variable {
    name  = "skipTerraformStage"
    value = "false"
  }

  variable {
    name  = "ServicePrincipal"
    value = "Azure sub"
  }
  variable {
    name  = "solution"
    value = "**/*.sln"
  }

  variable {
    name  = "buildPlatform"
    value = "Any CPU"
  }
  variable {
    name  = "buildConfiguration"
    value = "Release"
  }
}