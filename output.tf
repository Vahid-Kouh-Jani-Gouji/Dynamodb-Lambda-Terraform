output "deliver_table_name" {
  description = "Name of the environment DynamoDB table"
  value       = aws_dynamodb_table.delivery.name
}

output "deliver_table_arn" {
  description = "ARN of the environment DynamoDB table"
  value       = aws_dynamodb_table.delivery.arn
}

output "base_url" {
  description = "Base URL for API Gateway stage."

  value = aws_apigatewayv2_stage.lambda.invoke_url
}