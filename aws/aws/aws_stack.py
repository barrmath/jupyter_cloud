from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)

from aws_cdk import aws_sagemaker as sagemaker

from constructs import Construct


class Jupyter_lab(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id,**kwargs)
        # plus qu'a initialiser le Sagemaker ici Doc :https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sagemaker-readme.html

