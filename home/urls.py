from home import views
from django.urls import path

app_name="home"

urlpatterns=[
    path("",views.index,name="index"),
    path("contact/",views.contact,name="contact"),
    path("about/",views.about,name="about"),
    path("advertise/",views.advertise,name="advertise"),
    path("privacy/",views.privacy,name="privacy"),
    path("read/<int:blog_id>/", views.blog, name="blog"),
]
