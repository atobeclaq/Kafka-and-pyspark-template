from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
import os
import pandas as pd

def transform_data(input_data, output_file, transformation_fn, schema):
    # Create a SparkSession
    spark = SparkSession.builder \
        .appName("YourAppName") \
        .config("spark.driver.extraJavaOptions", "-Dspark.driver.extraJavaOptions=-Dlog4j.configuration=file:/spark/log4j.properties") \
        .config("spark.driver.extraJavaOptions", "-Dspark.driver.extraJavaOptions=-Dspark.default.properties.file=/spark/spark-defaults.conf") \
        .getOrCreate()

    # Set up logging
    log4j = spark._jvm.org.apache.log4j
    logger = log4j.LogManager.getLogger(__name__)
    # Set the log level
    spark.sparkContext.setLogLevel("INFO")

    # Convert the input_data dictionary to a list of rows
    rows = [(input_data[field.name]) for field in schema.fields]

    logger.info(" input data is "  + str(rows))
    # Create the DataFrame
    input_df = spark.createDataFrame([rows], schema)

    output_df = transformation_fn(input_df)
    # Convert DataFrame to Pandas DataFrame
    pandas_df = output_df.toPandas()

    # Save Pandas DataFrame as CSV
    # Check if the output file already exists
    if os.path.isfile(output_file):
        # Append data to the existing file
        pandas_df.to_csv(output_file, mode='a', header=False, index=False)
    else:
        # Save Pandas DataFrame as CSV
        pandas_df.to_csv(output_file, index=False)
    # Log a message
    logger.info("Data transformation completed successfully.")

    # Stop the SparkSession
    spark.stop()
