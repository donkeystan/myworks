"""
hf_uniform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from hf_uniform_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/<str:inputString>/', views.list_perm ),

    path('', views.index),
    
    path('login/', views.login),
    path('logout/', views.logout),

    path('main/', views.main),
    path('query/', views.query),
    path('detail/<int:uniform_id>/', views.detail),

    path('single_input/', views.single_input),
    path('multi_input/<str:orgnization_name>/', views.multi_input),

    path('edit_from_detail/<int:uniform_id>/', views.edit_from_detail),
    path('edit_from_detail/<int:uniform_id>/<str:mode>/', views.edit_from_detail),
    path('edit_from_multi_input/<int:uniform_id>/', views.edit_from_multi_input),
    path('edit_from_multi_input/<int:uniform_id>/<str:mode>/', views.edit_from_multi_input),

    path('delete_return_multi_input/<int:uniform_id>/', views.delete_return_multi_input),
    path('delete_return_query/<int:uniform_id>/', views.delete_return_query),
    path('delete_in_multi_input/<int:uniform_id>/', views.delete_in_multi_input),
    path('delete_in_query/<int:uniform_id>/', views.delete_in_query),
]
