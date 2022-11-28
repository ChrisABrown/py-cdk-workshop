from cgitb import handler
from pyclbr import Function
from constructs import Construct
from aws_cdk import (
    Stack,
   aws_lambda as _lambda,
)


class PyCdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime = _lambda.Runtime.PYTHON_3_9,
            code = _lambda.Code.from_asset('lambda'),
            handler = 'hello.handler',
            )