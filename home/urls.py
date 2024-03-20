from home import views
from django.urls import path

app_name="home"

urlpatterns=[
    path("",views.index,name="index"),
    path("blogs/",views.blogs,name="blogs"),
    path("contact/",views.contact,name="contact"),
    path("hire/",views.hire,name="hire"),
    path("category/",views.category,name="category"),
]
