import boto3
from boto3.dynamodb.conditions import Key
import get_item as g
import update_item as u
import insert_items as i

#add_new_entry('b703ca7b-b8a1-4d61-912e-c9ea32d91e8890','EOrbtio AsiallP')
UUID,Source='b703ca7b-b8a1-4d61-912e-c9ea32d91e82','Orbtio Japan'
u.update_entry(UUID, Source)