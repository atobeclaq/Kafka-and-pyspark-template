from kafka import KafkaConsumer

def Consumer( 
    bootstrap_server: str = "localhost:9092",
    topics:str = "topic1",
    group_id:str = "my-group"
    ):
    # Kafka broker configuration
    # bootstrap_servers = 'localhost:9092'

    # Kafka topics to subscribe to
    topics = [topics]

    # Create Kafka consumer
    consumer = KafkaConsumer(
        *topics,
        bootstrap_servers=bootstrap_server,
        group_id=group_id
    )

    # Process incoming messages continuously
    for message in consumer:
        # Process the message
        yield message.value.decode('utf-8')

    # Close the consumer (this part may not be executed since it's an infinite loop)
    consumer.close()
