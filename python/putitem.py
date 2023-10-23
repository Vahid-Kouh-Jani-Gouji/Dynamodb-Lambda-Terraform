import json
import boto3
import os
from uuid import uuid4


# Initialize the DynamoDB 
dynamodb = boto3.client('dynamodb', region_name='eu-central-1')


# Define the DynamoDB table name
dynamodb_table = 'delivery'


def lambda_handler(event, context):
    
   body = json.loads(event["body"])
   name = body.get("name", "Name not provided")
   email = body.get("email", "Email not provided")

   # Generate a unique ID for the DynamoDB item
   unique_id = str(uuid4())
    
   
    
   # Save information to DynamoDB
   dynamodb.put_item(
       TableName=dynamodb_table,
       Item={
           'id': {'S': unique_id},
           'name': {'S': name},
           'email': {'S': email},
          
       }
   )

   
    
 
   # You can customize the response as needed
   response = {
       "statusCode": 200,
       "body": json.dumps(event),
   }

   return response