data "azurerm_image" "windows_image" {
  name                = "aztf-w2016"
  resource_group_name = "packer-rg"
}

resource "random_password" "password" {
  length           = 16
  special          = true
  override_special = "!#$%&*()-_=+[]{}<>:?"
}

resource "local_file" "foo" {
  content  = random_password.password.result
  filename = "${path.module}/password.txt"
}

module "windows_vm" {
  source = "../modules/vm/windows"

  name                = "win-${random_string.main.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  subnet_id           = module.network.subnet_id
  vm_image_id         = data.azurerm_image.windows_image.id
  admin_password      = random_password.password.result
}