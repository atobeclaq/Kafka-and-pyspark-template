import threading
import time
from kafka_module import Consumer, Producer
import subprocess
from pyspark_module import transform_data
import ast
from multiprocessing import Process, Queue
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# To Do: Change it based on your requirement, variable section
schema = StructType([
    StructField("id", IntegerType(), nullable=False),
    StructField("name", StringType(), nullable=False),
    StructField("age", IntegerType(), nullable=False)
])

bootstrap_server= "localhost:9092" 
topics= "topic1"
group_id = "my-group"
messagesource="pyspark_module/input.csv"
type="production"


# To Do: Change it based on your requirement
def transformation_fn(input_df):
    # Apply transformation logic
    output_df = input_df.withColumn("age_squared", input_df.age ** 2)
    return output_df

# To Do: Change it based on your requirement
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


is_header = True
def consumerandprocess(bootstrap_server,topics,group_id):
    global is_header
    for message in Consumer(
        bootstrap_server= bootstrap_server, 
        topics= topics,
        group_id = group_id
        ):

        if is_header:
            is_header = False
            continue
        data = process_message(message)
        print("terraform data", data)
        if data is None:
            continue
        # Call the transform_data function with the received data and output file path
        transform_data(data, "output.csv", transformation_fn, schema)

generatemsg = threading.Thread(target=Producer, args=(bootstrap_server,topics,messagesource,type))
receivemsgandprocess = threading.Thread(target=consumerandprocess, args= (bootstrap_server,topics,group_id) )

# starting thread 1
generatemsg.start()
# starting thread 2
receivemsgandprocess.start()

# wait until thread 1 is completely executed
generatemsg.join()
# wait until thread 2 is completely executed
receivemsgandprocess.join()

# both threads completely executed
print("Done!")