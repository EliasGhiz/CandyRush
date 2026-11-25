# join_data.py
# Joins candy products with happiness scores by country.
# Reads LOCAL files (run ./fetch_data.sh first). It does not pull from GCS.
from pyspark.sql import SparkSession

CANDY_PATH = "data/candy_by_country"
WHR_PATH = "data/happiness_by_country"
OUT_PATH = "output/joined"

spark = SparkSession.builder.getOrCreate()

# No header rows. Verify the order of nova_group and additives_n.
# code is read as a string so leading zeros are kept.
candy = spark.read.csv(
    CANDY_PATH,
    schema="country STRING, code STRING, product_name STRING, "
           "sugars_100g DOUBLE, nova_group INT, additives_n INT")

whr = (spark.read.option("ignoreLeadingWhiteSpace", True).csv(WHR_PATH, inferSchema=True)
       .toDF("country", "happiness_score"))

joined = candy.join(whr, on="country", how="inner")

print("candy rows:", candy.count(), "| whr rows:", whr.count(), "| joined rows:", joined.count())
print("Candy countries with no happiness score:")
candy.select("country").distinct().join(whr, "country", "left_anti").show(100, truncate=False)

joined.show(5, truncate=False)
joined.write.mode("overwrite").parquet(OUT_PATH)
# use the line below to coalesce into one table file:
# joined.coalesce(1).write.mode("overwrite").option("header", True).csv("output/joined_csv")