Project maded in Python - Django - Django Rest Framework

clone this repositorie and then:

- Make a virtualenv with the comand: 
```
virtualenv venv
```
- activate venv with command if you are in linux : 

```
source venv/bin/activate
```
If you are uin Windows you have to serache the path with cd command to venv/Scripts/activate

- install dependencies: 
```
pip install -r requirements.txt
```
- use a postgres database with name payment_challenge or you can change de databese config to SQLITE in settings avoiding this step.
- run the command to migrate models to your database: 
```
python manage.py migrate
```
- Then you can run the server and test:

```
python manage.py runserver
```
URLS
localhost:8000/payables
localhost:8000/transactions

payables params in GET method:
-service_type

transactions params in GET method:
-start_date
-end_date



