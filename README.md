# 4300-Project

INSTALLING PROJECT
- download and open pycharm
    - you can use other IDEs but i would recommend pycharm as it has integrated git and an interpreter built for python specifically
- create and enter a new project  
- go to the toolbar on the top
    - click on vcs
    - click on get from version control, and put in github url    
- go to toolbar on the bottom and click python packages
    - install Django 
    - install django-crispy-forms
    - install django-bootstrap4
 
 RUNNING PROJECT 
 - on first set up: 
    - open terminal on bottom toolbar
    - 1: python manage.py makemigrations 
    - 2: python manage.py migrate
    - 3: python manage.py runserver
    - 4: click on localhost link 
 - for running later, only do runserver command (3) 
 - if you make changes to the models page, you need to run 1 and 2 before 3 otherwise changes will not be saved
 - if you want to access the admin page, run the server and add /admin to the url 
    - username: admin
    - password: admin  
 
 GENERAL DJANGO STUFF
 - the home directory contains the backend content 
 - the mysite directory contains the backend structure 
 - the static directory is for images, css, and js 
 - the templates directory if for html 
 - models.py is the database
 - views.py is the backend for each running webpage
 - urls.py contains the urls for each running webpage
    - if you add a webpage, you need to add the url to home/urls.py and mysite/urls.py
 - forms.py contains the form templates you can use in html and views 
 - if you want to learn more, the django documentation is REALLY good 
    - also TechWithTim on youtube has a really good playlist for django   
