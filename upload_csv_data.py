import csv
import requests
import json

def create_bank(bank_data):
    url = 'http://127.0.0.1:8000/create_bank/'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(bank_data))
    if response.status_code == 201:
        print(f"Bank created successfully: {bank_data['name']}")
        return response.json().get('bank_id')  # Return the bank_id of the created bank
    else:
        print(f"Failed to create bank: {response.status_code} - {response.text}")
        return None

def create_branch(branch_data):
    url = 'http://127.0.0.1:8000/create_branch/'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(branch_data))
    if response.status_code == 201:
        print(f"Branch created successfully: {branch_data['branch_name']}")
    else:
        print(f"Failed to create branch: {response.status_code} - {response.text}")
        print("Branch data:", branch_data)

# Read the CSV file and send data to the API
csv_file = 'C:/Users/manik/OneDrive/Desktop/bank_branches.csv'  # Update with your CSV file path

with open(csv_file, mode='r', newline='') as file:
    csv_reader = csv.DictReader(file)
    # Print the fieldnames (column names) for debugging
    print("CSV Columns:", csv_reader.fieldnames)
    
    for row in csv_reader:
        # Send bank data
        bank_data = {
            'name': row.get('bank_name')  # Adjust the field names based on your CSV columns
        }
        bank_id = create_bank(bank_data)
        
        # Send branch data if bank creation was successful
        if bank_id:
            try:
                branch_data = {
                    'ifsc': row.get('ifsc'),  # Adjust the field names based on your CSV columns
                    'bank_id': bank_id,  # Ensure this matches the created bank's ID
                    'branch_name': row.get('branch_name'),
                    'address': row.get('address'),
                    'city': row.get('city'),
                    'district': row.get('district'),
                    'state': row.get('state')
                }
                
                # Check for missing fields
                if not all(branch_data.values()):
                    print("Missing fields in branch data:", branch_data)
                else:
                    create_branch(branch_data)
            except KeyError as e:
                
                print(f"Missing key in CSV data: {e}")
                print("Row data:", row)
