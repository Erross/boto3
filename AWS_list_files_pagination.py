import boto3

S3 = boto3.client('s3',
aws_access_key_id='$(Access_Key)',
aws_secret_access_key='$(Secret_Key)')

paginator = S3.get_paginator('list_objects_v2')
page_iterator = paginator.paginate(Bucket='$(Bucket)',FetchOwner=True)

keyList = []
modList = []
sizeList = []
ownerList = []

for page in page_iterator:
    #print(page['Contents'])
    for i in page['Contents']:
        keyList.append(i['Key'])
        modList.append(str(i['LastModified']))
        sizeList.append(str(i['Size']))
        ownerList.append(i['Owner']['DisplayName'])

#returns lists of key, lastmodified, size and owner/displayname
#Iterates pages to return >1000 items which is max call