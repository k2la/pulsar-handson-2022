#!/usr/bin/env python3

import pulsar
import logging

logger = logging.getLogger('pulsar')
logger.setLevel('INFO')
client = pulsar.Client('pulsar://pulsar:6650', logger=logger)

topic = 'persistent://my-tenant/my-namespace/my-topic'
consumer = client.subscribe(topic, 'my-subscription')

print('sending message')

producer = client.create_producer(topic)
producer.send('hello!'.encode())

print('receiving message')

message = consumer.receive()
print(f'id: {message.message_id()}, data: {message.value().decode()}')
consumer.acknowledge(message)

producer.close()
consumer.close()
client.close()
