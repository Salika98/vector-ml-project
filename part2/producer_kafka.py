from kafka  import KafkaProducer
import numpy as np
from json import dumps

def generate_stream(msg, **kwargs):
	"""
	Generates a stream of requests to a client
	"""
	producer = KafkaProducer(bootstrap_servers=[kwargs['client']],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
						 
	
	producer.send(kwargs['topic'], value=msg)
	
	producer.close()