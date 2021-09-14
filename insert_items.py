import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('Patient_records_base')
def insert_items(UUID,Source,Status,Created_At,Notified_At,Resolved_At,Count,Last_Received,UUID_Pending,record_list,using_what):
    with table.batch_writer() as batch:
        batch.put_item(Item={"UUID": UUID, "Source": Source,
            "Status":Status,"Created_At": Created_At, "Notified_At": Notified_At, "Resolved_At": Resolved_At,
            "Last_Received": Last_Received,"Count": Count, "UUID_Pending": UUID_Pending })