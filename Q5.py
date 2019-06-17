import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    s3=boto3.resource('s3')
    cpy_src={'Bucket':'mybucket-q3','Key':'S3_sample-Q2.txt'}
    dest_bucket=s3.Bucket('austin-pe-ques2')
    dest_bucket.copy(cpy_src,'S3_sample-Q2-copy.txt')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

