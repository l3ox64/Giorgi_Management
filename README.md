# Giorgi_Management

A versatile web application for efficient personnel management.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

Make sure you have the following installed on your machine:

- [Python](https://www.python.org/downloads) (version 3.12.0)
- [SQL Server Express](https://www.microsoft.com/it-it/download/details.aspx?id=101064) (version 2019)
- [SQL Server Management Studio](https://www.microsoft.com/it-it/download/details.aspx?id=101064](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16)).(version 16)
### Installation

1. Clone the repository:
    ```bash
   git clone https://github.com/l3ox64/Giorgi_Management
   
2. Navigate to the project directory:
   ```bash
   cd Giorgi_Management
   
3. Install pipenv:
   ```bash
   pip install pipenv

4. Run virtual enviroment
   ```bash
   pipenv shell
   
5. Install project dependencies:
   ```bash
   pipenv install -r requirements.txt

6. Creates all the necessary tables:
   ```bash
   python manage.py migrate

7. Create user for test:
   ```bash
    python manage.py createsuperuser

8. Start the Django development server with:
   ```bash
   python manage.py runserver

9. Visit http://localhost:8000/ in your web browser to view your app.

### Integration with MSSQL

   - [Connect Django to Microsoft SQL Server (MSSQL) Database](https://igeorgiev.eu/python/django/python-django-connect-sql-server-mssql-database/)


