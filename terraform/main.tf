provider "aws" {
    access_key = "${var.aws_access_key}"
    secret_key = "${var.aws_secret_key}"
    region = "eu-west-3"
}

resource "aws_dynamodb_table" "my_first_table" {
  name        = "${var.table_name}"
  billing_mode = "${var.table_billing_mode}"
  read_capacity  = 2
  write_capacity = 2
  hash_key       = "Id"
  attribute {
    name = "Id"
    type = "N"
  }
   tags = {
    environment       = "${var.environment}"
  }
}