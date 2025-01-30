from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import col, avg

# Initialize Spark Session
spark = SparkSession.builder.appName("StockDataAnalysis").getOrCreate()

# Load CSV into Spark DataFrame
df = spark.read.csv("data/processed_stock_data.csv", header=False, inferSchema=True)

# Rename columns for readability
df = df.toDF("Open", "High", "Low", "Close", "Volume", "Dividends", "Stock_Splits")

# Show first few rows
print("✅ Loaded Stock Data:")
df.show(5)

# Define a window function for moving average (5-period)
window_spec = Window.orderBy("Open").rowsBetween(-4, 0)
df = df.withColumn("Moving_Avg", avg("Close").over(window_spec))

# Show processed data
print("✅ Processed Data with Moving Average:")
df.show(10)

# Save results
if df.count() == 0:
    print("❌ No data to write! DataFrame is empty.")
else:
    print(f"✅ Data contains {df.count()} rows. Writing to CSV...")
    df.write.csv("data/stock_data_spark_output", header=True, mode="overwrite")
    print("✅ Processed stock data saved successfully!")



print("✅ Processed stock data saved successfully!")
 
