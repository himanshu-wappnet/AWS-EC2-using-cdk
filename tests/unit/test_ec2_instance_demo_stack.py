import aws_cdk as core
import aws_cdk.assertions as assertions

from ec2_instance_demo.ec2_instance_demo_stack import Ec2InstanceDemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ec2_instance_demo/ec2_instance_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Ec2InstanceDemoStack(app, "ec2-instance-demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
