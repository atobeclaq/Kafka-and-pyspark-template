from pyspark.sql import SparkSession
import pandas as pd

def transform_data(input_data, output_file):
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

    # Convert the input data (Kafka consumer message) to DataFrame
    input_df = spark.createDataFrame(input_data, ["id", "name", "age"])

    # Perform data transformation
    output_df = input_df.select("id", "name", "age") \
        .filter(input_df.id > 10) \
        .withColumn("new_column", input_df.id * 2)

    # Write the transformed data to a CSV file
    output_df.coalesce(1).write.mode("overwrite").csv(output_file, header=True)
    # Convert DataFrame to Pandas DataFrame
    pandas_df = output_df.toPandas()

    # Save Pandas DataFrame as CSV
    pandas_df.to_csv(output_file, index=False)
    # Log a message
    logger.info("Data transformation completed successfully.")

    # Stop the SparkSession
    spark.stop()
