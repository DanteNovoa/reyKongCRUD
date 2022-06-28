import boto3

db = boto3.resource('dynamodb', region_name='us-east-1')
table = db.Table('signuptable')

response = table.get_item(Key={'email': 'dante@test.com'})

putItem = table.put_item(
    Item={
        'email':  'dante@test2.com',
        'first_name': 'dante2',
        'last_name': 'test_dante',
        'mobile': 2323232,
        'country': 'US',
        'newsletter': False,
        'club': 'Krakens'
    }
)

update = table.update_item(
    Key={'email': 'dante@test.com'},
    UpdateExpression='set first_name = :val',
    ExpressionAttributeValues={':val': 'updatedante'}
)