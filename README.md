# 4300-Project

INSTALLING PROJECT
- open IDE and create new project
    - I highly recommend using PyCharm as it is purpose built for python and be the easiest to run the project   
- download project files into new project directory 
    - or install from git repository using: https://github.com/zekesiegman/4300-Project.git  
    - if using pycharm, click VCS drop down at the top of the screen, the click get from version control and input git url  
- install python packages, can be done with pip in terminal or with built in IDE package installer 
    - install Django
    - install django-bootstrap5
    - install cryptography 
 
 RUNNING PROJECT 
 - on first set up: 
    - cd into mysite directory 
    - open IDE terminal
    - run: python manage.py runserver 
    - click on localhost link  
 - if you want to access the admin page (access point for database), run the server and add /admin to the url 
    - username: admin
    - password: admin  
 
 GENERAL SITE INFO 
 - Functionalities include: login/logout/register, veiwing product information, searching for a product,
    adding and removing a product to your cart, and checking out by providing payment info
    - user password and credit card number are both encrypted by the system 
 - The project was tested on chrome for Windows 10
 - We used the Django MVC framework with additional libraries of bootstrap 5 for css styling and cryptography for encrypting card numbers
 - Django does not offer much starter code other than creating the blank files for settings, urls, models, and views
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
