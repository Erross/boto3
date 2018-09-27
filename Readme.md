# boto3 approaches to AWS interactions with pipeline pilot - for python 3.5 implementation in pipeline pilot

## Pilot Generic DynamoDb Insert

This will insert a single pilot record into a named dynamodb table - globals on the component are used to pass in AWS keys, Region and table names

## translate
Send text to AWS translate and return the translation

## Pilot Translate

Translate text input from pilot global using AWS translate and return as property 'translated'

## AWS list files

List files in a named bucket - file name, size, owner, last modified date

##Pilot list objects in S3 bucket
AWS list files implemented in pilot - runs faster than out of the box AWS components from accelrys website