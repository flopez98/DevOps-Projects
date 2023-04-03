#Creating a NIC for the VM
resource "azurerm_network_interface" "nic" {
  count               = length(var.vm_name)
  name                = "nic-${var.vm_name[count.index]}"
  location            = var.resource_group_location
  resource_group_name = var.resource_group_name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.public_ip[count.index].id
  }

  depends_on = [
    azurerm_public_ip.public_ip
  ]
}