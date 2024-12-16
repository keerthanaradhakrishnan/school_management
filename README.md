# School Management System

## Description
A Django REST Framework (DRF) application with Role-Based Access Control (RBAC) to manage:
- Students
- Library History
- Fees History

## Features
- JWT Authentication
- Role-Based Access:
  - Admin: Full access.
  - Office Staff: Manage students and fees.
  - Librarian: View-only access to students and library.
 school_management/
    main/
        models.py       # Database models
        serializers.py  # API serializers
        views.py        # API views
        urls.py         # API endpoints
        management/
            commands/
                seed_users.py  # Script to create default users
    school_management/
        settings.py     # Project settings
        urls.py         # Main project URLs
    README.md
    manage.py 

## Setup
1. Create a virtual environment:
   virtualenv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

2.Install required packages:
pip install django djangorestframework djangorestframework-simplejwt

3.Set Up the Project:
Create a Django project and app:
django-admin startproject school_management
cd school_management
django-admin startapp main

Apply migrations:
python manage.py makemigrations
python manage.py migrate

Seed default users:
python manage.py seed_users

4. Run the Server:

Start the development server:
python manage.py runserver

5.Testing the APIs:

5.1 Authentication:

Use the /api/token/ endpoint to get a JWT token for one of the predefined users:
Admin: admin/admin123
Office Staff: officestaff/office123
Librarian: librarian/lib123

5.2 CRUD Operations:

Students: /api/students/
Library History: /api/library/
Fees History: /api/fees/
Use tools like Postman to test the API endpoints.

Default User Roles
Role	Username	Password
Admin	admin	admin123
Office Staff	officestaff	office123
Librarian	librarian	lib123
