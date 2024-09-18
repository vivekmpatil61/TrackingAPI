TrackingAPI:
TrackingAPI is a Django-based web application designed to generate and manage unique tracking numbers for parcels. This API is built to handle high concurrency and provide efficient tracking number management.

Features:
Generate Unique Tracking Numbers: Create unique tracking numbers for each parcel.
High Concurrency Handling: Designed to handle multiple requests efficiently.
RESTful API: Interact with the API through standard HTTP methods.
Getting Started
Prerequisites
Python 3.10 or later
Django 5.1.1
Gunicorn for production (optional, use Waitress on Windows)
Installation

Clone the repository:
git clone https://github.com/vivekmpatil61/TrackingAPI.git
cd TrackingAPI

Create a virtual environment:
python -m venv venv
Activate the virtual environment:

On Windows:
venv\Scripts\activate

On Unix/macOS:
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Configuration
Database Setup: Configure your database settings in TrackingAPI/settings.py. By default, it uses SQLite.

Environment Variables: Set up necessary environment variables (e.g., DJANGO_SETTINGS_MODULE, DATABASE_URL) in your .env file.

Running the Development Server
To start the development server, use the following command:

bash
Copy code
python manage.py runserver
Running with Gunicorn (for Unix-based systems)
For production, you can use Gunicorn:

bash
Copy code
gunicorn TrackingAPI.wsgi:application
Running with Waitress (for Windows)

Install Waitress:
pip install waitress

Run the application:
waitress-serve --host=0.0.0.0 --port=8000 TrackingAPI.wsgi:application
Testing
To run tests, use:
Instructions for Render:

Push your code to a Git repository (GitHub, GitLab, or Bitbucket).
Create a new Web Service on Render.
Connect your Git repository and deploy the app.
Contributing
We welcome contributions to the project. Please follow these guidelines:

Fork the repository.
Create a new branch for your changes.
Submit a pull request describing your changes.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any inquiries or support, please contact:

Name: Vivek Patil
Email: vivekmpatil61@gmail.com
