#!/usr/bin/env python3

from pulsar import schema


# 送受信したい class を定義
class Employee(schema.Record):
    id_ = schema.Integer()
    firstName = schema.String()
    lastName = schema.String()
    title = schema.String()


# 送受信したい class を定義
employeeSchema = schema.JsonSchema(Employee)
