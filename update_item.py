import boto3
import decimal
from datetime import date

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('Patient_records_base')



def date_to_integer(date_input):
    return 10000*date_input.year + 100*date_input.month + date_input.day
    
today = date_to_integer(date.today())

def update_entry(UUID, Source):
    try:
        resp = table.update_item(
            Key={"UUID": UUID , "Source": Source},
            
            ConditionExpression="attribute_exists(#Count)",
            ExpressionAttributeNames={
                #"#Status": "Status",
                "#Count": "Count",
                #"#UUID_P": "UUID_Pending", 
            },
            
            ExpressionAttributeValues={
                ':v': decimal.Decimal(1),
                #':p': UUID ,
            },
            
            UpdateExpression="SET #Count = #Count+:v" , #UUID_P = if_exists(#Status.eq('Pending'), :p)"
            
        )
    except Exception as msg:
        
        
        table.put_item(Item={"UUID": UUID, "Source": Source,
            "Status":"Pending","Created_At":today , "Notified_At":0000 , "Resolved_At":0000,
            "Last_Received":today ,"Count": 1, "UUID_Pending": UUID })
        
        print(f"Oops, could not update: {msg} so created a new entry")
        
        
        
        
        
        
        
        
        
        
        
        
        
    '''
        Key={'ReleaseNumber': '1.0.179'},
        UpdateExpression='SET #attr1 = :val1',
        ConditionExpression=Attr('ReleaseNumber').eq('1.0.179'),
        ExpressionAttributeNames={'#attr1': 'val1'},
        ExpressionAttributeValues={':val1': 'false'}
        
        
        Key={
        'ReleaseNumber': releaseNumber,
        'Timestamp': result[0]['Timestamp']
        },
        UpdateExpression="set Sanity = :r",
        ExpressionAttributeValues={
            ':r': 'false',
        },
        ReturnValues="UPDATED_NEW"
        '''