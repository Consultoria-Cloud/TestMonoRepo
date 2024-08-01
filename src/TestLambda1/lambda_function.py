import json
from libs.lib1 import lib1

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda 1! Version v1.0.0')
    }

lib1 ()