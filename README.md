django-skel
===========

A modern Django (1.5) project skeleton.

![A fancy Django project skeleton](https://github.com/rdegges/django-skel/raw/master/docs/source/_static/skel.jpg)


Meta
====

* author: Randall Degges
* email:  rdegges@gmail.com
* status: maintained, in development
* notes:  Have feedback? Please send me an email. This project is still in its
          infancy, and will be changing rapidly.


Purpose
=======

For background, see: http://rdegges.com/deploying-django

Essentially--deploying Django projects is hard. There are lots of things you
need to take into consideration. Being a Django user for years, I believe I've
found some extremely useful patterns to help manage all sorts of Django sites
(from the very smallest apps, to the largest).

This project is meant to be a boilerplate project for starting development. It
is heavily opinionated in terms of services and tools--but I think the tradeoff
is worthwhile.


Docs
====

The full project documentation is hosted at RTFD: http://django-skel.rtfd.org/.
They are continuously updated to reflect changes and information about the
project, so be sure to read them before using this boilerplate.


Install
=======

django-skel currently supports Django 1.8. To create a new django-skel base
project, create a virtual environment, activate it and install Django 1.8.
This assumes you are using virtualenvwrapper:
(see http://virtualenvwrapper.readthedocs.org/en/latest/index.html)

    $ mkvirtualenv env
    (env) $ pip install Django==1.8

    (env) $ django-admin.py startproject --template=https://github.com/wmfox3/django-skel/zipball/1.8 woot
    (env) $ heroku config:add DJANGO_SETTINGS_MODULE=myproject.settings.prod


Where  ``env`` is the environment and ``woot`` is the name of the project you'd like to create.

This is possible because Django 1.8's ``startproject`` command allows you to
fetch a project template over HTTP (which is what we're doing here).

While not strictly required, it is also recommended to do

     $ heroku config:add SECRET_KEY=putsomethingfairlycomplexhere

The production settings pull SECRET_KEY from environment but fallbacks
to a value which is generated mainly for development environment.

This setup allows you to easily keep your site in a public repo if you so
wish without causing opening a route to attack your Django passwords.

CD to the project directory and remove the unnecessary README.md and docs directory

    (env) $ cd woot
    (env) $ rm -rf docs README.md

Create your first app:

    (env) $ $ mkdir woot/apps/myapp
    (env) $ $ django-admin.py startapp myapp woot/apps/myapp

Now's a good time to initialize the git repository:

    (env) $ $ git init
    (env) Initialized empty Git repository in /home/rdegges/Code/ex/woot/.git/
    (env) $ git add .; git commit -m 'First commit using django-skel!'
    ...

Install the development requirements:

    (env) $ pip install -r reqs/dev.txt

Initialize the Django database (Django 1.8 uses migrate):

    (env) $ python manage.py migrate

Install the default Bower components:

    (env) $ python manage.py bower install

Start the development server and visit your home page at http://127.0.0.1:8000/:

    (env) $ python manage.py runserver
