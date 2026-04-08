import pandas as pd
import random
import csv
import Faker from faker


fake = Faker()

directory = "D:/Retails sales data/"
lookup_file_path = os.path.join(directory, "LookupFile.xlsx")

os.makedirs(directory, exist_ok=True)

df_store = pd.read_excel(lookup_file_path, sheet_name='Store Name Data')
print(f"Lookup loaded — {len(df_store)} adjectives/nouns available")
num_rows     = 100
csv_file     = "DimStore.csv"
file_path_csv = os.path.join(directory, csv_file)

with open(file_path_csv, mode='w', newline='') as file:
    writer = csv.writer(file)

header = ['StoreID','StoreName','StoreType','StoreOpeningDate','Address','City','State','Country','Region','ManagerName']

 
 writer.writerow(header)

    for i in range(1, num_rows + 1):
        adj        = df_store['Adjectives'].sample(n=1).values[0]
        noun       = df_store['Nouns'].sample(n=1).values[0]
        store_name = f"The {adj} {noun}"

        row = [i,
            store_name,
            random.choice(['Exclusive', 'MBO', 'SMB', 'Outlet']),
            fake.date_between(start_date='-20y', end_date='today'),
            fake.address().replace("\n", " ").replace(",", " "),
            fake.city(),
            fake.state(),
            fake.country(),
            random.choice(['North', 'South', 'East', 'West']),
            fake.name()
           ]

writer.writerow(row)

print("DimStore.csv generated!")
print(f"Total Rows : {num_rows}")
print(f"Saved at   : {file_path_csv}")

df_store_final = pd.read_csv(file_path_csv)
print("\nShape:", df_store_final.shape)
df_store_final.head(10)