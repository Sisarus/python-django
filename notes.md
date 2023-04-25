python3 -m pip install -U -r requirements.txt

python3 manage.py makemigrations onlinecourse

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver

python3 manage.py migrate onlinecourse zero