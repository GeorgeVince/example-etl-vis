import os

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import *
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    FloatType,
    TimestampType,
)

from dotenv import load_dotenv
load_dotenv()

MONGO_INPUT_URI = os.getenv("MONGO_INPUT_URI")
MONGO_OUTPUT_URI = os.getenv("MONGO_OUTPUT_URI")
MONGO_SPARK_PACKAGE = os.getenv("MONGO_SPARK_PACKAGE")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")
KAFKA_SPARK_PACKAGE = os.getenv("KAFKA_SPARK_PACKAGE")
KAFKA_BOOTSTRAP_SERVER = os.getenv("KAFKA_BOOTSTRAP_SERVER")
KAFKA_TOPIC_NAME = os.getenv("KAFKA_TOPIC_NAME")

purchase_schema = StructType(
    [
        StructField("purchase_id", StringType()),
        StructField("stock_code", IntegerType()),
        StructField("item_description", StringType()),
        StructField("quantity", IntegerType()),
        StructField("customer_id", StringType()),
        StructField("cost", FloatType()),
        StructField("purchase_date", TimestampType()),
    ]
)


def save(message: DataFrame, id) -> None:

    message.show(truncate=False)

    # Convert to JSON and explode out
    to_write = message.withColumn(
        "value", from_json("value", schema=purchase_schema)
    ).select(col("value.*"))

    to_write.write.format("mongo").mode("append").option("database", MONGO_DB).option(
        "collection", MONGO_COLLECTION
    ).save()

    to_write.show()


def main() -> None:
    spark = (
        SparkSession.builder.appName("example-sales-pipeline")
        .config("spark.mongodb.input.uri", MONGO_INPUT_URI)
        .config("spark.mongodb.output.uri", MONGO_OUTPUT_URI)
        .config(
            "spark.jars.packages",
            f"{MONGO_SPARK_PACKAGE},{KAFKA_SPARK_PACKAGE}",
        )
        .getOrCreate()
    )

    df = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVER)
        .option("subscribe", KAFKA_TOPIC_NAME)
        .load()
    )

    df.selectExpr(
        "CAST(key AS STRING)", "CAST(value AS STRING)"
    ).writeStream.foreachBatch(save).start().awaitTermination()


if __name__ == "__main__":
    main()
