resource "azurerm_resource_group" "main" {
  name     = "packer-rg"
  location = var.location
}