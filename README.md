# Run locally
 - Required: Python
 - Run: `pip install -r requirements.txt` to install dependencies
 - Run: `manage.py migrate` to create database (SQLite3)
 - Run: `manage.py createsuperuser` to create admin account
 - Setup via URL: `http://localhost:8000/admin`
 - Enjoy application at: `http://localhost:8000`

# Deploy to Heroku
## Migrate database
`heroku run python manage.py migrate`

## Create Superuser
`heroku run python manage.py createsuperuser`