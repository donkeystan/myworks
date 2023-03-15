"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes_app import views

# admin page: superuser
# username: admin
# password: a123456

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login),
    path('logout/', views.logout),
    path('notes/', views.notes),
    path('archived/', views.archived),
    path('archiving/<int:id>/', views.archiving),
    path('de_archiving/<int:id>/', views.de_archiving),
    path('edit/<int:id>/', views.edit),
    path('edit/<int:id>/<str:mode>/', views.edit),
    path('delete/<int:id>/', views.delete),
]
