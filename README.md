# Contact-storage-and-emailing
This is a simple Flask application that provides an API for managing contact details. It supports basic CRUD operations: Create, Read, Update, and Delete. The application uses SQLite as the database and Flask-Migrate for handling database migrations.

Features
Create a new contact with name, email, and phone number.
Read contact details by name.
Update contact details by name.
Delete a contact by name.
Installation
Clone the Repository:

bash

git clone https://github.com/yourusername/your-repository-name.git
Navigate to the Project Directory:

bash

cd your-repository-name
Set Up a Virtual Environment:

bash

python3 -m venv venv
Activate the Virtual Environment:

On macOS and Linux:

bash

source venv/bin/activate
On Windows:

bash

venv\Scripts\activate
Install the Required Packages:

bash
pip install -r requirements.txt
Configuration
The application uses SQLite for the database. The database URI is set in the app.config:

python

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
Running the Application
Initialize the Database:

The database will be created automatically when you run the application for the first time.

Start the Flask Server:

bash

python server.py
The application will run on http://127.0.0.1:5001.

API Endpoints
Get Details
Endpoint: /get_details
Method: GET
Parameters:
name (query parameter): Name of the contact.
Response:
Success (200): Contact details in JSON format.
Error (400): Missing name parameter.
Error (404): Contact not found.
Add Details
Endpoint: /add_details
Method: POST
Body:
json

{
  "Name": "string",
  "Email": "string",
  "Phone": "string"
}
Response:
Success (201): Confirmation message.
Error (400): Missing name parameter.
Error (409): Contact already exists.
Update Details
Endpoint: /update_details
Method: PUT
Body:
json

{
  "Name": "string",
  "Email": "string",
  "Phone": "string"
}
Response:
Success (200): Confirmation message with updated data.
Error (400): Missing name parameter.
Error (404): Contact not found.
Delete Details
Endpoint: /delete_details
Method: DELETE
Parameters:
name (query parameter): Name of the contact to be deleted.
Response:
Success (200): Confirmation message.
Error (400): Missing name parameter.
Error (404): Contact not found.
Requirements
Flask
Flask-SQLAlchemy
Flask-Migrate
Requests (for testing)
You can install the required packages using:

bash

pip install -r requirements.txt
