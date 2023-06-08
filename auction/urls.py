from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("podd/", podderjka, name="podd"),
    path("cat/<int:cat>", category, name="cat"),
    path("about/", about, name="about"),

]
