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

## Create new Django app

```bash
# Inside api project run {app_name}
python manage.py startapp {app_name}
```

## Run the app locally

```bash
# Run the app locally
heroku local web
```
