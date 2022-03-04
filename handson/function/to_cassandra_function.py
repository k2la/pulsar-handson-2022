from pulsar import Function

import json

class UsernameFunction(Function):
  def __init__(self):
    pass

  def process(self, input, context):
    input_json = json.loads(input)
    name = ("%s %s" % (input_json["firstName"], input_json["lastName"]))
    message_conf = {}
    message_conf["partition_key"] = str(input_json["id"])
    output_topic = "persistent://my-tenant/my-namespace/output"
    context.publish(output_topic, name, message_conf=message_conf)
