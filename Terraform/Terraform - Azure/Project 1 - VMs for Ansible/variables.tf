variable "resource_group_name" {
  type = string
  description = "Resource Group Name"
}

variable "resource_group_location" {
  type = string
  default = "East Us"
  description = "Resource Group Location"
}

variable "vnet_name" {
  type = string
}

variable "subnet_name" {
  type = string
}
