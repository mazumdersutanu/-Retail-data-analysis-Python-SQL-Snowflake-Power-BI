import pandas as pd
import numpy as np

directory = "D:/Retails sales data/"
num_rows = 100000  

#  Generate random dates between 2014 and 2024
random_dates   = np.random.choice(np.arange(np.datetime64('2014-01-01'),np.datetime64('2024-12-31')
                    ),
                    size=num_rows
                )
formatted_dates = pd.to_datetime(random_dates).strftime('%Y%m%d')

# ✅ Generate all columns
data = {
    'DateID'          : formatted_dates,
    'ProductID'       : np.random.randint(1, 1001, size=num_rows),
    'StoreID'         : np.random.randint(1, 101,  size=num_rows),
    'CustomerID'      : np.random.randint(1, 1001, size=num_rows),
    'QuantityOrdered' : np.random.randint(1, 21,   size=num_rows),  # ✅ Fixed typo
    'OrderAmount'     : np.random.randint(100, 1001, size=num_rows)
}

df = pd.DataFrame(data)

# ✅ Calculate derived columns
discount_perc          = np.random.uniform(0.02, 0.15, size=num_rows)
shipping_perc          = np.random.uniform(0.05, 0.15, size=num_rows)

df['DiscountAmount']   = (df['OrderAmount'] * discount_perc).round(2)
df['ShippingCost']     = (df['OrderAmount'] * shipping_perc).round(2)   # ✅ Fixed space in name
df['TotalAmount']      = (df['OrderAmount'] - (df['DiscountAmount'] + df['ShippingCost'])).round(2)

# ✅ Add OrderID as unique identifier
df.insert(0, 'OrderID', range(1, num_rows + 1))

# ✅ Save to your directory
file_path = os.path.join(directory, "FactOrders.csv")
df.to_csv(file_path, index=False)

print("✅ FactOrders.csv generated successfully!")
print(f"Total Rows    : {len(df)}")
print(f"Total Columns : {len(df.columns)}")
print(f"Saved at      : {file_path}")