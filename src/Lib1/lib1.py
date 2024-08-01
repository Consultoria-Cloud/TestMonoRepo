import json

def lib1 (event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda 1! Version v1.0.0')
    }
