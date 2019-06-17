import boto3

s3 = boto3.client('s3')
s3.download_file('mybucket, 'hello.txt', '/tmp/hello.txt', ExtraArgs={'VersionId': })
