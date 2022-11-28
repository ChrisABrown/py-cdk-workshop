#!/usr/bin/env python3

import aws_cdk as cdk

from py_cdk_workshop.py_cdk_workshop_stack import PyCdkWorkshopStack


app = cdk.App()
PyCdkWorkshopStack(app, "py-cdk-workshop")

app.synth()
