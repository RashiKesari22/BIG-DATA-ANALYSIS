"""
spark_analysis.py

Read a massive CSV, perform a simple yet representative analysis,
and show how the work is distributed across the Spark cluster.

Usage (local mode):
    pyspark spark_analysis.py

Usage (cluster):
    spark-submit --master yarn --num-executors 8 --executor-memory 16g spark_analysis.py
"""

import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, countDistinct, count, avg, sum as _sum

# ----------------------------------------------------------------------
# 1. Create a Spark session (adjust config as needed)
# ----------------------------------------------------------------------
def create_session(app_name: str = "LargeCSVAnalysis") -> SparkSession:
    return (
        SparkSession.builder.appName(app_name)
        .config("spark.sql.execution.arrow.enabled", "true")
        .getOrCreate()
    )

# ----------------------------------------------------------------------
# 2. Load the CSV (replace with your actual path)
# ----------------------------------------------------------------------
def load_csv(spark: SparkSession, path: str):
    # inferSchema is cheap for a one‑off run; for production you would provide a schema.
    return spark.read.csv(path, header=True, inferSchema=True, sep=",")

# ----------------------------------------------------------------------
# 3. Aggregation – count events per type, distinct users, average latency
# ----------------------------------------------------------------------

def aggregate_pizza_sales(df):
    # pick the human‑readable pizza name (last column in the sample)
    return (
        df.groupBy(col("pizza_name"))
          .agg(_sum(col("quantity")).alias("total_quantity"))
          .orderBy(col("total_quantity").desc())
    )

# ----------------------------------------------------------------------
# 5. Write results (Parquet is fast and compact)
# ----------------------------------------------------------------------
def write_results(result_df, out_path: str):
    result_df.write.mode("overwrite").parquet(out_path)

# ----------------------------------------------------------------------
# Main driver
# ----------------------------------------------------------------------
def main():
    if len(sys.argv) != 3:
        print("Usage: spark-submit <script> <input_csv> <output_dir>")
        sys.exit(1)

    input_path, output_path = sys.argv[1], sys.argv[2]

    spark = create_session()
    raw_df = load_csv(spark, input_path)
    agg_df = aggregate_pizza_sales(raw_df)
    write_results(agg_df, output_path)

    # Show a quick preview (will trigger the job)
    agg_df.show(32)

    spark.stop()

if __name__ == "__main__":
    main()
