resource "azurerm_network_interface" "myterraformnic" {
  name                = "${var.application_type}-${var.resource_type}-netint"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${var.public_ip_address_id}"
  }
}

resource "azurerm_linux_virtual_machine" "myterraformvm" {
  name                = "${var.vm_name}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "Standard_DS1_v2"
  admin_username      = "${var.admin_user}"
  network_interface_ids = [azurerm_network_interface.myterraformnic.id]
  admin_ssh_key {
    username   = "${var.user_name}"
    public_key = "${file("id_rsa.pub")}"
  }

  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "16.04-LTS"
    version   = "latest"
  }
}