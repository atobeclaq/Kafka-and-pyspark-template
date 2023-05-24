from kafka import KafkaConsumer

# Kafka broker configuration
bootstrap_servers = 'localhost:9092'

# Kafka topics to subscribe to
topics = ['topic1']

# Create Kafka consumer
consumer = KafkaConsumer(
    *topics,
    bootstrap_servers=bootstrap_servers,
    group_id='my-group'
)

# Process incoming messages continuously
for message in consumer:
    # Process the message
    print(f"Received message: {message.value.decode('utf-8')}")

# Close the consumer (this part may not be executed since it's an infinite loop)
consumer.close()
