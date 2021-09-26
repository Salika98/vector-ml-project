from kafka import KafkaConsumer
from json import loads
import numpy as np
import time


def get_data_from_kafka(**kwargs):
    """
    Client that receives a stream of requests
    """

    consumer = KafkaConsumer(
        kwargs['topic'],
        bootstrap_servers=[kwargs['client']],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))


    for message in consumer:
        msg = message.value
        print(msg)