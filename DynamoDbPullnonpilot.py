import boto3
import json
from datetime import datetime, timedelta
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id='$(Access_Key)',
                              aws_secret_access_key='$(Secret_Key)',
                              region_name='us-east-2'

                              )
table = dynamodb.Table('$(tablename)')
now = datetime.now()
three_hours_ago = now - timedelta(days=1)
print(now)
print(three_hours_ago)
now = now.strftime('%F %T')
three_hours_ago = three_hours_ago.strftime('%F %T')
print(now)
print(three_hours_ago)
#date can be filtered if formatted YYYY-MM-DD HH:MM:SS
fe = Key('Date2').gt(three_hours_ago)
response = table.scan(FilterExpression=fe)
data = response['Items']
while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey']
                          ,FilterExpression=fe)
    data.extend(response['Items'])

x = []
for i in data:
    x.append(json.dumps(i))

print(len(x))