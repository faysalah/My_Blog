## My Blog

    python version 3  
    virtualenv 1.2.5

### Required packages

    pip install Django==2.0.3
    pip install mysqlclient==1.3.1

###  Fllowing steps to run project
##### 1. create a database on mysql 

##### 2. goto settings.py in Blog directory and change this config as your database name, user, password and port

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'demo_django',
            'USER': 'root',
            'PASSWORD': '',
            'HOST':'localhost',
            'PORT':''
        }
    }
    
##### 3.  this command to generate database

    python manage.py migrate

##### 4.  this command to run project    
    
    python manage.py runserver
  
