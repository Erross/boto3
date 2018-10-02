import boto3
import json

dynamodb = boto3.client('dynamodb',
                        aws_access_key_id='$(Access_Key)',
                        aws_secret_access_key='$(Secret_Key)',
                        region_name='$(Region_Name)'
                        )
x = []
response = dynamodb.scan(TableName='$(Table)')
for i in response['Items']:
    x.append(json.dumps(i))