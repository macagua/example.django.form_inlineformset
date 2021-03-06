=================================
example.django.form_inlineformset
=================================

Example for Django using the `Form <https://docs.djangoproject.com/en/1.8/topics/forms/>`_, `ModelForm <https://docs.djangoproject.com/en/1.8/topics/forms/modelforms/>`_ and `InlineFormSet <https://docs.djangoproject.com/en/1.8/topics/forms/modelforms/#inline-formsets>`_.


Features
========

* A web app example for register kitchen recipes.

* Three models like Recipes, Ingredients, Instructions included.

* A list view and a create and edit view included.

* Also you can create, search, list, update and delete Recipes, Ingredients or Instructions via the Django Admin interface.


Requirements
============

* Python 3.7.

* Django 2.1.11.


Installation
============

This web app example requires some Python additional dependencies, for
install it, please, execute the following command:

::

    pip3 install -r requirements.txt --timeout 120


Create the database, please, execute the following command:

::

    cd kitchen_stuff
    python3 manage.py makemigrations
    python3 manage.py migrate


Settings
========

This Django web application needs to create a Django admin user, to access
and manage the admin interface, run the following command:

**Tips**: for this local installation use user as **admin** and password as **admin**.

::

    python3 manage.py createsuperuser --username admin --email admin@mail.com


Run
===

You need to run Django server, run the following command:

::

    python manage.py runserver


You can see the Django web application, opening your web browser with the following URL: `http://0.0.0.0:8000/ <http://0.0.0.0:8000/>`_.

Also you can see Django admin interface, use username **admin** and password **admin**- opening your web browser with the following URL: `http://0.0.0.0:8000/admin/ <http://0.0.0.0:8000/admin/>`_.


References
==========

- `Django 2.1 Project tutorial <https://docs.djangoproject.com/en/2.1/intro/>`_.

- `Django: Ejemplo de Form + InlineFormset <https://alexanderae.com/django-form-inlineformset.html>`_.

- `Django class-based views with multiple inline formsets <http://kevindias.com/writing/django-class-based-views-multiple-inline-formsets/>`_.
