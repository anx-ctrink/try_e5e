import base64
 
def myfunction(event, context):
    input_binary = base64.b64decode(event['data']['binary'])
    output_binary = bytes(map(lambda b: b ^ 255, input_binary))
    return {
        'type': 'binary',
        'data': {
            'binary': base64.b64encode(output_binary).decode('ascii'),
            'name': 'output.blob',
            'content_type': 'x-my-first-function/blob',
        },
    }
