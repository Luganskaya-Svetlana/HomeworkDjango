# HomeworkDjango
Python project for Yandex.Intensive 


### Workflow status
![workflow](https://github.com/Luganskaya-Svetlana/HomeworkDjango/actions/workflows/python-package.yml/badge.svg)


### Install the project
```bash 
git clone https://github.com/Luganskaya-Svetlana/HomeworkDjango
```

### Create a virtual environment
Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```bash
python -m venv venv
venv\Scripts\activate
```


### Install required libraries
```bash
pip install -r requirements.txt
```

### Configure DataBase
Commited db is just an example. 
For loading data to a new db use:
```bash
cd mysite
py manage.py makemigrations
py manage.py migrate
py manage.py loaddata catalog/fixtures/data.json
```
For creating superuser (to get access to the admin panel) use:
```bash
cd mysite
py manage.py createsuperuser
```

### Run the project 
```bash
cd mysite
py manage.py runserver
```

### Configure .env
Confidential information is stored in the .env file.
In settings.py there are default values of SECRET_KEY, DEBUG, ALLOWED_HOSTS and ADMIN_MAIL, so you can just run the project. But if you want to change default values, create .env file, copy text from env.example, paste it to .env and make desired changes.

### Entity Relationship Diagram
![ERDv4](https://user-images.githubusercontent.com/94749729/203385407-0cbbf750-bf13-4436-94c4-1adf175aa095.png)


