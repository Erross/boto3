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
    session = boto3.Session(
        aws_access_key_id='$(Access_Key)',
        aws_secret_access_key='$(Secret_Key)'
    )
    Folder_Path = '$(Folder_Path)'
    s3 = session.resource('s3')
    your_bucket = s3.Bucket('$(Bucket Name)')
    objlist = []
    for x in your_bucket.objects.all():
        if Folder_Path in x.key:
            objlist.append(x.key)
    props.defineStringArrayProperty("Object", objlist)
    props.defineStringProperty("path", Folder_Path)

    context = pilotpython.Context(ctxt)
    return pilotpython.READY_FOR_INPUT_OR_NEW_DATA


def onFinalize(ctxt):
    context = pilotpython.Context(ctxt)
    None
