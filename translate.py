import boto3

translate = boto3.client('translate',
    aws_access_key_id='$(Access_Key)',
    aws_secret_access_key='$(Secret_Key')

    )

response = translate.translate_text(
    Text='你好,世界',
    SourceLanguageCode='Auto',
    TargetLanguageCode='En'
)

print(response['TranslatedText'])
#print(response.keys())

#print(response['Items'])
#x = 0
#for i in response['Items']:
#    print (i)
