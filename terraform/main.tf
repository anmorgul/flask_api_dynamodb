provider "aws" {
    access_key = "${var.aws_access_key}"
    secret_key = "${var.aws_secret_key}"
    region = "${var.aws_region}"
}

resource "aws_dynamodb_table" "my_first_table" {
  name        = "${var.table_name}"
  billing_mode = "${var.table_billing_mode}"
  read_capacity  = 2
  write_capacity = 2
  hash_key       = "id"
  attribute {
    name = "id"
    type = "S"
  }
   tags = {
    environment       = "${var.environment}"
  }
}