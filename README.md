# Python Script with PyODBC

This Python script connects to a database using PyODBC, retrieves data, and prints it using pandas.

## Prerequisites

- Python 3.x installed
- Required Python packages: pyodbc, pandas

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/0nur0duncu/python-files.git
   ```

2. Install the required packages:

   ```bash
   pip install pyodbc pandas
   ```

3. Create a `settings.json` file with your database parameters:

   ```json
   {
     "Database_parameter": {
       "Driver": "your_driver",
       "Server": "your_server",
       "Database": "your_database",
       "Username": "your_username",
       "Password": "your_password",
       "Trusted_Connection": "yes/no",
       "Encrypt": "yes/no"
     }
   }
   ```

## Usage

1. Run the script:

   ```bash
   python pydb.py
   ```

2. View the output, which includes the top 5 rows of the 'Orders' table and the SQL Server version.
