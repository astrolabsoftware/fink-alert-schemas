#!/bin/bash

FINK_PACKAGES=\
org.apache.spark:spark-streaming-kafka-0-10-assembly_2.12:3.4.1,\
org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1,\
org.apache.spark:spark-avro_2.12:3.4.1,\
org.apache.hbase:hbase-shaded-mapreduce:2.2.7

MESOS=
PRINCIPAL=
SECRET=
ROLE=

spark-submit \
    --master $MESOS \
    --conf spark.mesos.principal=$PRINCIPAL \
    --conf spark.mesos.secret=$SECRET \
    --conf spark.mesos.role=$ROLE \
    --conf spark.executorEnv.HOME='/localhome/fink'\
    --conf spark.sql.parquet.columnarReaderBatchSize=512\
    --conf spark.sql.execution.arrow.pyspark.enabled=true\
    --conf spark.sql.execution.arrow.maxRecordsPerBatch=1000000\
    --conf spark.kryoserializer.buffer.max=512m\
    --packages $FINK_PACKAGES \
    --driver-memory 2G --executor-memory 2G --conf spark.cores.max=24 --conf spark.executor.cores=1 extract_test_data_rubin.py
