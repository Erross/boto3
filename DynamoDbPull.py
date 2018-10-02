import swigpython3 as pilotbase  # for bare-metal stuff
import pilotpython  # nicer python classes
import boto3
import json


def onInitialize(ctxt):
    context = pilotpython.Context(ctxt)
    return pilotpython.READY_FOR_INPUT_OR_NEW_DATA


def onProcess(ctxt, dr):
    # First Bit here is pilot required, probably#
    context = pilotpython.Context(ctxt)
    data = pilotpython.DataRecord(dr)
    props = data.getProperties()
    # Next Bit is my code#

    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id='$(Access_Key)',
                              aws_secret_access_key='$(Secret_Key)',
                              region_name='$(Region_Name)'

                              )
    table = dynamodb.Table('$(Table)')
    response = table.scan()
    data = response['Items']
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    x = []
    for i in data:
        x.append(json.dumps(i))

    props.defineStringArrayProperty("Done", x)
    # props.defineStringProperty("Argh", e)
    context = pilotpython.Context(ctxt)
    # next bit triggers next data input probably#
    return pilotpython.READY_FOR_INPUT_OR_NEW_DATA


def onFinalize(ctxt):
    context = pilotpython.Context(ctxt)
    None
