python3 -m venv .env
sourse .env/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver