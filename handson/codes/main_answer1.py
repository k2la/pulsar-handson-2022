#!/usr/bin/env python3

import pulsar
import logging
from employee import Employee, employeeSchema

logger = logging.getLogger('pulsar')
logger.setLevel('INFO')
client = pulsar.Client('pulsar://pulsar:6650', logger=logger)

topic = 'persistent://my-tenant/my-namespace/schema-topic'
consumer = client.subscribe(
    topic=topic, subscription_name='my-subscription', schema=employeeSchema)

print('sending message')

producer = client.create_producer(topic=topic, schema=employeeSchema)
producer.send(Employee(id_=100, firstName='Taro',
              lastName='Yamada', title='Manager'))

print('receiving message')

message = consumer.receive()
print(message.value())
print(f'firstName: {message.value().firstName}')
consumer.acknowledge(message)

producer.close()
consumer.close()
client.close()
