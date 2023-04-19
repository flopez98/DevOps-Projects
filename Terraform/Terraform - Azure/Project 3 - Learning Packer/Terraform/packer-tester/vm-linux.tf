data "azurerm_image" "aztf_ubuntu_image" {
  name                = "aztf-ubuntu"
  resource_group_name = "packer-rg"
}

module "linux_vm" {
  source = "../modules/vm/linux"

  name                = "linux-${random_string.main.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  subnet_id           = module.network.subnet_id
  vm_image_id         = data.azurerm_image.aztf_ubuntu_image.id
}