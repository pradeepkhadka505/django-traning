
from django.urls import path
from . import views


urlpatterns = [

    path('', views.onfunctioncall, name="index"),
    path('about', views.about_function, name="about"),
    path('add/<int:a>/<int:b>', views.add, name="add"),
    path('intro/<str:name>/<int:age>', views.intro, name="intro")
]