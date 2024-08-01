import json

def lib1 (event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lib1')
    }
