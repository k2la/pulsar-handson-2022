from pulsar import Function

import json

class IdRoutingFunction(Function):
  def __init__(self):
    self.output2_topic = "persistent://my-tenant/my-namespace/output2"
    self.output3_topic = "persistent://my-tenant/my-namespace/output3"
  """
  * context.publishを使うと、引数に指定したトピックにメッセージを流すことができる
  """
  def process(self, input, context):
    input_json = json.loads(input)
    name = ("%s %s" % (input_json["firstName"], input_json["lastName"]))
    if(input_json["id"] >= 100):
      context.publish(self.output2_topic, name)
    else:
      context.publish(self.output3_topic, name)
