import pandas as pd
import numpy as np
import os

DATEID = '20240728'
directory = "D:/Retails sales data/"

os.makedirs(directory, exist_ok=True)

for i in range(1, 101):
    num_rows = np.random.randint(100, 1000)
    
    data = {
        'DateID'          : [DATEID] * num_rows,
        'ProductID'       : np.random.randint(1,1001,size=num_rows),
        'StoreID'         : [i] * num_rows,
        'CustomerID'      : np.random.randint(1,1001,size=num_rows),
        'QuantityOrdered' : np.random.randint(1,21,size=num_rows),
        'OrderAmount'     : np.random.randint(100,1001,size=num_rows)
         }
    
    df = pd.DataFrame(data)
    
    discount_perc = np.random.uniform(0.02, 0.15, size=num_rows)
    shipping_perc = np.random.uniform(0.05, 0.15, size=num_rows)

    df['DiscountAmount'] = (df['OrderAmount'] * discount_perc).round(2)
    df['ShippingCost']   = (df['OrderAmount'] * shipping_perc).round(2)
    df['TotalAmount']    = (df['OrderAmount'] - (df['DiscountAmount'] + df['ShippingCost'])).round(2)
    
    file_name = f'Store_{i}_{DATEID}.csv'
    file_path = os.path.join(directory, file_name)
    if os.path.exists(file_path):
        os.remove(file_path) 
    df.to_csv(file_path, index=False)
    
all_files = os.listdir(directory)
print(f"Total files : {len(all_files)}")
print("First 5:", all_files[:5])


df_all = pd.concat(
    [pd.read_csv(os.path.join(directory, f)) for f in all_files],
    ignore_index=True
)

print("\nAll files combined!")
print("Total Rows :", len(df_all))
print("Total Columns:", len(df_all.columns))
df_all.head()