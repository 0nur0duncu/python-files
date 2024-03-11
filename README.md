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
   python your_script.py
   ```

2. View the output, which includes the top 5 rows of the 'Orders' table and the SQL Server version.

## Notes

- Ensure that you have the necessary permissions and network access to connect to the specified database.

Make sure to replace placeholders like `your_username`, `your_password`, `your_server`, etc., with your actual database connection details. Additionally, include the correct path to your script in the installation section. This README.md file provides a clear guide for users to set up and run your Python script.
