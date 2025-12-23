# BIG-DATA-ANALYSIS
COMPANY : CODTECH IT SOLUTIONS

NAME : RASHI KESARI

INTERN ID:CT04DR3010

DOMAIN : DATA ANALYTICS

DURATION : 4 WEEKS

MENTOR : NEELA SANTHOSH KUMAR

**DESCRIPTION OF TASK 

Big Data Analysis is about taking a huge pile of raw information and making it useful for real people. We use a powerful engine like PySpark or Dask that can process huge datasets in parallel on many computers. This lets us handle data that normal software cannot manage. The end goal is to give analysts, managers, or business owners clear answers to their questions. The analysis turns raw numbers into useful insights that drive their daily decisions and improve their business. We set up the tool to split the big data into smaller chunks, distribute them across machines, and run operations like filtering, aggregation, and transformation quickly. We also handle fault‑tolerance so the job does not fail if one machine breaks. In practice, businesses use this analysis to spot trends, predict sales, manage inventory, or understand customer behaviour. The tool helps them explore data faster than traditional methods and make smarter strategies. After crunching the data, we create simple charts, dashboards, or summary reports (using Power BI & Tableau). These visuals let anyone see patterns and act without digging into raw numbers.

**PREREQUISITE 

To get the script running we will need:

1.Java 17 (Spark 4.0 requires it) – install with `brew install openjdk@17` and set `JAVA_HOME=/opt/homebrew/opt/openjdk@17`.

2. Apache Spark 4.0– download from the official site, unpack it, and add `$SPARK_HOME/bin` to your `PATH`.

3. Python 3.9+ with `pyspark` package – `pip install pyspark`.

4.The CSV file (e.g., `pizza_sales.csv`) that matches the column names used in the script.

5.Write permission to the output directory you pass as the second argument.

Once those are in place you can launch the job with:

```
bash
spark-submit spark_pizza.py pizza_sales.csv output
```

or locally with `pyspark`. If any of the steps fail, double‑check that `JAVA_HOME` points to Java 17 and that `SPARK_HOME` is set correctly.


* Set `SPARK_HOME` to the Spark installation directory and make sure its `bin` folder is in your `PATH`:
 
bash

export SPARK_HOME=/opt/homebrew/Cellar/apache-spark/4.0.1_1/libexec

export PATH=$SPARK_HOME/bin:$PATH

*Point Spark (and everything else) at that JDK

bash

export JAVA_HOME=/opt/homebrew/opt/openjdk@17

export PATH=$JAVA_HOME/bin:$PATH

**OUTPUT

pizza_name		total_quantity

The Classic Deluxe	12265

The Barbecue Chicken	12160

The Hawaiian Pizza	12110

The Pepperoni Pizza	12090

The Thai Chicken	11855

The California Chicken	11850

The Sicilian Pizza	9690

The Spicy Italian pizza	9620

The Southwest Chicken	9585

The Big Meat Pizza	9570

The Four Cheese Pizza	9510

The Italian Supreme pizza	9420

The Vegetables pizza	7630

The Mexicana Pizza	7420

The Napolitana Pizza	7320

The Prosciutto pizza	7285

The Pepper Salami pizza 	7230

The Spinach pizza	7230

The Italian Capoc pizza	7190

The Greek Pizza	7100

The Five Cheese Pizza	7045

The Pepperoni pizza	6795

The Green Garden pizza	4985

The Chicken Alfredo pizza	4935

The Italian Vegetable pizza	4905

The Chicken Pesto pizza	4865

The Spinach Pesto pizza	4850

The Soppressata Pizza	4805

The Spinach Supreme pizza	4750

The Calabrese Pizza	4685

The Mediterranean pizza	4670

The Brie Carre Pizza	2450

The script is written in a way that lets Spark handle the heavy lifting, so it can scale from a tiny CSV on your laptop to a multi‑terabyte file on a cluster.

**INSIGHTS DERIVED FROM BIG DATA PROCESSING.

1. Distributed data source– `spark.read.csv` reads the file in parallel across all executors. Whether the file lives locally, on HDFS, S3, or any other distributed storage, Spark splits it into partitions and processes them concurrently.

2. Simple, stateless transformations– The only operation is a `groupBy` + `sum`. Spark can shuffle the data once and compute the aggregation on many nodes, then combine the partial results. No extra loops or driver‑side processing that would bottleneck the job.

3. Config‑driven parallelism – By tweaking `spark.sql.shuffle.partitions` (or the number of executors/memory) you control how much work each node does. The code itself does not need to change.

4. Parquet output – Writing the tiny result set to Parquet is cheap, but if the downstream job later reads the full dataset, Parquet’s columnar, compressed format scales well.







