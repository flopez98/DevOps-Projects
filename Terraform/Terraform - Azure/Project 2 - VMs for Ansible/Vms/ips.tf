# Creating a public IP for each VM
resource "azurerm_public_ip" "public_ip" {
  count               = length(var.vm_name)
  name                = "ip-${var.vm_name[count.index]}"
  resource_group_name = var.resource_group_name
  location            = var.resource_group_location
  allocation_method   = "Dynamic"
}
