#!/usr/bin/env python3

import aws_cdk as cdk

from py_cdk_workshop.pipeline_stack import WorkshopPipelineStack


app = cdk.App()
WorkshopPipelineStack(app, "pipeline-stack")

app.synth()
