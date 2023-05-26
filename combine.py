from kafka_module import Consumer, Producer
import subprocess
from pyspark_module import transform_data
import ast
from multiprocessing import Process, Queue
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
schema = StructType([
    StructField("id", IntegerType(), nullable=False),
    StructField("name", StringType(), nullable=False),
    StructField("age", IntegerType(), nullable=False)
])
def transformation_fn(input_df):
    # Apply transformation logic
    output_df = input_df.withColumn("age_squared", input_df.age ** 2)
    return output_df
def process_message(message):
    # Convert the message string to a list
    data = ast.literal_eval(message)
    
    if data[0] == 'id':
        # Skip the header row
        return None
    
    # Extract the values from the list
    id, name, age = data
    
    # Convert id and age to integers
    return {"id": int(id), "name": name, "age": int(age)}


# Specify the path to the bash script
# bash_script_path = 'kafka_module/start-kafka-zookeeper.sh'

# # Run the bash script
# subprocess.run(['bash', bash_script_path], check=True)

Producer(
    bootstrap_server='localhost:9092',
    topic = "topic1",
    messagesource= "pyspark_module/input.csv",
    type = "production" # Can just pass 'test' if just want test if the system will run as expected
    )


is_header = True
for message in Consumer(bootstrap_server= "localhost:9092", topics= "topic1",group_id = "my-group"):
    # print(f"Received message: {message}")
    if is_header:
        is_header = False
        continue
    data = process_message(message)
    print("terraform data", data)
    if data is None:
        continue
    # Call the transform_data function with the received data and output file path
    transform_data(data, "output.csv",transformation_fn, schema)

# import asyncio
# from kafka_module import Consumer, Producer
# from pyspark_module import transform_data
# import ast
# from kafka import KafkaProducer
# import time
# import csv


# import asyncio
# from concurrent.futures import ProcessPoolExecutor


# def process_message(message):
#     # Convert the message string to a list
#     data = ast.literal_eval(message)

#     if data[0] == 'id':
#         # Skip the header row
#         return None

#     # Extract the values from the list
#     id, name, age = data

#     # Convert id and age to integers
#     return {"id": int(id), "name": name, "age": int(age)}


# async def produce_messages():
#     Producer(
#     bootstrap_server='localhost:9092',
#     topic = "topic1",
#     messagesource= "pyspark_module/input.csv",
#     type = "production" # Can just pass 'test' if just want test if the system will run as expected
#     )


# async def consume_and_transform_data():

#     for message in Consumer(bootstrap_server= "localhost:9092", topics= "topic1",group_id = "my-group"):
#         data = process_message(message.value.decode('utf-8'))
#         if data is not None:
#             transform_data(data, "output.csv",transformation_fn, schema)




# loop = asyncio.get_event_loop()
# a1 = loop.create_task(get())
# loop.run_until_complete(a1)
