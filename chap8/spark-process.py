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

df1 = spark.range(2, 10000000, 2)
df2 = spark.range(2, 10000000, 4)

step1 = df1.repartition(5)
step1_2 = df2.repartition(6)

step2 = step1.selectExpr("id * 5 as id")
step3 = step2.join(step1_2, ["id"])
step4 = step3.selectExpr("sum(id)")

step4.collect()  # 결과는 2,500,000,000,000


# collect 액션으로 하나의 스파크 잡이 완료되는 것을 확인
# 보통 액션 하나당 하나의 스파크 잡이 생성되며 액션은 항상 같은 결과를 반환
# 스파크 잡은 일련의 스테이지로 나뉘며 스테이지 수는 셔플 작업이 얼마나 많이 발생하는지에 따라 달라집니다.

# 위의 예제의 잡은 다음과 같이 나뉩니다.

# (range 명령을 수행하는 단계, range 명령을 사용하면 기본적으로 8개의 파티션을 생성)
# 스테이지 1: 태스크 8개
# 스테이지 2: 태스크 8개

# (repartition 단계, 데이터 셔플링으로 파티션 수를 변경)
# 스테이지 3: 태스크 5개
# 스테이지 4: 태스크 6개

# (spark.sql.shuffle.partitions 속성의 기본값은 200임으로 태스트 200개 생성)
# 스테이지 5: 태스크 200개

# (드라이버로 결과를 전송하기 전에 파티션마다 개별적으로 수행된 결과를 단일 파티션으로 모으는 작업)
# 스테이지 6: 태스크 1개

# 스파크의 스테이지는 다수의 머신에서 동일한 연산을 수행하는 태스크의 그룹을 나타냄
# 셔플 작업이 일어난 다음에는 반드시 새로운 스테이지를 시작
# 스파크의 스테이지는 태스크로 구성 각 태스크는 단일 익스큐터에서 실행할 데이터의 블록과 다수의 트랜스포메이션 조합으로 볼 수 있음
# 만약 1000개의 작은 파티션으로 구성되어 있다면 1000개의 태스크를 만들어 병렬로 실행할 수 있음
# 즉 태스크는 데이터 단위(파티션)에 적용되는 연산 단위를 의미
# 파티션 수를 늘리면 더 높은 병렬성을 얻을 수 있음 최적화를 위한 가장 간단한 방법
