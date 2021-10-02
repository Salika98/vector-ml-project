from google.cloud import pubsub_v1

# Credentials
project_id = "vactor-ai-project"
topic_id = "my-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

data = "Hello"
data = data.encode("utf-8")

future = publisher.publish(topic_path, data)
print(future.result())