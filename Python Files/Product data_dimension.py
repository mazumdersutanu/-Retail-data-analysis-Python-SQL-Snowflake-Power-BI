import pandas as pd
import random
import csv

num_rows = 1000
csv_file = "DimProduct.csv"
file_path_csv = os.path.join(directory, csv_file)


directory  = "D:/Retails sales data/"
file_path  = os.path.join(directory, "LookupFile.xlsx")

with open(file_path_csv, mode='w', newline='') as file:
    writer = csv.writer(file)

header = ['ProductID', 'ProductName', 'Category', 'Brand', 'UnitPrice']
writer.writerow(header)

    for i in range(1, num_rows + 1):
        row = [
            df_check_products['Product Name'].sample(n=1).values[0],
            df_check_categories['Category Name'].sample(n=1).values[0],
            random.choice([
                'FakeLuxeAura',
                'FakeUrbanGlow',
                'FakeEtherealEdge',
                'FakeVelvetVista',
                'FakeZenithStyle'
            ]),
            random.randint(100, 1000)
        ]
writer.writerow(row)
        
 
print("DimProduct.csv generated successfully!")
print(f"Total Rows : {num_rows}")
print(f"Saved at   : {file_path_csv}")