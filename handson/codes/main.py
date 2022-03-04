#!/usr/bin/env python3

# 発表資料を見て FIXME の部分を修正しましょう

import pulsar
import logging

# log level を設定
# client を作成
logger = logging.getLogger('pulsar')
logger.setLevel('INFO')
client = pulsar.Client('pulsar://pulsar:6650', logger=logger)

# 先程作った tenant と namespace 上の topic に subscribe する consumer を作る
# topic は自動で作られる
topic = 'FIXME'
consumer = client.FIXME(topic, 'my-subscription')

print('sending message')

# producer を作り、message を送信する
producer = client.create_producer(topic)
# byte 列として message を送信する
producer.FIXME('hello!'.encode())

print('receiving message')

# message を受信する
message = consumer.FIXME()
print(f'id: {message.message_id()}, data: {message.value().decode()}')

# acknowledge (受信した事を broker に通知) する
# これをしないと message は broker から削除されない (設定によっては再送される)
consumer.FIXME(message)

# 最後に client, producer, consumer を閉じる
# 閉じないと program 終了後も接続が残る
producer.close()
consumer.close()
client.close()
