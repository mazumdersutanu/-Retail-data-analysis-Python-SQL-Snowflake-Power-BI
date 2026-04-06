!pip install faker
import csv
import random
import os
from faker import Faker

# Initialize Faker
fake = Faker()

# Number of rows & file name 
num_rows = 1000          
csv_file = "DimCustomer.csv" 
file_path = os.path.join(directory, csv_file)

# Open and write CSV
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)

# Header
    header = ['CustomerID','FirstName','LastName','Gender','DateOfBirth','Email','PhoneNumber','Address','City','State','PostalCode',
              'Country','LoyaltyProgramID']
    
    writer.writerow(header)

    # Generate rows
    for i in range(1, num_rows + 1):
        row = [
            i,                                                              # CustomerID
            fake.first_name(),                                             # FirstName
            fake.last_name(),                                              # LastName
            random.choice(['M', 'F', 'Others', 'Not Specified']),         # Gender
            fake.date_of_birth(minimum_age=18, maximum_age=70),           # ✅ Realistic age
            fake.email(),                                                  # Email
            fake.phone_number(),                                           # PhoneNumber
            fake.address().replace(",", " ").replace("\n", " "),          # Address
            fake.city(),                                                   # City
            fake.state(),                                                  # State
            fake.postcode(),                                               # PostalCode
            fake.country(),                                                # Country
            random.randint(1, 5)                                           # LoyaltyProgramID
        ]
        writer.writerow(row)

print("✅ File generated successfully!")
print(f"Total Rows : {num_rows}")
print(f"Saved at   : {file_path}")