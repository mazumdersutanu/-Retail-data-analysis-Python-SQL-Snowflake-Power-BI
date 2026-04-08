import snowflake.connector
import os

conn = snowflake.connector.connect(
    user = '######',
    password = '######',
    account = '######',
    warehouse = '######',
    database = 'RETAIL_ANALYTICS',
    schema = 'RETAIL_SCHEMA'
)

print("Connected to Snowflake!")
cursor = conn.cursor()

directory = "D:/Retails sales data/"

files_to_load = {"DimDate.csv": "DIMDATE", "DimCustomer.csv": "DIMCUSTOMER", "DimProduct.csv": "DIMPRODUCT",
                 "DimStore.csv": "DIMSTORE", "FactOrders.csv": "FACTORDERS", "DimLoyaltyProgram.csv": "DimLoyaltyProgram"}



      for csv_file, table_name in files_to_load.items():
          file_path = os.path.join(directory, csv_file)

    
     if not os.path.exists(file_path):
        print(f"File not found — skipping : {csv_file}")
        continue
        print(f"\nLoading {csv_file} → {table_name}...")

    
    put_command = f"""
        PUT file://{file_path} @%{table_name}
        AUTO_COMPRESS = TRUE
        OVERWRITE = TRUE
    """
    cursor.execute(put_command)
    print(f"File uploaded to stage")

    copy_command = f"""
        COPY INTO {table_name}
        FROM @%{table_name}
        FILE_FORMAT = (
            TYPE = 'CSV'
            SKIP_HEADER = 1
            FIELD_OPTIONALLY_ENCLOSED_BY = '"'
            NULL_IF = ('NULL', 'null', '')
            EMPTY_FIELD_AS_NULL = TRUE
            DATE_FORMAT = 'YYYY-MM-DD'
        )
        ON_ERROR = 'CONTINUE'
    """
    cursor.execute(copy_command)
    print(f"Data loaded into {table_name}")

    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    row_count = cursor.fetchone()[0]
    print(f"Total rows in {table_name} : {row_count}")


print("\nAll files loaded successfully into Snowflake!")