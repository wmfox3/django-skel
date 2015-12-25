django-skel
===========

A modern Django (1.8) project skeleton forked from the excellent work of Randall Degges.

Meta
====

* author: wmfox3
* email:  wmfox3@gmail.com
* status: maintained, in development
* notes:  Have feedback? Please send me an email. This project is still in its
          infancy.


Background
=======

For background, see Randall Degges' notes at: http://rdegges.com/deploying-django

Purpose
====

Essentially--deploying Django projects is hard. There are lots of things you
need to take into consideration. Being a Django user for years, I believe I've
found some extremely useful patterns to help manage all sorts of Django sites
(from the very smallest apps, to the largest).

This project is meant to be a boilerplate project for starting development. It
is heavily opinionated in terms of services and tools--but I think the tradeoff
is worthwhile.

Docs
====

The original project documentation is hosted at RTFD: http://django-skel.rtfd.org/.

Install
=======

django-skel currently supports Django 1.8. To create a new django-skel base
project, create a virtual environment, activate it and install Django 1.8.
This assumes you are using virtualenvwrapper:
(see http://virtualenvwrapper.readthedocs.org/en/latest/index.html)

    $ mkvirtualenv env
    (env) $ pip install Django==1.8

    (env) $ django-admin.py startproject --template=https://github.com/wmfox3/django-skel/zipball/1.8 woot

Where  ``env`` is the environment and ``woot`` is the name of the project you'd like to create.

This is possible because Django 1.8's ``startproject`` command allows you to
fetch a project template over HTTP (which is what we're doing here).

The next thing you’ll probably want to do is remove my project docs:

    (env) $ rm -rf docs README.md

That way you don’t get the documentation you’re reading right now in your new project.

Next, create your first django app for this project:

    (env) $ $ mkdir woot/apps/myapp
    (env) $ $ django-admin.py startapp myapp woot/apps/myapp

Now's a good time to initialize the git repository and commit everything:

    (env) $ $ git init
    (env) Initialized empty Git repository in /home/rdegges/Code/ex/woot/.git/
    (env) $ git add .; git commit -m 'First commit using django-skel!'
    ...

Install all the dependancies needed to run the development site:

    (env) $ pip install -r reqs/dev.txt

If the pip command above fails, it means you’re missing some C libraries that are required for some 
of the Python libraries to work. The ones you need (on Ubuntu) are:

    libevent-dev
    libpq-dev
    libmemcached-dev
    zlib1g-dev
    libssl-dev
    python-dev
    build-essential

Initialize the Django database (Django 1.8 uses migrate):

    (env) $ python manage.py migrate

Install the default Bower components:

    (env) $ python manage.py bower install

Start the development server and visit your home page at http://127.0.0.1:8000/:

    (env) $ python manage.py runserver
