# Travel Django Project

## Description

This Django project is a web application designed to manage travel packages. It includes features for viewing packages, viewing package details, processing payments, and handling user authentication (login, logout, and registration). Users can also contact the support team through a contact form.

## Project Structure

- `myapp/`: Contains the main application logic.
  - `views.py`: Contains view functions for handling requests and responses.
  - `models.py`: Defines the data models for the application.
  - `forms.py`: Contains forms used in the project.
  - `urls.py`: Defines the URL patterns for routing requests to the appropriate views.
- `TRAVEL_DJANGO/`: Contains the project's settings and configuration files.
  - `urls.py`: The project's main URL configuration.

## Installation

1. **Clone the repository:**



   git clone https://github.com/anandmohanam/trip-planner.git

Navigate to the project directory:


cd <trip-planner>

2.**Install the requirements:**



pip install -r requirements.txt


3.**Create a virtual environment:**

python -m venv venv

4.**Activate the virtual environment:**

On Windows:


venv\Scripts\activate

On macOS/Linux:



 venv/bin/activate



5.**Apply migrations:**




python manage.py migrate

6.**Run the development server:**


python manage.py runserver

Access the application at http://127.0.0.1:8000/ in your web browser.