import boto3

S3 = boto3.client('s3',
aws_access_key_id='$(Access_Key)',
aws_secret_access_key='$(Secret_Key)')

response = S3.list_objects_v2(Bucket='$(Bucket)',FetchOwner=True)

print(response)
keyList = []
modList = []
sizeList = []
ownerList = []
for i in response['Contents']:
    keyList.append(i['Key'])
    modList.append(i['LastModified'])
    sizeList.append(i['Size'])
    ownerList.append(i['Owner']['DisplayName'])


print(keyList)
print(ownerList)
