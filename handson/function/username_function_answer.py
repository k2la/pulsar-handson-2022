from pulsar import Function

import json

class UsernameFunction(Function):
  def __init__(self):
    pass

  def process(self, input, context):
    input_json = json.loads(input)
    return ("%s %s" % (input_json["firstName"], input_json["lastName"]))
