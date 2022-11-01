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
```bash
cd mysite
py manage.py migrate
py manage.py loaddata catalog/fixtures/data.json
```

### Run the project 
```bash
cd mysite
py manage.py runserver
```

### Configure .env
Confidential information is stored in the .env file.
In settings.py there are default values of SECRET_KEY, DEBUG and ALLOWED_HOSTS, so you can just run the project. But if you want to change default values, create .env file, copy text from env.example, paste it to .env and make desired changes.

### Entity Relationship Diagram
![ERD](https://user-images.githubusercontent.com/94749729/199280714-68c5ceb0-b694-4460-aebe-1871babfd243.png)
