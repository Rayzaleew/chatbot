# [ChatBot]


**Simple chatbot implementation using OpenAI API**

---

## Overview


What's ready?

* Understanding and responding to any text prompt
* Storing messages in database and remembering context of dialogue
* Responsive user interface
* This applications provides basic API, which means you can customize frontend as much as you want without changing logic of backend



**Below**: *Screenshot of the project*

![Screenshot][image]



## Requirements

* Python 3.6+
* Django 3.1+
* djangorestframework 3.12+
* python-dotenv
* openai

I **highly recommend** using the latest patch release of all these packages.

## Installation

--> First of all, clone this repository:

    git clone https://github.com/Rayzaleew/chatbot
    
--> Move into the directory where we have the project files :

    cd chatbot
    
--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv env #or python -m virtualenv if you're using Windows

```

--> Activate the virtual environment :
```bash
env\scripts\activate #or env\Scripts\activate.bat if you're using Windows

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

## Database configuration

--> Change name of the chatbot/.env.sample file to chatbot/.env and specify data of your database. For example:
```
SECRET_KEY = 'some-secret-key' 
OPENAI_API_KEY = 'YOUR-API-KEY' #specify your OpenAI API key, that you can get on https://platform.openai.com/account/api-keys

#DATABASES
ENGINE   = 'django.db.backends.sqlite3' 
NAME     = 'chat.db'

```
*For detailed explanation of how to connect to specific SQL database visit [Django documentation][django-docs]* 


--> Apply migrations to your database:
```bash
python manage.py makemigrations
python manage.py migrate

```

--> Create superuser:

    python manage.py createsuperuser
    


#

## Running development server

--> To run the ChatBot, use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/



## Deployment

You can use nginx + gunicorn (Linux) or mod_wsgi + Apache (Windows) to deploy this application. 

Don't forget change DEBUG option to False in settings.py and collect all static files to one place:

        python manage.py collectstatic



## *To-Do:*

* Create DockerFile for fast deployment
* ~Add public registration and replace login template~
* Add support for different dialogues (it's only one room for now)
* Optimise storing messages and context of dialogue (it's just adding previous messages to current prompt)
* Improve user interface



[demo]: https://chat.w3b.dedyn.io/chat
[image]: https://user-images.githubusercontent.com/104368253/226906808-c055a331-4d33-44db-817b-27b47e191d7d.png
[django-docs]: https://docs.djangoproject.com/en/4.1/ref/databases/
