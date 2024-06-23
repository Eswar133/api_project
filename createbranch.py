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
from bank.models import Bank,Branch
csv_file = 'data/bank_branches.csv'  
data = []
print("success")
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    # Printing column name for debubbing
    print("CSV Columns:", csv_reader.fieldnames)
    bank_dict = {}
    for row in tqdm(csv_reader):
        # Send bank data
        bank_name = row.get('bank_name')
        bank_id = None
        if bank_name in bank_dict:
            bank_id = bank_dict[bank_name]
        else:
            bank_id = Bank.objects.get(name=bank_name).id
            bank_dict[bank_name] = str(bank_id)
        try:    
            branch_data = {
                    'ifsc': row['ifsc'],  
                    'bank_id': bank_id,  
                    'branch': row.get('branch_name',''),
                    'address': row.get('address',''),
                    'city': row.get('city',''),
                    'district': row.get('district',''),
                    'state': row.get('state','')
                }  
            data.append(branch_data)
        except:
            print("Invalid data",row)
#with open("data/bank_branches.json","w") as js:
#  json.dump(data,js,indent=2)
    
branch_objects = [Branch(**branch_data) for branch_data in data]
Branch.objects.bulk_create(branch_objects)