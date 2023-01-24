import aws_cdk as core
from aws_cdk import (
    
    aws_ec2 as ec2,

)
from constructs import Construct


vpcID="vpc-0881092e182fe1658"
instanceName="webserver-2"
instanceType="t2.micro"
amiName="ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-20211129"


class Ec2InstanceStack(core.Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        key_name = ec2.CfnKeyPair(self,"new-key-cdk",key_name="cdk-test")

        # The code that defines your stack goes here

        # lookup existing VPC
        vpc = ec2.Vpc.from_lookup(
            self,
            "vpc",
            vpc_id=vpcID,
        )
        
        # create a new security group
        sec_group = ec2.SecurityGroup(
            self,
            "sec-group-allow-ssh",
            vpc=vpc,
            allow_all_outbound=True,
        )

        # add a new ingress rule to allow port 22 to internal hosts
        sec_group.add_ingress_rule(
            peer=ec2.Peer.ipv4('10.0.0.0/16'),
            description="Allow SSH connection", 
            connection=ec2.Port.tcp(22)
        )

        # define a new ec2 instance
        ec2_instance = ec2.Instance(
            self,
            "ec2-instance",
            instance_name=instanceName,
            key_name= key_name,
            instance_type=ec2.InstanceType(instanceType),
            machine_image=ec2.MachineImage().lookup(name=amiName),
            vpc=vpc,
            security_group=sec_group,
        )
