variable "aws_access_key" {
  type = string
}

variable "aws_secret_key" {
  type = string
}

variable "aws_region" {
  type        = string
  description = "AWS region"
  default     = "eu-central-1"
}

variable "table_name" {
  type        = string
  default     = "my_table"
}

variable "table_billing_mode" {
  type        = string
  default     = "PROVISIONED"
}

variable "environment" {
  type        = string
  default     = "dev"
}