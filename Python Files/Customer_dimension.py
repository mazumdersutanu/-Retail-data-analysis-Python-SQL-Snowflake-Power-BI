!pip install faker
import csv
import random
import os
from faker import Faker

fake = Faker()

num_rows = 1000          
csv_file = "DimCustomer.csv" 
file_path = os.path.join(directory, csv_file)

with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)

    header = ['CustomerID','FirstName','LastName','Gender','DateOfBirth','Email','PhoneNumber','Address','City','State','PostalCode',
              'Country','LoyaltyProgramID']
     
    writer.writerow(header)

    for i in range(1, num_rows + 1):
        row = [
            i,                                                              
            fake.first_name(),                                             
            fake.last_name(),                                              
            random.choice(['M', 'F', 'Others', 'Not Specified']),        
            fake.date_of_birth(minimum_age=18, maximum_age=70),           
            fake.email(),                                                  
            fake.phone_number(),                                           
            fake.address().replace(",", " ").replace("\n", " "),          
            fake.city(),                                                   
            fake.state(),                                                  
            fake.postcode(),                                               
            fake.country(),                                                
            random.randint(1, 5)                                           
        ]
        writer.writerow(row)

print("File generated successfully!")
print(f"Total Rows : {num_rows}")
print(f"Saved at   : {file_path}")