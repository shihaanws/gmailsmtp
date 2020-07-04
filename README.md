# gmailsmtp
Simple mail forwading backend using Django with gmail's smtp server.



# Requirements

* Install Django web framework  &nbsp; &nbsp; : **$ pip install django**

* Starting a django project &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;   : **$ django-admin startproject projectname**

* To know your version of Django : **$ python -m django --version**

# The development server 

$ python manage.py runserver

# Starting the Django App

$ python manage.py startapp appname


In ``settings.py``:
::

    INSTALLED_APPS = [
        ...
        "sendemail", #add the app name here
        ...
    ]
    
    EMAIL_BACKEND= 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST='smtp.gmail.com'
    EMAIL_USE_TLS=True
    EMAIL_PORT=587
    EMAIL_HOST_USER='fromemailaddress@gmail.com'  #type your from mail address here
    EMAIL_HOST_PASSWORD='frompassword'           #type the password for the from mail address
    
 In ``urls.py``:
::

    INSTALLED_APPS = [
        ...
        "sendemail", #add the app name here
        ...
    ]   
    
***While running the srever dont forget to check the less secure app access***



