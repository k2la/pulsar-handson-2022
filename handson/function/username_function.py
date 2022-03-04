# FIXME を別のものに置き換えてください

from pulsar import Function

import json

class UsernameFunction(Function):
  def __init__(self):
    pass

  def process(self, input, context):
    input_json = json.loads(input)
    return ("%s %s" % (input_json["FIXME"], input_json["FIXME"]))
