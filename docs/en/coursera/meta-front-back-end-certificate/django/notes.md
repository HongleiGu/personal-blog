# startup
python installed, then `pip install django`

use `python -m django --version` to check django version

use `django-admin startproject name`

to build a project with name

to run the project, run `python3 manage.py runserver`

to create an app `python -m django startapp myapp`

A **Django project** is the complete web application setup, while a **Django app** is a component of that setup, designed for a specific purpose. This modularity allows for better organization, maintainability, and reusability of code in Django applications.

## views:

```python
from django.shortcuts import render

# create your views here
from django.http import HttpResponse

def home(request):
	return HttpResponse('Hello World')
```

so basically this give out a api that returns Hello World when requested with any method

we can also use render

```python
from django.shortcuts import render

def myview(request):  

  

      if request.method=='GET':  

            #perform read or delete operation on the model  

  

      if request.method=='POST':  

            #perform insert or update operation on the model  

            context={ } #dict containing data to be sent to the client  

  

      return render(request, 'mytemplate.html', context)
```

and even specify the methods

## urls

in the project, we configure

```python
"""

URL configuration for intro project.

  

The `urlpatterns` list routes URLs to views. For more information please see:

    https://docs.djangoproject.com/en/4.2/topics/http/urls/

Examples:

Function views

    1. Add an import:  from my_app import views

    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views

    1. Add an import:  from other_app.views import Home

    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf

    1. Import the include() function: from django.urls import include, path

    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.contrib import admin

from django.urls import path

from introApp import views

  

urlpatterns = [

    path("admin/", admin.site.urls),

    path("", views.home, name = "home"), # added

]
```

the add a new page at the home page

we can also do

```python
from django.urls import path, include
urlpatterns = [

    path("admin/", admin.site.urls),

    path("", include('restaurant.urls')), # added to include all the urls from the app restaurant

]

```

we can also add a param in the url using regex like

```python
path('drinks/<int:id>', views.drinks)

path(r'menu_item/(?P<pk>\d+)$', views.menu, name='menu_item')

# or

re_path(r'menu/[0-9]{2}/$', views.diaplay_menu_item)

```
## MVT:

model, view, template

the view is the apis, model is the data class, template is the frontend

### views:
see above

### models:
so we might do
#### create table

```postgresql
CREATE TABLE user (
	"id" serial NOT NULL PRIMARY KEY,
	"first_name" VARCHAR(30) NOT NULL,
	"last_name" VARCHAR(30) NOT NULL
)
```

```python
from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
```

after creating the model we need to include it the settings.py INSTALLED_APPS, register the models in the admin,py then we migrate with

```
python manage.py makemigrations
python manage.py migrate
```

migrations are used to keep a record of changes made to models and implements the changes to the database schema

##### foreign keys
for example, in Menu

`
`category_id = models.ForeignKey(Menu, on_delete = models.PROTECT, default = None)`



#### insert

```postgresql
INSERT INTO user(id, first_name, last_name)
VALUES (1, "John", "Jones");
```

```python
new_user = User(id = 1, "John", "Jones")
new_user.save()
```

#### select
```postgresql
SELECT * FROM user WHERE id = 1
```

```python
user = User.objects.get(id = 1)
```

we can also do

```python
Customers.objects.all()
# SELECT * FROM customers

Customers.objects.filter(key=value)
# SELECT * FROM customers WHERE key = value

# notice that the result QuerySet is a set
# so we can do

Customers.objects.filter(key=value) & Customers.objects.filter(key1=value1)
```

#### forms:

we can let the model to be a subclass of form.Form in order to make it a form 
```python
from django import forms    

  

class ApplicationForm(forms.Form): 

    name = forms.CharField(label='Name of Applicant', max_length=50) 

    address = forms.CharField(label='Address', max_length=100) 

    posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator')) 

    field = forms.ChoiceField(choices=posts)
```
so that in the template we can directly use

```python
<form action="url" method="post">
	{{form}}
	<input type="submit" value="Submit">
</form>
```

we can also use the as_p, as_table to convert our form into a table or a paragraph

##### validation:

use form.is_valid() to check

and after validation, use cleaned_data to get the valid data

##### from modal:

```python
class LogForm(form.ModelForm):
	class Meta:
		model = Logger # imported
		fields = '__all__' # all the fields
		# note the model has to be registered
		
```
## request:

use request.GET request.POST to send a request to a certain server

use request.COOKIES to get the cookies

use request.FILES to get the files uploaded

use request.user to get the current user


## admin:

we can use `python3 manage.py createsuperuser` to create a superuser

also, we can register adminss as a custom class with 

create a modal, register it

```python
From django.contrib import admin. 

  

# Register your models here. 

from .models import Person 

@admin.register(Person) 

class PersonAdmin(admin.ModelAdmin): 

    list_display = ("last_name", "first_name") 

    search_fields = ("first_name__startswith", )
```

we can unregister a User with

```python
from django.contrib, import admin 

# Register your models here.  

from django.contrib.auth.models, import User 

# Unregister the provided model admin:  

admin.site.unregister(User)
```

## permissions:

- superuser: top-level user
- Staff user: can access django admin interface, dont automatically gain the access to read/write
- user: ordinary user

create superuser: python manage.py createsuperuser --username=something --email=something

we can enablle permission setting by `<app>.<actionmodel>`

- myapp.add_mymodal
- myapp.change_mymodal
- myapp.delete_mymodal
- myapp.view_mymodal

we can use user.has_perm("myapp.view_mymodal")

to check if a certain user has a certain type of permission

groups are list of permissions to one or more  users, you may have a group of chefs, and another group of waiters, etc.

we can register a permission of a certain class with

```python
class Product(models.Model): 

    ProductID: models.IntegerField() 

    name : models.TextField() 

    category : models.TextField 

    class Meta: 

        permissions = [('can_change_category', 'Can change category')]
```

and when sending a request, we can use the permission_required to check the permission, or mannually check it ourselves

```python
from django.contrib.auth.decorators import permission_required 

  

@permission_required("myapp.change_category") 

def store_creator(request): 

    # Logic for making change to category of product model instance
```

in the templates, we can also enforce permissions, we pass the use or perm into the template then check whatever is inside

or, in the urls

```python
from django.conf.urls import url 

from django.contrib.auth.decorators import login_required, permission_required 

  

urlpatterns = [ 

    url(r'^users_only/', login_required(myview)), 

  

    url(r'^category/', permission_required('myapp.change_category', login_url='login')(myview)), 

]
```

we can register a user with python manage.py shell

or in the code
```python
from django.contrib.auth.models import User
user = User.objects.create_user('name','email','password')
user_name = User.objects.get(username="name")
```
grant or remove permissions with 
```python
user.user_permissions.add("app.permission")
```

# database configurations

in settings.py

configure

```python
DATABASES = {
	'default': {
		'engine': 'django.db.backends.mysql',
		'NAME': 'feedback',
		'HOST': '127.0.0.1',
		'PORT': '3306',
		'USER': 'admin',
		'PASSWORD': 'password'
	}
}
```
as we usualy do to connec to a database