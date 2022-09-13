from operator import contains
import os
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("2015-summary-data-processing").getOrCreate()

read_file_location = (
    "C:/Users/mobigen/definitive-spark/data/flight-data/json/2015-summary.json"
)

# 스파크는 자체 데이터 타입 정보를 사용하므로 프로그래밍 언어의 데이터 타입을 스파크의 데이터 타입으로 설정 불가
myManualSchema = StructType(
    [
        StructField("DEST_COUNTRY_NAME", StringType(), True),
        StructField("ORIGIN_COUNTRY_NAME", StringType(), True),
        StructField("count", LongType(), False, metadata={"hello": "world"}),
    ]
)

df = (
    spark.read.format("json")
    .option("header", "true")
    .option("schema", myManualSchema)
    .load(read_file_location)
)

# df2 = df.select(lower(col("ORIGIN_COUNTRY_NAME")))

# df2.explain()

# df.select(regexp_extract(col("ORIGIN_COUNTRY_NAME"), "(United|test)", 0)).show()
df.select(regexp_extract(col("ORIGIN_COUNTRY_NAME"), "(United|test)", 1)).show()
df.select(coalesce(col("ORIGIN_COUNTRY_NAME"), col("DEST_COUNTRY_NAME"))).show()
