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
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Added successfully',
        }

    return {  
        'msg': 'Some error occcured',
        'response': response
    }
    

def GetItem(id):
    try:
        response = MyTable.get_item(
            Key = {
                'id'     : id
            },
            AttributesToGet=[
                'model', 'color'
            ]
        )
        if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
            
            if ('Item' in response):
                return { 'Item': response['Item'] }

            return { 'msg' : 'Item not found!' }

        return {
            'msg': 'Some error occured',
            'response': response
        }
    except:
        response = {
        'msg': 'Some error occured',
        'response': "DB not exist"
    }
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
