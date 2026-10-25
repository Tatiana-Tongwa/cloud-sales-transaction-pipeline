# Databricks notebook source
from pyspark.sql.functions import current_timestamp, lit
# Current_timestap used to returns current date and time as a deterministic column value for the duration of a query and lit wraps a static python or scalar value into a spark column.

# 1. Define the source directory
volume_path = "/Volumes/workspace/default/olist/"

# 2. Map source filenames to Bronze table names
sources = {
    "orders": "olist_orders_dataset.csv",
    "items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "products": "olist_products_dataset.csv",
    "categories": "product_category_name_translation.csv"
}

# 3. Automatically discover CSV files in the volume
available_files = {
    file.name: file.path
    #dbutils.fs.ls(volume_path): list files and directories in the databricks volume.
    for file in dbutils.fs.ls(volume_path)
    if file.name.lower().endswith(".csv") and not file.isDir()
}

# 4. Check that all required files exist
missing_files = [
    filename
    for filename in sources.values()
    if filename not in available_files
]

if missing_files:
    raise FileNotFoundError(
        f"Missing source files: {missing_files}"
    )

# 5. Ingest each source into its Bronze Delta table
for table_name, filename in sources.items():

    # Retrieve the full path automatically
    source_path = available_files[filename]

    print(f"Processing: {filename}")

    # Read original CSV records as strings
    df = (
        spark.read
        .option("header", "true")
        .option("inferSchema", "false")
        .csv(source_path)
    )

    # Add ingestion metadata
    bronze_df = (
        df.withColumn("source_file", lit(filename))
          .withColumn("ingested_at", current_timestamp())
    )

    # Define destination table
    destination = f"workspace.default.bronze_olist_{table_name}"

    # Write to Delta Lake
    (
        bronze_df.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(destination)
    )

    # Confirm how many records were saved
    record_count = spark.table(destination).count()

    print(f"Created: {destination}")
    print(f"Records stored: {record_count}")
    print("-" * 40)

print("Bronze ingestion completed successfully!")