#!/usr/bin/env python3
import os
import aws_cdk as core

from ec2_instance_demo.ec2_instance_demo_stack import Ec2InstanceStack


app = core.App()

env = core.Environment(region="ap-south-1",account="810833458562")

Ec2InstanceStack(app, "ec2-instance",env=env)
app.synth()
