from home import views
from django.urls import path

app_name="home"

urlpatterns=[
    path("",views.index,name="index"),
    path("read/<int:blog_id>/", views.blog, name="blog"),
]
