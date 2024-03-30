#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws.aws_stack import Jupyter_lab

print ('Creating environment')
cdk_env = cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))

app = cdk.App()

Jupyter_lab(app,"JupyterLab",env=cdk_env)

app.synth()
