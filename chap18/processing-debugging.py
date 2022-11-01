import os
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# 이거 자체가 드라이버 프로세스 인듯
spark = SparkSession.builder.appName("debugging-processing").getOrCreate()

read_file_location = (
    "C:/Users/mobigen/definitive-spark/data/retail-data/all/online-retail-dataset.csv"
)

(
    spark.read.format("csv")
    .option("header", "true")
    .csv(read_file_location)
    .repartition(2)
    .selectExpr("instr(Description, 'GLASS') >= 1 as is_glass")
    .groupBy("is_glass")
    .count()
)

os.system("pause")
