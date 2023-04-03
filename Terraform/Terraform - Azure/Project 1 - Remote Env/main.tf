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

#Creating a resource group
resource "azurerm_resource_group" "az-rgp" {
  name     = "az-dev-rgp"
  location = "East Us"
  tags = {
    environment = "Dev"
  }
}

#Creating a virtual network
resource "azurerm_virtual_network" "az-vnet" {
  name                = "az-vnet-dev"
  location            = azurerm_resource_group.az-rgp.location
  resource_group_name = azurerm_resource_group.az-rgp.name
  address_space       = ["10.0.0.0/16"]

  tags = azurerm_resource_group.az-rgp.tags
}

#Creating subnet within the previous virtual network
resource "azurerm_subnet" "az-subnet-001" {
  name                 = "az-subnet-001"
  resource_group_name  = azurerm_resource_group.az-rgp.name
  virtual_network_name = azurerm_virtual_network.az-vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}

#Deploying a network security group for the subnet
resource "azurerm_network_security_group" "az-dev-security-grp" {
  name                = "az-dev-security-grp"
  location            = azurerm_resource_group.az-rgp.location
  resource_group_name = azurerm_resource_group.az-rgp.name

  tags = azurerm_resource_group.az-rgp.tags
}

#Creating a rule for the NSG
resource "azurerm_network_security_rule" "az-dev-rule1" {
  name                        = "az-dev-rule1"
  priority                    = 100
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "*"
  source_port_range           = "*"
  destination_port_range      = "*"
  source_address_prefix       = "*" ##Optional - Rename to your personal IP for better security 0.0.0.0/32
  destination_address_prefix  = "*"
  resource_group_name         = azurerm_resource_group.az-rgp.name
  network_security_group_name = azurerm_network_security_group.az-dev-security-grp.name
}

#Associating the NSG with the subnet
resource "azurerm_subnet_network_security_group_association" "az-dev-association" {
  subnet_id                 = azurerm_subnet.az-subnet-001.id
  network_security_group_id = azurerm_network_security_group.az-dev-security-grp.id
}

#Creating a public IP for a VM
resource "azurerm_public_ip" "az-dev-pip" {
  name                = "az-dev-pip"
  resource_group_name = azurerm_resource_group.az-rgp.name
  location            = azurerm_resource_group.az-rgp.location
  allocation_method   = "Dynamic"

  tags = azurerm_resource_group.az-rgp.tags
}

#Creating a NIC for the VM
resource "azurerm_network_interface" "az-dev-nic" {
  name                = "az-dev-nic"
  location            = azurerm_resource_group.az-rgp.location
  resource_group_name = azurerm_resource_group.az-rgp.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.az-subnet-001.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.az-dev-pip.id
  }

  tags = azurerm_resource_group.az-rgp.tags
}

#Creating a virtual machine
resource "azurerm_linux_virtual_machine" "az-dev-vm" {
  name                = "az-dev-vm"
  resource_group_name = azurerm_resource_group.az-rgp.name
  location            = azurerm_resource_group.az-rgp.location
  size                = "Standard_F2"
  admin_username      = "adminuser"
  network_interface_ids = [
    azurerm_network_interface.az-dev-nic.id,
  ]

  custom_data = filebase64("customdata.tpl")

  admin_ssh_key {
    username   = "adminuser"
    public_key = file("~/.ssh/azdevkey.pub")
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

  provisioner "local-exec" {
    command = templatefile("${var.host_os}-ssh-script.tpl", {
      hostname = self.public_ip_address,
      user = "adminuser",
      identityfile = "~/.ssh/azdevkey"
    })
    interpreter = var.host_os == "windows" ? ["Powershell", "-Command"] : ["bash", "-c"]
  }

  tags = azurerm_resource_group.az-rgp.tags
}

#Getting data and output
data "azurerm_public_ip" "az-dev-ipdata" {
  name = azurerm_public_ip.az-dev-pip.name
  resource_group_name = azurerm_resource_group.az-rgp.name
}

output "public_ip_address" {
  value = "${azurerm_linux_virtual_machine.az-dev-vm.name}: ${data.azurerm_public_ip.az-dev-ipdata.ip_address}"
}