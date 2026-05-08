from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName("ETL Job").getOrCreate()

# Read data from S3 (replace with your path later)
df = spark.read.csv("s3://your-bucket-name/raw_data.csv", header=True, inferSchema=True)

# Data transformation
df_clean = df.dropna()
df_clean = df_clean.withColumnRenamed("customer_name", "customer")

# Write processed data back to S3
df_clean.write.mode("overwrite").parquet("s3://your-bucket-name/processed_data/")

print("ETL Job Completed")
