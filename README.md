# api_project
This project is designed to provide REST API implemention for bank and  branch  

# API ENDPOINTS
## Create bank (/api/create_bank/): allows creation of a new bank.
- Request method : POST 
- Sample endpoint : http://127.0.0.1:8000/api/create_bank/
- Sample input ```{ "id":"200", "name":"ANDHRA_BANK } ```
- sample output ``` { "message": "Bank created successfully", "bank_id": "128369" }```
- Response code : "201"

## Get Banks (/api/get_banks/): Retrieves a list of all banks.
- Request method : GET
- Sample endpoint : http://127.0.0.1:8000/api/get_banks/
- Sample output ``` {
        "id": 128199,
        "name": "BARCLAYS BANK"
    },
    {
        "id": 128200,
        "name": "STATE BANK OF TRAVANCORE"
    },```

- Response code : "200"

## Create Branch (/api/create_branch/): Allows the creation of a new branch for a specified bank.
- Request method : POST
- Sample endpoint : http://127.0.0.1:8000/api/create_branch/
- Sample input ```{
    "ifsc": "ABC1256",
    "bank_id": 128370,  
    "branch": "MainBranch",
    "address": "123Main St",
    "city": "Springfeld",
    "district": "Sprinfield District",
    "state": "State Name"
}```
- Sample output ``` ```
- Response code :

## Get Branches (/api/get_branch/): Retrieves a paginated list of all branches.
- Request method : GET
- Sample endpoint : http://127.0.0.1:8000/api/get_branch/
- Sample output :```{
    "total_count": 127860,
    "num_pages": 12786,
    "current_page": 1,
    "next": 2,
    "previous": null,
    "results": [
        {
            "ifsc": "ABHY0065001",
            "bank_id": 128234,
            "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED",
            "branch": "RTGS-HO",
            "address": "ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024",
            "city": "MUMBAI",
            "district": "GREATER MUMBAI",
            "state": "MAHARASHTRA"
        },
        {
            "ifsc": "ABHY0065002",
            "bank_id": 128234,
            "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED",
            "branch": "ABHYUDAYA NAGAR",
            "address": "ABHYUDAYA EDUCATION SOCIETY, OPP. BLDG. NO. 18, ABHYUDAYA NAGAR, KALACHOWKY, MUMBAI - 400033",
            "city": "MUMBAI",
            "district": "GREATER MUMBAI",
            "state": "MAHARASHTRA"
        },```
- Sample response : "200"

# TECH STACK
