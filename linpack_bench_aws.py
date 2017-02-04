import sys
import subprocess
import boto3
import time
from requests import get



ip = get('https://api.ipify.org').text
"""subprocess.run('aws ecr get-login > login.txt',shell=True)
subprocess.run('sh -e login.txt',shell=True)"""
num_nodes = 1
regions = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'eu-west-1', 'eu-west-2', 'eu-central-1',
           'ap-northeast-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1']
machine_types = ['t2.micro', 't2.small', 't2.medium', 't2.large']
region = regions[7]
client = boto3.client(
    'ecs',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name=regions[7]

)
response1 = client.create_cluster(
    clusterName='test'
)
ec2 = boto3.resource('ec2', region_name=regions[7])
""""
filename = region + 'TestKey.pem'
outfile = open(filename ,'w')
key_pair = ec2.create_key_pair(KeyName='TestKey'+region)
KeyPairOut = str(key_pair.key_material)
outfile.write(KeyPairOut)
"""
instances = ec2.create_instances(

    ImageId='ami-30bdce57',
    MinCount=1,
    MaxCount=1,
    KeyName="TestKey" + region,
    InstanceType=machine_types[0]
)
instance = instances[0]
instance.wait_until_running()
instance.load()
p_dns = instance.public_dns_name
f_dns = "ec2-user@" + p_dns
filename = region + 'TestKey.pem'
subprocess.run('ssh -i ' + filename + ' ' + f_dns, shell=True)
subprocess.run('curl http://169.254.169.254/latest/dynamic/instance-identity/document/ > id_doc.txt', shell=True)
subprocess.run('curl http://169.254.169.254/latest/dynamic/instance-identity/signature/ > id_sign.txt', shell=True)

""""
response2 = client.register_container_instance(
    cluster='test',
	totalResources=[
        {
            'name': 'cpu',
			'type': 'DOUBLE',
            'doubleValue': 123.0,
            'longValue': 123,
            'integerValue': 123,

        },
    ],

    attributes=[
        {
            'name': 'ecs.instance-type',
            'value': 't2.small'

        }
    ]
)
print(response2)

response2 = client.register_container_instance(
    cluster='test',
    instanceIdentityDocument='{"devpayProductCodes" : null,"privateIp" : "10.0.0.244","availabilityZone" : "ap-northeast-1c","version" : "2010-08-31","region" : "ap-northeast-1","pendingTime" : "2017-01-19T12:00:09Z","instanceId" : "i-09cbfdc4c952321f0","billingProducts" : null,"instanceType" : "t2.small","imageId" : "ami-30bdce57","accountId" : "998181420119","architecture" : "x86_64"}',
    instanceIdentityDocumentSignature= 'KVfqkNbNVb0Wi49Voh5dYT1+6iEM+i3fWz4jH45K9bEiqaSu5gns1gq+wmsPjdCxW+XHm0lOHz4rpfLoqKd0d8cHRMzeHRcw7p2/xfAMsqlNBi6DIYgTZYFzdh+B21zrmFjV7BzlBmLyfcWe23NgcrSyP2QympulymYXU02KhZI=',

    versionInfo={
        'agentVersion': '1.13.1',
        'agentHash': 'string',
        'dockerVersion': '1.12.6'
    },
	    totalResources=[
        {
            'name': 'CPU',
            'type': 'string',
            'doubleValue': 123.0,
            'longValue': 123,
            'integerValue': 123,
            'stringSetValue': [
                'string',
            ]
        },
    ],
    containerInstanceArn='arn:aws:ecr:ap-northeast-1:998181420119:repository/part1_sop',
    attributes=[
        {
            'name': 'string',
            'value': 'string',
            'targetType': 't2.small',
            'targetId': 'string'
        },
    ]
)

response3 = client.register_task_definition(
    family='test',
    networkMode='bridge',
    containerDefinitions=[
        {
            'name': '9dee399a-70ee-40da-82d7-7aee0344c104',
            'image': 'docker-whale',
            'cpu': 12*1024,
            'memory': 123,
            'memoryReservation': 123,
            'portMappings': [
                {
                    'containerPort': 123,
                    'hostPort': 123,
                    'protocol': 'tcp'|'udp'
                },
            ],
            'essential': True|False,
            'entryPoint': [
                'string',
            ],
            'command': [
                'string',
            ],
            'environment': [
                {
                    'name': 'string',
                    'value': 'string'
                },
            ],
            'mountPoints': [
                {
                    'sourceVolume': 'string',
                    'containerPath': 'string',
                    'readOnly': True|False
                },
            ],
            'volumesFrom': [
                {
                    'sourceContainer': 'string',
                    'readOnly': True|False
                },
            ],
            'hostname': 'string',
            'user': 'string',
            'workingDirectory': 'string',
            'disableNetworking': True|False,
            'privileged': True|False,
            'readonlyRootFilesystem': True|False,
            'dnsServers': [
                'string',
            ],
            'dnsSearchDomains': [
                'string',
            ],
            'extraHosts': [
                {
                    'hostname': 'string',
                    'ipAddress': 'string'
                },
            ],
            'dockerSecurityOptions': [
                'string',
            ],
            'dockerLabels': {
                'string': 'string'
            },
            'ulimits': [
                {
                    'name': 'core'|'cpu'|'data'|'fsize'|'locks'|'memlock'|'msgqueue'|'nice'|'nofile'|'nproc'|'rss'|'rtprio'|'rttime'|'sigpending'|'stack',
                    'softLimit': 123,
                    'hardLimit': 123
                },
            ],
            'logConfiguration': {
                'logDriver': 'json-file'|'syslog'|'journald'|'gelf'|'fluentd'|'awslogs'|'splunk',
                'options': {
                    'string': 'string'
                }
            }
        },
    ],
    volumes=[
        {
            'name': 'string',
            'host': {
                'sourcePath': 'string'
            }
        },
    ],
    placementConstraints=[
        {
            'type': 'memberOf',
            'expression': 'string'
        },
    ]
)
9dee399a-70ee-40da-8
9dee399a-70ee-40da-82d7-7aee0344c104
docker-whale

    totalResources=[
        {
            'name': 'CPU',
            'type': 'string',
            'doubleValue': 123.0,
            'longValue': 123,
            'integerValue': 123,
            'stringSetValue': [
                'string',
            ]
        },
    ],
"""
