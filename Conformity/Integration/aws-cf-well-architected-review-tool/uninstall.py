#!/usr/local/bin/python3

import argparse
import boto3
import botocore.exceptions
import json

parser = argparse.ArgumentParser(
    description='''
    Removes the Conformity-WellArchitected-Integration stack.
        
    Assumes your AWS CLI is configured and that you have sufficient permissions
    to run 'aws cloudformation create-stack' with CAPABILITY_NAMED_IAM.'
    ''')
parser.add_argument( "--stackName", type=str, default="Conformity-WellArchitectedReview-Sync", help="Name used to create the Conformity->Well-Architected Review sync stack")
args = parser.parse_args()
cfnClient = boto3.client("cloudformation")

try:
    stacks = cfnClient.describe_stacks(StackName=f"{args.stackName}")
    cfnClient.delete_stack(StackName=f"{args.stackName}")
    print(f'Stack {args.stackName} deleted')
except botocore.exceptions.ClientError as clientError:
    print(json.dumps(clientError.response, indent=4))

