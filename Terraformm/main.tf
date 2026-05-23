# 1. Tell Terraform to use Azure
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# 2. Create an Azure Resource Group (The folder for all cloud resources)
resource "azurerm_resource_group" "rg" {
  name     = "hackathon-healthcare-rg"
  location = "East US"
}

# 3. Create a Virtual Network (VNet) for security
resource "azurerm_virtual_network" "vnet" {
  name                = "hackathon-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

# 4. Create a dedicated Subnet for our Container Apps
resource "azurerm_subnet" "subnet" {
  name                 = "aca-subnet"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}

# 5. Create the Azure Container Registry (ACR) to hold your Python Docker Images
resource "azurerm_container_registry" "acr" {
  name                = "hackathonregistry${random_string.unique.result}" # Needs a unique name
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = true
}

# Helper tool to generate a unique name for your container registry
resource "random_string" "unique" {
  length  = 6
  special = false
  upper   = false
}

# 6. Create the Azure Container Apps Environment (The cluster workspace)
resource "azurerm_container_app_environment" "env" {
  name                       = "hackathon-aca-env"
  location                   = azurerm_resource_group.rg.location
  resource_group_name        = azurerm_resource_group.rg.name
  infrastructure_subnet_id   = azurerm_subnet.subnet.id
}

# 7. Create Application Insights for your Monitoring Requirement
resource "azurerm_application_insights" "insights" {
  name                = "hackathon-app-insights"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  application_type    = "web"
}