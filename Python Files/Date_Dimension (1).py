import pandas as pd
import os

directory = "D:/Retails sales data/"

# start date and end date between which we need to generate our dates.
start_date = '2014-01-01'
end_date   = '2024-12-31'

# generate a series of dates between the start and the end date 
date_range = pd.date_range(start=start_date, end=end_date)

# convert these series of dates into a data frame 
date_dimension = pd.DataFrame(date_range, columns=['Date'])

# add new columns to our dataframe DayofWeek Month Quarter Year Isweekend DateID
date_dimension['DayofWeek'] = date_dimension['Date'].dt.dayofweek
date_dimension['DayName']   = date_dimension['Date'].dt.day_name()   
date_dimension['Month']     = date_dimension['Date'].dt.month
date_dimension['MonthName'] = date_dimension['Date'].dt.month_name()
date_dimension['Quarter']   = date_dimension['Date'].dt.quarter
date_dimension['Year']      = date_dimension['Date'].dt.year
date_dimension['IsWeekend'] = date_dimension['DayofWeek'].isin([5, 6])
date_dimension['DateID']    = date_dimension['Date'].dt.strftime('%Y%m%d').astype(int)

# Reorder — DateID as first column
cols = ['DateID'] + [col for col in date_dimension.columns if col != 'DateID']
date_dimension = date_dimension[cols]

# Save to your directory
file_path = os.path.join(directory,"DimDate.csv")
date_dimension.to_csv(file_path, index=False)

print("DimDate.csv saved successfully!")
print("Total Rows :", len(date_dimension))
print("Total Columns :", len(date_dimension.columns))
print("Saved at :", file_path)