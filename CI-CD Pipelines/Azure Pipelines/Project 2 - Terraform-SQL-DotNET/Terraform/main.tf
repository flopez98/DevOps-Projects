terraform {
  backend "azurerm" {}

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.46.0"
    }
  }
}


provider "azurerm" {
  features {

  }
}

resource "random_string" "name" {
  length  = 8
  lower   = true
  numeric = false
  special = false
  upper   = false
}


resource "azurerm_resource_group" "az-test-webapp" {
  name     = "az-test-rgp-${random_string.name.result}"
  location = "East Us"
}

resource "azurerm_service_plan" "plan67532" {
  name                = "plan${random_string.name.result}"
  resource_group_name = azurerm_resource_group.az-test-webapp.name
  location            = azurerm_resource_group.az-test-webapp.location
  os_type             = "Windows"
  sku_name            = "F1"
}

resource "azurerm_windows_web_app" "main" {
  name                = "app${random_string.name.result}"
  resource_group_name = azurerm_resource_group.az-test-webapp.name
  location            = azurerm_resource_group.az-test-webapp.location
  service_plan_id     = azurerm_service_plan.plan67532.id

  site_config {
    always_on = false
    application_stack {
      current_stack  = "dotnet"
      dotnet_version = "v6.0"
    }
  }
  depends_on = [
    azurerm_service_plan.plan67532
  ]

}

resource "azurerm_mssql_server" "main" {
  name                         = "sqlserver${random_string.name.result}"
  resource_group_name          = azurerm_resource_group.az-test-webapp.name
  location                     = azurerm_resource_group.az-test-webapp.location
  version                      = "12.0"
  administrator_login          = "4dm1n157r470r"
  administrator_login_password = "4-v3ry-53cr37-p455w0rd"
}

resource "azurerm_mssql_firewall_rule" "example" {
  name             = "FirewallRule1"
  server_id        = azurerm_mssql_server.main.id
  start_ip_address = "0.0.0.0"
  end_ip_address   = "0.0.0.0"
}

resource "azurerm_mssql_database" "appdb" {
  name         = "appdb"
  server_id    = azurerm_mssql_server.main.id
  collation    = "SQL_Latin1_General_CP1_CI_AS"
  license_type = "LicenseIncluded"
  max_size_gb  = 2
  sku_name     = "basic"
  depends_on = [
    azurerm_mssql_server.main
  ]

}

resource "null_resource" "terraform-to-devops-vars" {
   triggers = {
        // always execute
        uuid_trigger = uuid()    
   }
   provisioner "local-exec" {
    command = <<EOT
      Write-Host "##vso[task.setvariable variable=SQL_SERVER_NAME;isOutput=true]${azurerm_mssql_server.main.name}.database.windows.net"
      Write-Host "##vso[task.setvariable variable=RGP_NAME;isOutput=true]${azurerm_resource_group.az-test-webapp.name}"
      Write-Host "##vso[task.setvariable variable=APP_NAME;isOutput=true]${azurerm_windows_web_app.main.name}"
      EOT
    interpreter = ["Powershell", "-Command"]
  }

  depends_on = [
    azurerm_mssql_server.main
  ]
}