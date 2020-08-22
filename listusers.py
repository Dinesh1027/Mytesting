import boto3
import sys

region = sys.argv[1]
accesskey = sys.argv[2]
secretkey = sys.argv[3]

IAM_commands_only=boto3.client('iam',region_name=region,aws_access_key_id=accesskey,aws_secret_access_key=secretkey)
list_user_response=IAM_commands_only.list_users()

for i in list_user_response['Users']:
	print(i['UserName'],i['CreateDate'])
