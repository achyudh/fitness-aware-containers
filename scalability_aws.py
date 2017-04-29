import sys
import subprocess
#import boto3
import time
from multiprocessing import Process

cluster_name = "try3"
region = "ap-northeast-1"
account_id = "998181420119"
num_instances = 10
c_instance_id = []
instance_id = []

response = subprocess.run("aws ecs list-container-instances --cluster " + cluster_name + " > cluster.txt",shell = True)
with open('cluster.txt', 'r') as myfile:
    data=myfile.read().replace(" ","")
length = len(data)
initial_inst = (length - 130) / 99 + 1
print(initial_inst)

start_time = time.time()
subprocess.run("ecs-cli scale --capability-iam --size " + str(num_instances),shell=True)
cluster_name = "try3"
region = "ap-northeast-1"
account_id = "998181420119"

c_instance_id = []
instance_id = []
print(length + (num_instances - initial_inst) * 99)
while len(data) < length + (num_instances - initial_inst) * 99:
	response = subprocess.run("aws ecs list-container-instances --cluster " + cluster_name + " > cluster.txt",shell = True)
	with open('cluster.txt', 'r') as myfile:
    		data=myfile.read().replace(" ","")
	print(len(data))

print("--- %s seconds ---" % (time.time() - start_time))
