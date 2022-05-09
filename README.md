# 4300-Project

INSTALLING PROJECT
- download and open pycharm
    - you can use other IDEs but i would recommend pycharm as it has integrated git and an interpreter built for python specifically
- create and enter a new project  
- go to the toolbar on the top
    - click on vcs
    - click on get from version control, and put in github url 
           - https://github.com/zekesiegman/4300-Project.git      
- go to toolbar on the bottom and click python packages
    - install Django 
    - install django-crispy-forms
    - install django-bootstrap5
    - install cryptography 
 
 RUNNING PROJECT 
 - on first set up: 
    - open terminal on bottom toolbar
    - 1: python manage.py makemigrations 
    - 2: python manage.py migrate
    - 3: python manage.py runserver
    - 4: click on localhost link 
 - for running later, only do runserver command (3) 
 - if you make changes to the models page, you need to run 1 and 2 before 3 otherwise changes will not be saved
 - if you want to access the admin page (access point for database), run the server and add /admin to the url 
    - username: admin
    - password: admin  
 
 GENERAL SITE INFO 
 - Functionalities include: login/lotout/register, veiwing product information, searching for a product,
    adding and removing a product to your cart, and checking out by providing payment info
    - user password and credit card number are both encrypted by the system 
 - The project was tested on chrome for Windows 10
 - We used the Django MVC framework with additional libraries of bootstrap 5, crispy-forms, and cryptography
 - Django does not offer much starter code other than creating the initial files for settings, urls, models, and views
 - We filled in these starter files with our backend code and added our own HTML pages, everything on the site
   (other than the built in admin page) is 100% our own work and code 
 - Folder structure: 
    - mysite: parent directory 
        - home: our own backend code
            - migrations: changes made to database   
        - mysite: backend code required by django to run the site
        - static: css, images, and JS
        - templates: HTML pages 
        - db.sqlite3: database encoding 
        - manage.py: master file for starting project    
