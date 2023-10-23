# resource "random_pet" "table_name" {
#   prefix    = "delivery"
#   separator = "_"
#   length    = 4
# }

resource "aws_dynamodb_table" "delivery" {
  name         = "delivery"
  billing_mode = "PAY_PER_REQUEST"

  hash_key  = "id"

  
  attribute {
    name = "id"
    type = "S"
  }

 
  
}
