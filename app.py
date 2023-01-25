#!/usr/bin/env python3
import os
import aws_cdk as core

from ec2_instance_demo.ec2_instance_demo_stack import Ec2InstanceStack


app = core.App()

env = core.Environment(region="<REGION>",account="<AWS_ACCOUNT_ID>") #ENTER REGION AND ACCOUNT ID

Ec2InstanceStack(app, "ec2-instance",env=env)
app.synth()
