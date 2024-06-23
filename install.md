### Installation
#### Clone the Repository
- git clone https://github.com/your-username/api_project.git
- cd api_project
#### Set Up Virtual Environment
- python -m venv venv
- source venv/bin/activate (windows)
#### Install Dependencies
- available in requirement.txt file in the project
#### Configure PostgreSQL
- Ensure PostgreSQL is installed and running.
- Create a database for the project.
- Update the database settings in settings.py accordingly.
#### Run Migrations:
- python manage.py migrate
#### Load Data:
- python load_bank_data.py
- python load_branch_data.py
#### Start the Development Server:
- python manage.py runserver
