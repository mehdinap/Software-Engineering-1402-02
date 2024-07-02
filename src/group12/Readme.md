# Group12 Project

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)



## Introduction
This project is developed by Group12. It is a web application built using Flask, a lightweight WSGI web application framework in Python. The application includes various functionalities and follows a modular structure.

## Project Structure
group12/
│
├── pycache/
├── .venv/
├── flask/
├── migrations/
├── static/
├── templates/
├── init.py
├── admin.py
├── apps.py
├── models.py
├── requirements.txt
├── tests.py
├── urls.py
└── views.py


- `__pycache__/` - Contains Python bytecode files.
- `.venv/` - Virtual environment directory.
- `flask/` - Flask application directory.
- `migrations/` - Database migration files.
- `static/` - Static files (CSS, JavaScript, images, etc.).
- `templates/` - HTML template files.
- `__init__.py` - Initialization file for the Flask app.
- `admin.py` - Admin related functionalities.
- `apps.py` - Application configuration.
- `models.py` - Database models.
- `requirements.txt` - List of dependencies.
- `tests.py` - Test cases for the application.
- `urls.py` - URL routing.
- `views.py` - View functions for handling requests.

## Installation
To install and run this project, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/group12.git
    cd group12
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the migrations:**
    ```bash
    flask db upgrade
    ```

## Usage
To run the application, use the following command:
```bash
flask run
