from django.urls import path
from . import views

urlpatterns = [
    path("hello", view=views.say_hello, name="SayHello"),
    path("add/<int:num1>/<int:num2>", view=views.add, name="Add")
]