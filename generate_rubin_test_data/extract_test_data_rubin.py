from pyspark.sql import SparkSession
from fink_broker.common.spark_utils import list_hdfs_files

major = 10
minor = 0

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("WARN")

paths = list_hdfs_files("online/raw/20260101")
df = spark.read.format("parquet").load(paths)

# Parquet for unit tests
df.limit(100).write.parquet("rubin_test_data_{}_{}.parquet".format(major, minor))

# Avro for real-time tests
df.limit(100).write.format("avro").save("rubin_test_data_{}_{}.avro".format(major, minor))
