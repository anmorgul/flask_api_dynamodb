from boto3 import resource
from config import Config

AWS_ACCESS_KEY_ID = Config.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = Config.AWS_SECRET_ACCESS_KEY
REGION_NAME = Config.REGION_NAME
 
resource = resource(
   'dynamodb',
   aws_access_key_id     = AWS_ACCESS_KEY_ID,
   aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
   region_name           = REGION_NAME
)

MyTable = resource.Table('my_table')

def addItem(id, model, color):
    response = MyTable.put_item(
        Item = {
            'id'     : id,
            'model'  : model,
            'color' : color
        }
    )
    return response

def GetItem(id):
    response = MyTable.get_item(
        Key = {
            'id'     : id
        },
        AttributesToGet=[
            'model', 'color'
        ]
    )
    return response

def GetItems():
    response = MyTable.scan()
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        print(response['ResponseMetadata']['HTTPStatusCode'])
        data = response.get('Items')
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])
        return data

    return {
        'msg': 'Some error occured',
        'response': response
    }
