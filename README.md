# Multi-Tenancy
Building a Multi-Tenant Supported RESTful API with Django Rest Framework

### Installation
1. Create virtual environment:

   ```bash
   python -m venv env
   cd env
   scripts\activate
   pip install django
   django-admin startproject project
   cd project

2. Clone the repository:

    ```bash
    git clone https://github.com/11Jou/Multi-Tenancy.git
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

The project will be accessible at [http://localhost:8000/](http://localhost:8000/).

### Explanation
To make Api support multi tenancy we can use several approach , one of them is to create a separate database schema for each tenant and each tenant have it's own users
tenants can be identified by a unique identifier ( subdomain or header ) , in this project we used subdomain identifier

1. each tenant is identified by unique subdomain ( nokia.localhost , samsung.localhost )
2. each tenant have it's schema contain tables ---> Items , Auth , Session and etc

by this approch we can achive data isolation strategy because each tenant can only perform a CRUD operation on his own schema
