from kafka import KafkaProducer
import time

# Kafka broker configuration
bootstrap_servers = 'localhost:9092'

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers
)

# Generate and send messages continuously
while True:
    message = f"Message generated at {time.time()}"
    producer.send('topic1', value=message.encode('utf-8'))
    time.sleep(1)  # Wait for 1 second before sending the next message

# Close the producer (this part may not be executed since it's an infinite loop)
producer.close()
