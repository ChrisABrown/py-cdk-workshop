from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    assertions
)

from py_cdk_workshop.hitcounter import HitCounter


def test_dynamodb_table_created():
    stack = Stack()
    HitCounter(stack, "HitCounter",
               downstream=_lambda.Function(stack, "TestFunction",
                                           runtime=_lambda.Runtime.PYTHON_3_9,
                                           code=_lambda.Code.from_asset("lambda"),
                                           handler="hello.handler"
                                           )
               )
    template = assertions.Template.from_stack(stack)
    template.resource_count_is("AWS::DynamoDB::Table", 1)


def test_lambda_has_env_vars():
    stack = Stack()
    HitCounter(stack, "HitCounter",
               downstream=_lambda.Function(stack, "TestFunction",
                                           runtime=_lambda.Runtime.PYTHON_3_9,
                                           code=_lambda.Code.from_asset("lambda"),
                                           handler="hello.handler"
                                           )
               )
    template = assertions.Template.from_stack(stack)
    envCapture = assertions.Capture()

    template.has_resource_properties("AWS::Lambda::Function",
                                     {"Handler": "hitcount.handler",
                                      "Environment": envCapture,
                                      })
    assert envCapture.as_object() == {
        "Variables": {
            "DOWNSTREAM_FUNCTION_NAME": {"Ref": "TestFunctionXXX"},
            "HITS_TABLE_NAME": {"Ref": "HitConterHitsXXX"},
        },
    }
