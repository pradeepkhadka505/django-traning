
from django.urls import path
from . import views


urlpatterns = [

    path('', views.onfunctioncall, name="index"),
    path('about', views.about_function, name="about"),
    path('add/<int:a>/<int:b>', views.add, name="add"),
    path('intro/<str:name>/<int:age>', views.intro, name="intro"),
    path('myfirstpage', views.myfirstpage, name="myfirstpage"),
    path('mysecondpage', views.mysecondpage, name="mysecondpage"),
    path('mythirdpage', views.mythirdpage, name="mythirdpage"),
    path('myimage', views.my_image, name="myimage"),
    path('myimage2', views.my_image2, name="myimage2"),
    path('myimage3', views.my_image3, name="myimage3"),
    path('myimage4', views.my_image4, name='myimage4'),
    path('myimage5/<str:imagename>', views.my_image5, name='myimage5')
    
]