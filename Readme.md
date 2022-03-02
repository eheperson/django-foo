
## Prepare the environment

```
python3 -m venv env
source env/bin/activate 

pip install django
pip install djangorestframework
```

## Basic Introduction

Start a django project : `django-admin startproject <project_name> <dir_to_project_be_initialized> `
Run Django server : `python manage.py runserver`
Run Django server on specific port : `python manage.py runserver 8003`
Run Django server with specific ip ßon specific port : `python manage.py runserver 0:8003`
\
Create django app : `python manage.py startapp polls`

___

### File definitions : 
- `admin.py` : ???
- `apps.py` : I'm not sure what is this.
- `models.py`: To create models for the app.
- `tests.py` : To write tests for the app.
- `views.py` : To write views for the app.
- `urls.py` : ???
___
  
## Notes 
-   Each view is responsible for doing one of two things: 
    -   Returning an HttpResponse object containing the content for the requested page
    -   Raising an exception such as Http404.
    - The rest is up to you.

- Your view can read records from a database, or not. 

- It can use a template system such as Django’s – or a third-party Python template system – or not. 

- It can generate a PDF file, output XML, create a ZIP file on the fly, anything you want, using whatever Python libraries you want.

- Adding a shell.py file to the polls ap to testing purposes
    - Execute a Python script from the Django shell : `$ python manage.py shell < myscript.py`

___


### Creating Models
> Edit the polls/models.py file to create models.

*In our poll app, we’ll create two models: Question and Choice. A Question has a question and a publication date. A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.*

### Activating models

> Django apps are “pluggable”: You can use an app in multiple projects, and you can distribute apps, because they don’t have to be tied to a given Django installation.

To include the app in our project, we need to add a reference to its configuration class in the `INSTALLED_APPS` setting. The `PollsConfig` class is in the `polls/apps.py` file, so its dotted path is `'polls.apps.PollsConfig'`. Edit the `core/settings.py` file and add that dotted path to the `INSTALLED_APPS` setting. It’ll look like this:

### Handle Migrations

> Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. You can read the migration for your new model if you like; it’s the file `polls/migrations/0001_initial.py`.

There are three main command runs with `manage.py` to handle migrations on django:
* **`makemigrations`**
  
    `makemigrations` tells Django that we have made some changes to our models and we would like the changes to be stored as a migration.

* **`migrate`**
  
    `migrate` command will run the migrations for us and manage our database schema automatically.
  
* **`sqlmigrate`**
  
    The sqlmigrate command takes migration names and returns their SQL.
    The sqlmigrate command doesn’t actually run the migration on your database - instead, it prints it to the screen so that you can see what SQL Django thinks is required. 
    > It’s useful for checking what Django is going to do or if you have database administrators who require SQL scripts for changes.

    Usage : `python manage.py sqlmigrate polls 0001`


> If you’re interested, you can also run `python manage.py check`; this checks for any problems in your project without making migrations or touching the database.

---


## Templates

Django’s template system separates the design from Python by creating a template that the view can use.

- First create a directory called templates in your polls directory. Django will look for templates in there.

> Your project’s `TEMPLATES` setting describes how Django will load and render templates.\
> The default settings file configures a DjangoTemplates backend whose `APP_DIRS` option is set to `True`.\
> By convention `DjangoTemplates` looks for a `“templates”` subdirectory in each of the `INSTALLED_APPS`.

**Template namespacing**\
Now we might be able to get away with putting our templates directly in polls/templates.\
> Django will choose the first template it finds whose name matches, and if you had a template with the same name in a different application, Django would be unable to distinguish between them.\
> We need to be able to point Django at the right one, and the best way to ensure this is by namespacing them.\
> That is, by putting those templates inside another directory named for the application itself.\
> Within the templates directory you have just created, create another directory called polls, and within that create a file called index.html.

## Static Files

* First, create a directory called static in your app directory.
* Django will look for static files there, similarly to how Django finds templates inside `<app>/templates/`.
* Django’s `STATICFILES_FINDERS` setting contains a list of finders that know how to discover static files from various sources.
* One of the defaults is `AppDirectoriesFinder` which looks for a “static” subdirectory in each of the `INSTALLED_APPS`, like the one in polls we just created. The admin site uses the same directory structure for its static files.

**Static file namespacing**

Django will choose the first static file it finds whose name matches, and if you had a static file with the same name in a different application, Django would be unable to distinguish between them. We need to be able to point Django at the right one, and the best way to ensure this is by namespacing them. That is, by putting those static files inside another directory named for the application itself.
> Within the static directory you have just created, create another directory called polls and within that create a file called style.css. In other words, your stylesheet should be at `polls/static/polls/style.css`.


### Django Rest Framework

```
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
pip install pygments  # We'll be using this for the code highlighting
```

```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views.\
Add the following to your root urls.py file.
```
urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls'))
]
```

Any global settings for a REST framework API are kept in a single configuration dictionary named `REST_FRAMEWORK`.\ 
Start off by adding the following to your `settings.py` module:
```
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
```



### Introducing the Django Admin

> Generating admin sites for your staff or clients to add, change, and delete content is tedious work that doesn’t require much creativity. For that reason, Django entirely automates creation of admin interfaces for models.\
> **The admin isn’t intended to be used by site visitors. It’s for site managers.**

First we'll alcreate an initial admin user named 'admin' with a password of '1'
```
python manage.py createsuperuser --email admin@example.com --username admin
``` 

**Make the poll app modifiable in the admin**

Only one more thing to do:

we need to tell the admin that Question objects have an admin interface. 

To do this, open the `polls/admin.py` file, and edit it to look like this:

```
from django.contrib import admin
from .models import Question

admin.site.register(Question)
```