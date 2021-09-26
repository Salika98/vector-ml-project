from kafka  import KafkaProducer
from time import sleep
import numpy as np
from json import dumps
from model_service import make_predictions


def generate_stream(xs, **kwargs):
	"""
	Generates a stream of requests to a client
	"""
	producer = KafkaProducer(bootstrap_servers=[kwargs['client']],
							value_serializer=lambda x: 
							dumps(x).encode('utf-8'))

	# Make predictions on the given dataset
	predictions = make_predictions(xs)

	# Send each precition to the client with 5sec pause in between
	for prediction in predictions:
		producer.send(kwargs['topic'], value=int(prediction))
		sleep(5)

	producer.close()
