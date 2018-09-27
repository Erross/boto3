import swigpython3 as pilotbase  # for bare-metal stuff
import pilotpython  # nicer python classes
import boto3


def onInitialize(ctxt):
    context = pilotpython.Context(ctxt)
    return pilotpython.READY_FOR_INPUT_OR_NEW_DATA


def onProcess(ctxt, dr):
    context = pilotpython.Context(ctxt)
    data = pilotpython.DataRecord(dr)
    props = data.getProperties()

    S3 = boto3.client('s3',
                      aws_access_key_id='$(Access_Key)',
                      aws_secret_access_key='$(Secret_Key)')

    response = S3.list_objects_v2(Bucket='$(Bucket)', FetchOwner=True)

    keyList = []
    modList = []
    sizeList = []
    ownerList = []
    for i in response['Contents']:
        keyList.append(i['Key'])
        modList.append(str(i['LastModified']))
        sizeList.append(str(i['Size']))
        ownerList.append(i['Owner']['DisplayName'])

    print(keyList)

    props.defineStringArrayProperty("Key", keyList)
    props.defineStringArrayProperty("LastModified", modList)
    props.defineStringArrayProperty("Size", sizeList)
    props.defineStringArrayProperty("Owner", ownerList)

    context = pilotpython.Context(ctxt)
    return pilotpython.READY_FOR_INPUT_OR_NEW_DATA


def onFinalize(ctxt):
    context = pilotpython.Context(ctxt)
    None
