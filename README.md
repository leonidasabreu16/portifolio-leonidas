python -m venv env

env\Scripts\activate

source env/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

http://localhost:8000/