from operator import contains
import os
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# sparkSession 생성
# sparkSession으로 SparkContext에 접근 가능 (SparkContext + SQLContext)
# 모든 스파크 코드는 RDD 명령으로 컴파일
# 스파크 코드는 트랜스포메이션과 액션으로 구성
spark = SparkSession.builder.appName("join-processing").getOrCreate()

## load dataset
person = spark.createDataFrame(
    [
        (0, "Bill Chambers", 0, [100]),
        (1, "Matei Zaharia", 1, [500, 250, 100]),
        (2, "Michael Armbrust", 1, [250, 100]),
    ]
).toDF("id", "name", "graduate_program", "spark_status")

graduateProgram = spark.createDataFrame(
    [
        (0, "Masters", "School of Information", "UC Berkeley"),
        (2, "Masters", "EECS", "UCBerkeley"),
        (1, "Ph.D.", "EECS", "UCBerkeley"),
    ]
).toDF("id", "degree", "department", "school")

sparkStatus = spark.createDataFrame(
    [(500, "vicePresident"), (250, "PMCMember"), (100, "Contributor")]
).toDF("id", "status")

person.createOrReplaceGlobalTempView("person")
graduateProgram.createOrReplaceGlobalTempView("person")
sparkStatus.createOrReplaceGlobalTempView("person")

# joinExpression = person["graduate_program"] == graduateProgram["id"]
# joinExpression = person.graduate_program == graduateProgram.id
# person.join(graduateProgram, joinExpression).show()
# person.join(graduateProgram, joinExpression, "inner").show()

person.join(sparkStatus, array_contains(person.spark_status, sparkStatus.id)).show()
