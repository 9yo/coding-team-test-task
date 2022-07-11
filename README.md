# Run
1. Setup PostgreSQL  as in backend/backend/settings.py DATABASES.

2. Run in teminal:
``` terminal
python -m venv venv
source venv/bin/activate #optional
pip install -r requirements.txt
cd backend
python manage.py migrate
python manage.py seed # to fill database as in task.txt
python manage.py runserver
```
Send request to http://localhost:8000/api/v1/foods/
