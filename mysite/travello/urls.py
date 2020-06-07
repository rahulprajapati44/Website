from django.urls import path

from . import views

urlpatterns = [
    #path('',views.home, name="home"), # for home page url we have function name "home" in views
    path('',views.index, name="index"), # here first argument is action name recived from html, and name argument is home function

]