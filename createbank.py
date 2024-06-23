import csv
from tqdm import tqdm
import json
import sys 
import os
import django
DJANGO_PATH = 'C:/Users/manik/api_project/'
sys.path.append(DJANGO_PATH)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_project.settings")

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from bank.models import Bank
csv_file = 'data/bank_branches.csv'  
data = []
print("success")
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    # Printing column name for debubbing
    print("CSV Columns:", csv_reader.fieldnames)
    bank_names = []
    for row in tqdm(csv_reader):
        bank_names.append(row.get('bank_name'))
        # Send bank data
        # bank_data = {
            #'name': row.get('bank_name') 
            #  
        # }   
        #data.append(bank_data)
    bank_names = list(set(bank_names))
    data = [{'name':bank_name} for bank_name in bank_names]
with open("data/bank_branches.json","w") as js:
   json.dump(data,js,indent=2)
    
bank_objects = [Bank(**bank_data) for bank_data in data]
Bank.objects.bulk_create(bank_objects)