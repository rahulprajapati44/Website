from django.urls import path

from mysite.calc import views

urlpatterns = [
    path('',views.home, name="home"), # for home page url we have function name "home" in views
    path('homepage',views.home, name="home"), # here first argument is action name recived from html, and name argument is home function
    path('addition',views.add, name = "add"),
    path("multiplication",views.mul, name="mul")
]