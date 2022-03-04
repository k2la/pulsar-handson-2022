import pulsar
import logging

class Employee(pulsar.schema.Record):
  id = pulsar.schema.Integer()
  firstName = pulsar.schema.String()
  lastName = pulsar.schema.String()
  title = pulsar.schema.String()

logger = logging.getLogger('pulsar')
logger.setLevel('INFO')
client = pulsar.Client('pulsar://pulsar:6650', logger=logger)

topic = "persistent://my-tenant/my-namespace/input"
schema = pulsar.schema.JsonSchema(Employee)

producer = client.create_producer(topic=topic, schema=schema)
employee = Employee(id=100, firstName="Taro", 
                    lastName="Yamada", title="Manager")
producer.send(employee)

producer.close()
client.close()
