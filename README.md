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
    cd your-project
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
