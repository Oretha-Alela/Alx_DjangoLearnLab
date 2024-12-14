# Social Media API

This is a Social Media API built using Django and Django REST Framework, designed to handle user authentication and provide foundational elements for social media functionalities.

---

## Features
- Custom User Model with additional fields like bio, profile picture, and followers.
- Token-based authentication for secure user login and registration.
- Basic endpoints for user registration and login.

---

## Requirements
Ensure you have the following installed:
- Python 3.8+
- Django 4.2+
- Django REST Framework 3.14+

Install required packages:
```bash
pip install django djangorestframework
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd social_media_api
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Initial Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Development Server
```bash
python manage.py runserver
```

---

## Endpoints

### 1. **User Registration**
**POST** `/api/accounts/register/`

#### Request Body:
```json
{
  "username": "example_user",
  "password": "example_password",
  "email": "user@example.com",
  "bio": "This is an example bio",
  "profile_picture": "<file>"
}
```

#### Response:
```json
{
  "token": "<generated_token>"
}
```

---

### 2. **User Login**
**POST** `/api/accounts/login/`

#### Request Body:
```json
{
  "username": "example_user",
  "password": "example_password"
}
```

#### Response:
```json
{
  "token": "<generated_token>"
}
```

---

## Project Structure
```
|-- social_media_api/
    |-- accounts/
        |-- migrations/
        |-- __init__.py
        |-- admin.py
        |-- apps.py
        |-- models.py
        |-- serializers.py
        |-- tests.py
        |-- urls.py
        |-- views.py
    |-- social_media_api/
        |-- __init__.py
        |-- asgi.py
        |-- settings.py
        |-- urls.py
        |-- wsgi.py
    |-- manage.py
```

---

## Notes
- Make sure to configure your database in `settings.py` if you're not using SQLite.
- Use tools like Postman or curl to test the API endpoints.
- For deploying the application, consider platforms like Heroku or PythonAnywhere.

---

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

