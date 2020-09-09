# canairio-services

CanAirIO Services

**Conceptual Model**:

[![Conceptual Model](./doc/Canairio-Services-Conceptual.png "Conceptual Model")](./doc/Canairio-Services-Conceptual.png)

---

> Work in progress ...

## Create and setup virtual environment

```bash
# Linux terminal
python -m venv .venv
source .venv/bin/activate
```

## Linux Debian/Ubuntu requirements

```bash
# Linux terminal
sudo apt install libpq-dev
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
# Insite api/ run
python manage.py createsuperuser
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
