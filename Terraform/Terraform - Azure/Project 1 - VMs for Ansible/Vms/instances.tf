#Creating VMs
resource "azurerm_linux_virtual_machine" "main" {
  for_each = { for idx, name in var.vm_name : idx => name }
  name                = "vm-${each.value}"
  resource_group_name = var.resource_group_name
  location            = var.resource_group_location
  size                = "Standard_B2s"
  admin_username      = "adminuser"
  network_interface_ids = [
    azurerm_network_interface.nic[each.key].id,
  ]

  admin_ssh_key {
    username   = "adminuser"
    public_key = file("~/.ssh/id_rsa.pub")
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "16.04-LTS"
    version   = "latest"
  }

  depends_on = [
    azurerm_network_interface.nic
  ]
}
