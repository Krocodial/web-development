To initialize a Django project do the following  
  
create a new directory for the project  
run the command "django-admin startproject projectname"

run the website with
	"python3 manage.py runserver (optional)ipaddress:port"

create the catalog application  
	"python3 manage.py startapp catalog"  


Whenever the web application is changed in any significant way you should run a migration to ensure everything still works
	"python3 manage.py makemigrations"
	"python3 manage.py migrate"

