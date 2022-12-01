
from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

from cdk_dynamo_table_view import TableViewer
from .hitcounter import HitCounter


class PyCdkWorkshopStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        hello = _lambda.Function(
            self,
            "HelloHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("lambda"),
            handler="hello.handler",
        )

        hello_with_counter = HitCounter(
            self,
            "HelloHitHandler",
            downstream=hello,
        )

        apigw.LambdaRestApi(
            self,
            "Endpoint",
            handler=hello_with_counter.handler,
        )

        TableViewer(
            self, 'ViewHitCounter',
            title="Hits Table",
            table=hello_with_counter.table,
        )
