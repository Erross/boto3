import swigpython3 as pilotbase  # for bare-metal stuff
import pilotpython  # nicer python classes
import boto3
from botocore.exceptions import ClientError


def onInitialize(ctxt):
    context = pilotpython.Context(ctxt)
    return pilotpython.READY_FOR_INPUT_OR_NEW_DATA


def onProcess(ctxt, dr):
    # First Bit here is pilot required, probably#
    context = pilotpython.Context(ctxt)
    data = pilotpython.DataRecord(dr)
    records = data.getProperties()
    parameters = context.getComponentParameters()
    # Next Bit is my code#
    client = boto3.client('dynamodb', region_name='us-east-2', aws_access_key_id='$(Access_Key)',
                          aws_secret_access_key='$(Secret_Key)')
    props = data.getProperties()
    numProperties = props.getSize()

    insertitem = {}

    for p in range(numProperties):
        thisP = props.getByIndex(p)
        thisName = thisP.getName()
        thisValue = str(thisP.getValue().getString())
        insertitem[thisName] = {"S": thisValue}

    try:
        client.put_item(
            TableName="$(DynamoTable)",
            Item=
            insertitem

        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("User already exists")
        else:

            props.defineStringProperty("Error", "Unexpected error: %s" % e)

    # next bit defines outputs#
    props.defineStringProperty("Done", "Done")
    props.defineStringProperty("Did", x)
    context = pilotpython.Context(ctxt)
    # next bit triggers next data input probably#
    return pilotpython.READY_FOR_INPUT_OR_NEW_DATA


def onFinalize(ctxt):
    context = pilotpython.Context(ctxt)
    response =
    None
