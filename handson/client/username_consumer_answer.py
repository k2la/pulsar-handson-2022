import pulsar
import logging

logger = logging.getLogger('pulsar')
logger.setLevel('INFO')
client = pulsar.Client('pulsar://pulsar:6650', logger=logger)

topic = "persistent://my-tenant/my-namespace/output"
consumer = client.subscribe(
    topic=topic, subscription_name="my-subscription")

message = consumer.receive()
print(message.data().decode())
consumer.acknowledge(message)

consumer.close()
client.close()
