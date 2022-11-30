from asyncio import events
import json
<<<<<<< HEAD
from urllib import request


def handler(event, context):
    print("request: {}".format(json.dumps(event)))
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": "Hello, CDK! You have hit {}\n".format(event["path"]),
    }
=======
from urllib import request 


def handler(event, context)
    print('request: { }' .format(json.dumps(event))
          return {
              'statusCode': 200,
              'headers': {
                  'Content-Type': 'text/plain'
                  },
              'body': 'Hello, CDK! You have hit {}/n' .format(event['path'])
          }
>>>>>>> 3ce3f16 (Added all directores and files needed to edit code)
