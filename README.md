# api_project
This project is designed to provide REST API endpoints for retrieving bank and branch details. Set up the project and app in the virtual enviorment which avoids python packages to install globally ill install packages within the environment, which does not affect the base Python installation in any way and also it includes functionalities for creating and retrieving bank and branch information, using technologies like HTML and Bootstrap for better data visualization and pagination with 10 branches for page . The project also involves using Python scripts to read data from CSV files and load it into a PostgreSQL (v.16) database.

## Features
API ENDPOINTS
- Create Bank (/api/create_bank/): Allows creation of a new bank.
- Get Banks (/api/get_banks/): Retrieves a list of all banks.
- Create Branch (/api/create_branch/): Allows creation of a new branch for a specified bank.
- Get Branches (/api/get_branch/): Retrieves a paginated list of all branches.
  
REQUIREMENTS
- Installed packages like postgresql which can be seen in the requirement.txt file in the project
- With the help of bul_create able to send data in less time 
- Tested REST API endpoints with the help of postman

TimeTaken
- Three days 
