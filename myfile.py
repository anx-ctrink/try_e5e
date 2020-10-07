def myfunction(event, context):
    return {
        'response_headers': {
            'x-sent-content-type': event['request_headers'].get('content-type', '*/*'),
        },
        'data': 'Hello world!',
    }
