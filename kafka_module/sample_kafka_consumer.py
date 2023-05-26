from kafka import KafkaConsumer

message_count = 0  # Variable to track the message count

# def condition_to_stop():
#     return message_count >= 100

def Consumer( 
    bootstrap_server: str = "localhost:9092",
    topics:str = "topic1",
    group_id:str = "my-group"
    ):

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
        print(message.value.decode('utf-8'), "received ++++++++++++++++++++++")
        yield message.value.decode('utf-8')
        # message_count += 1

        # # Check if the condition to stop is met
        # if condition_to_stop():
        #     break

    # Close the consumer (this part may not be executed since it's an infinite loop)
    consumer.close()
