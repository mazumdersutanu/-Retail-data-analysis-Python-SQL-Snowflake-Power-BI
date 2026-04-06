import snowflake.connector
import os

# connection
conn = snowflake.connector.connect(
    user = 'FASTLEARN',
    password = 'SecurePass2024',
    account = 'VOC75589',
    warehouse = 'COMPUTE_WH',
    database = 'RETAIL_ANALYTICS',
    schema = 'RETAIL_SCHEMA'
)

print("✅ Connected to Snowflake!")
cursor = conn.cursor()

directory = "D:/Retails sales data/"


# each csv file mapped to its snowflake table

files_to_load = {"DimDate.csv" : "DIMDATE", "DimCustomer.csv" : "DIMCUSTOMER", "DimProduct.csv" : "DIMPRODUCT",
                 "DimStore.csv" : "DIMSTORE", "FactOrders.csv" : "FACTORDERS", "DimLoyaltyProgram.csv" : "DimLoyaltyProgram"}


# loop through each file and load it
for csv_file, table_name in files_to_load.items():
file_path = os.path.join(directory, csv_file)

    # check if file exists before trying to load
    if not os.path.exists(file_path):
        print(f"❌ File not found — skipping : {csv_file}")
        continue

    print(f"\nLoading {csv_file} → {table_name}...")

    # step 1 — put file into snowflake internal stage
    put_command = f"""
        PUT file://{file_path} @%{table_name}
        AUTO_COMPRESS = TRUE
        OVERWRITE = TRUE
    """
    cursor.execute(put_command)
    print(f"File uploaded to stage")

    # step 2 — copy from stage into actual table
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

    # step 3 — verify row count
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    row_count = cursor.fetchone()[0]
    print(f"Total rows in {table_name} : {row_count}")


print("\nAll files loaded successfully into Snowflake!")
