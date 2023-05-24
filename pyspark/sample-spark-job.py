from pyspark.sql import SparkSession
import pandas as pd
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
# Read input data from a CSV file
input_df = spark.read.csv("spark/input.csv", header=True, inferSchema=True)


# Perform data transformation
output_df = input_df.select("id", "name", "age") \
    .filter(input_df.id > 10) \
    .withColumn("new_column", input_df.id * 2)


# Write the transformed data to a Parquet file
# output_df.write.mode("overwrite").parquet("output.parquet")

# Write the transformed data to a CSV file
output_df.coalesce(1).write.mode("overwrite").csv("output.csv", header=True)
# Convert DataFrame to Pandas DataFrame
pandas_df = output_df.toPandas()

# Save Pandas DataFrame as CSV
pandas_df.to_csv("output2.csv", index=False)
# Log a message
logger.info("Data transformation completed successfully.")

# Stop the SparkSession
spark.stop()
