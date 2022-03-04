# FIXME を別のものに置き換えてください

import pulsar
import logging

logger = logging.getLogger('pulsar')
logger.setLevel('INFO')
client = pulsar.Client('pulsar://pulsar:6650', logger=logger)

topic = "FIXME"
consumer = client.subscribe(
    topic=topic, subscription_name="my-subscription")

message = consumer.receive()
print(message.value().decode())
consumer.acknowledge(message)

consumer.close()
client.close()
