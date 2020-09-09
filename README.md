# canairio-services

CanAirIO Services `Project Description Here`

---

**Conceptual Model**:

[![Conceptual Model](./doc/Canairio-Services-Conceptual.png "Conceptual Model")](./doc/Canairio-Services-Conceptual.png)

---

> Work in progress ...

**TODO:**

- [ ] Add Project Description
- [x] Postman API Documentation
- [ ] Automated Testing with Postman
- [ ] Getting Started Tutorial

---

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

## Admin Content

```bash
# In a browser go to:
http://localhost:5000/admin
```

## Postman API Documentation

Read and review the CanAirIO Services API Documentation in Postman.

[CanAirIO Services API Documentation](https://documenter.getpostman.com/view/2374715/TVCjx6Ba)

## Getting Started

Make sure you check out the [Getting Started with CanAirIO Services](./doc/getting-started.md) tutorial.
