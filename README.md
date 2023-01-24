
# Welcome to EC2 using CDK Python project!

This is a project for EC2 using CDK with Python Language.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates a virtualenv within this project, stored under the `.venv` directory.  To create the virtualenv it assumes that there is a `python3`(or `python` for Windows) executable in your path with access to the `venv` package. If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv manually.

To install or setup the environment for cdk we need to fire below commands:
```
$ python -m ensurepip --upgrade
```
```
$ python -m pip install --upgrade pip
```
```
$ python -m pip install --upgrade virtualenv
```

Install "Node Packages" from official website https://nodejs.org/en/download/ (For windows)

```
$ apt install npm (For Ubuntu/Debian)
```
```
$ npm --version
```
```
$ npm install -g aws_cdk
```
```
$ cdk --version
```

(ALTERNATIVE: Now if we want to Initialize the project so for that we will use below commands) --> WITHOUT CLONING THIS REPOSITORY
```
$ mkdir ec2-instance-demo
```
```
$ cd ec2-instance-demo
```
```
$ cdk init --language python
```

THEN WE NEED TO MADE CHANGES HERE,
```
1) ```REMOVE "core" from import part in ec2_instance_demo_stack.py and instead of it change it to "import aws_cdk as core"
```
```
2) ADD "from constructs import Construct" in ec2_instance_demo_stack.py file. 
```
```
3) change the def __init__ portion to this:

def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
```        
```
4) REPLACE amiName to amiName="ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-20211129"
```
```
5) ADD key_name= 'your key pair name',
```
```
6) ADD this line inside of class  --> key_name=ec2.CfnKeyPair(self,"new-key-cdk",key_name="cdk-test")
```
```
7) in app.py change "from aws_cdk import core" to "import aws_cdk as core".
```
```
8) in app.py change "from ec2_instance.ec2_instance_stack import Ec2InstanceStack" to "ec2_instance_demo.ec2_instance_demo_stack import Ec2InstanceStack" .
```



(FROM HERE WE HAVE TO PERFORM STEPS DIRECTLY IF WE ARE SKIPPING THE ALTERNATAIVE OPTION)
To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add them to your `setup.py` file and rerun the `pip install -r requirements.txt` command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!

Now after making changes deploy the app.

```
$ cdk deploy
```

After that for destroy the application throw this.

```
$ cdk destroy
```
