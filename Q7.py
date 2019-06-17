import boto3,json

def create_role(iam,path):
    role_name='rahul'
    description='A test role'
    trust_policy={
  			"Version": "2012-10-17",
  			"Statement": [
    			{
      				"Sid": "",
      				"Effect": "Allow",
      				"Principal": {
        			"Service": "ec2.amazonaws.com"
      				},
      				"Action": "sts:AssumeRole"
    			}
  		]
		}

    tags=[
      {
        'Key': 'Environment',
        'Value': 'Production'
      }
    ]
    try:
        response = iam.create_role(
        Path=path,
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(trust_policy),
        Description=description,
        MaxSessionDuration=3600,
        Tags=tags
       )

        print(response)
        return(role_name)
    except Exception as e:
        print(e)



def create_policy(iam):
    # Create a policy
    my_managed_policy ={
    			"Version": "2012-10-17",
    			"Statement": [
        			{
            				"Effect": "Allow",
            				"Action": "s3:*",
            				"Resource": "*"
        			}
    			     ]
			} 

    response = iam.create_policy(
    PolicyName='mys3_rahul',
    PolicyDocument=json.dumps(my_managed_policy)
    )
    print(response)
    return(response)



def attach_policy(iam,resp_json,role_name):
   # Attach a role policy
    iam.attach_role_policy(
    PolicyArn=resp_json['Policy']['Arn'],
    RoleName=role_name
    )

def instance_profile(iam,path):
    instance_profile = iam.create_instance_profile(InstanceProfileName='Rahul-Profile',Path=path)
    print(instance_profile)
    response = client.associate_iam_instance_profile(
    IamInstanceProfile={
        'Arn': instance_profile['InstanceProfile']['Arn'],
        'Name': 'Rahul-Profile'
    },
    InstanceId=''
    )

def connection_ec2:
    pass
#I have done it through AWS commandLine 
#I have to try it doing with boto3



if __name__=='__main__':
    
    iam=boto3.client('iam')
    path='/'
    ec2=boto3.client('ec2')
    role_name=create_role(iam,path)
    resp_json=create_policy(iam)
    attach_policy(iam,resp_json,role_name)
    instance_profile(iam,path)
