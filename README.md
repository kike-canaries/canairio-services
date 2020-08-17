# canairio-services

CanAirIO Services

---

> Work in progress ...

## Create and setup virtual environment

```bash
# Linux terminal
python -m venv .venv
source .venv/bin/activate
```

## Install Python requirements

```bash
# Linux terminal
pip install -r requirements.txt
```

## Setup environment variables

```bash
# Local .env file
cp -fv example.env .env
```

## Creating an admin user

Read Documentation: [here](https://docs.djangoproject.com/en/3.0/intro/tutorial02/#creating-an-admin-user)

```bash
# Linux terminal
python api/manage.py createsuperuser
# ---
Username: admin
Email address: admin@example.com
Password: **********
Password (again): *********
Superuser created successfully.
```

## Run the app locally

```bash
# Run the app locally
heroku local web
```

### Static Content

```bash
# In a browser go to:
http://localhost:5000/
```

### Admin Content

```bash
# In a browser go to:
http://localhost:5000/admin
```
