# Social Media API

A Django-powered API for creating a social media application, featuring user authentication, token-based login, and support for user profile management.

---

## Features
- **Custom User Model** with additional fields like bio, profile picture, and followers.
- **Token-based Authentication** using Django REST Framework's token system.
- Endpoints for user registration, login, and profile management.

---

## Requirements
- Python 3.8+
- Django 4.2+
- Django REST Framework 3.14+

Install dependencies with:
```bash
pip install django djangorestframework
```

---

## Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd social_media_api
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
Run migrations to set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Server
Launch the development server:
```bash
python manage.py runserver
```

---

## Endpoints

### **User Registration**
**POST** `/api/accounts/register/`

**Request Body:**
```json
{
  "username": "example_user",
  "password": "example_password",
  "email": "user@example.com",
  "bio": "This is an example bio",
  "profile_picture": "<file>"
}
```

**Response:**
```json
{
  "token": "<generated_token>"
}
```

---

### **User Login**
**POST** `/api/accounts/login/`

**Request Body:**
```json
{
  "username": "example_user",
  "password": "example_password"
}
```

**Response:**
```json
{
  "token": "<generated_token>"
}
```

---

### **User Profile**
**GET** `/api/accounts/profile/`

Retrieve the user's profile information.

**Response:**
```json
{
  "id": 1,
  "username": "example_user",
  "email": "user@example.com",
  "bio": "This is an example bio",
  "profile_picture": "http://example.com/media/profile_pics/picture.jpg",
  "followers": [],
  "following": []
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



