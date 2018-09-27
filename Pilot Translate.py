import swigpython3 as pilotbase  # for bare-metal stuff
import pilotpython  # nicer python classes
import boto3


def onInitialize(ctxt):
    context = pilotpython.Context(ctxt)
    return pilotpython.READY_FOR_INPUT_OR_NEW_DATA


def onProcess(ctxt, dr):
    # First Bit here is pilot required, probably#
    context = pilotpython.Context(ctxt)
    data = pilotpython.DataRecord(dr)
    props = data.getProperties()
    # Next Bit is my code#

    translate = boto3.client('translate',
                             aws_access_key_id='$(Access_Key)',
                             aws_secret_access_key='$(Secret_Key)'
                             )

    response = translate.translate_text(
        Text='$(Text to Translate)',
        SourceLanguageCode='$(SourceLanguage)',
        TargetLanguageCode='$(TargetLanguage)'
    )

    # next bit defines outputs#
    props.defineStringProperty("Translated", response['TranslatedText'])
    # props.defineStringProperty("Argh", e)
    context = pilotpython.Context(ctxt)
    # next bit triggers next data input probably#
    return pilotpython.READY_FOR_INPUT_OR_NEW_DATA


def onFinalize(ctxt):
    context = pilotpython.Context(ctxt)
    None
