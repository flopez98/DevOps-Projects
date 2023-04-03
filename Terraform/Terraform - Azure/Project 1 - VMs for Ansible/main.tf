terraform {
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

resource "azurerm_resource_group" "main" {
  name = var.resource_group_name
  location = var.resource_group_location
}

resource "random_string" "server_name" {
  count  = 2
  length = 4
  special = false
}

module "vms" {
  source = "./Vms"
  vm_name = [
    "${random_string.server_name[0].result}",
    "${random_string.server_name[1].result}",
  ]
  resource_group_location = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  subnet_id = azurerm_subnet.main.id
}