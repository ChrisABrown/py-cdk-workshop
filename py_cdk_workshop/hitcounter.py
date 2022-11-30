from msilib.schema import Environment
from typing_extensions import runtime
from constructs import Construct
from aws_cdk import (
    aws_lambda as _lambda,
    aws_dynamodb as ddb,
)


class HitCounter(Construct):
    @property
    def handler(self):
        return self._handler

    def __init__(
        self, scope: Construct, id: str, downstream: _lambda.IFunction, **kwargs
    ):
        super().__init__(scope, id, **kwargs)

        table = ddb.Table(
            self,
            "Hits",
            partition_key={"name": "path", "type": ddb.AttributeType.STRING},
        )

        self._handler = _lambda.IFunction(
            self,
            "HitCountHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("lambda"),
            handler="hitcount.handler",
            Environment={
                "DOWNSTREAM_FUNCTION_NAME": downstream.function_name,
                "HITS_TABLE_NAME": table.table_name,
            },
        )