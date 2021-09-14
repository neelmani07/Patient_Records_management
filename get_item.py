import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('Patient_records_base')
def gett_with_both(UUID, Source):
    
    resp = table.get_item(Key={"UUID": UUID, "Source": Source})
    print(resp)
    if 'Item' in resp:
        record_dict=resp['Item']
        #print(type(record_dict))
        record_list=list(record_dict.values())
        #print("in gett",record_list)
        #print(record_list)
        return record_list
    else:
        return None
   
def gett_with_UUID(UUID):
    
    #resp = table.get_item(Key={"UUID": UUID, "Source": Source})
    resp = table.query(KeyConditionExpression=Key('UUID').eq(UUID))
    if resp['Items'] != []:
        print(resp['Items'])
        print(type(resp['Items']))
        record_dict=resp['Items'][0]
        record_list=list(record_dict.values())
        print("in gett")
        print(record_list)
        return record_list
    else:
        return None 