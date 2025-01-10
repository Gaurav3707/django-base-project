# Django Project Setup Guide

## Prerequisites

Before setting up the project, ensure you have the following installed:

- Python (3.x)
- pip (Python package manager)
- virtualenv (Python virtual environment tool)
- Django (if not specified in `requirements.txt`)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Create and Activate Virtual Environment

#### On Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory of your project and add the following environment variables:

```env
# Security and Debug
SECRET_KEY = ''
DEBUG = ''

# Database Configuration
DB_NAME = ''
DB_USER = ''
DB_PASSWORD = ''
DB_HOST = ''
DB_PORT = ''

# Email Configuration
DEFAULT_FROM_EMAIL = ''
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = ''
EMAIL_USE_TLS = ''

# Exception Email Recipients
EXCEPTION_MAIL_RECIPIENTS = []
```

Update the values with your project-specific configurations.

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin account.

### 7. Start the Development Server

```bash
python manage.py runserver
```

Access the server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Optional: Import Postman Collection

If you need to test APIs with Postman, the Postman collection is available in the `/postman` directory in JSON format.

### Steps to Import:
1. Open Postman.
2. Go to the **Collections** tab.
3. Click on **Import**.
4. Select the JSON file from the `/postman` directory.
5. Save and use the imported collection to test APIs.

---

## Additional Notes

- Ensure your database configurations in `.env` match your setup.
- For any issues, refer to the Django documentation or contact the project maintainer.
