import json

def hello_world_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
