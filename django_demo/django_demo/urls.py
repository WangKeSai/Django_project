"""django_demo URL Configuration

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
from jobapp import views

urlpatterns = [
    path('', views.home),
    path('/favicon.ico/', views.home),
    path('admin/', admin.site.urls),
    path('regist/', views.regist),
    path('login/', views.login),
    path('logout/', views.logout),
    path('reset_pw/', views.reset_pw),
    path('home/', views.home),
    path('works/', views.work_list),
    path('person_info/', views.person_info),
    path('reset_info/', views.reset_info),
    path('reset_headimg/', views.reset_headimg),
    path('image_code/', views.image_code)
]
