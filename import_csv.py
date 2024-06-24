import csv
import requests
import json
from tqdm import tqdm

def create_bank(bank_data):
    url = 'http://127.0.0.1:8000/api/banks/'  
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(bank_data))
        if response.status_code == 201:
            print(f"Bank created successfully: {bank_data['name']}")
            return response.json().get('bank_id')  
        else:
            print(f"Failed to create bank: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def create_branch(branch_data):
    url = 'http://127.0.0.1:8000/api/create_branch/'  
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(branch_data))
        if response.status_code == 201:
            print(f"Branch created successfully: {branch_data['branch_name']}")
        else:
            print(f"Failed to create branch: {response.status_code} - {response.text}")
            print("Branch data:", branch_data)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

csv_file = 'C:/Users/manik/OneDrive/Desktop/bank_branches.csv'  

with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    # Printing column name for debubbing
    print("CSV Columns:", csv_reader.fieldnames)
    
    for row in tqdm(csv_reader):
        # Send bank data
        bank_data = {
            'name': row.get('bank_name')  
        }
        bank_id = create_bank(bank_data)
        
        # Sending branch data if bank created successfull
        if bank_id:
            try:
                branch_data = {
                    'ifsc': row.get('ifsc'),  
                    'bank_id': bank_id,  
                    'branch_name': row.get('branch_name'),
                    'address': row.get('address'),
                    'city': row.get('city'),
                    'district': row.get('district'),
                    'state': row.get('state')
                }
                
                # Checking for the  missing fields
                if not all(branch_data.values()):
                    print("Missing fields in branch data:", branch_data)
                else:
                    create_branch(branch_data)
            except KeyError as e:
                print(f"Missing key in CSV data: {e}")
                print("Row data:", row)

print("Data import completed.")
