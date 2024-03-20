from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"core/index.html")

def blogs(request):
    return render(request,"core/blogs.html")

def contact(request):
    return render(request,"core/contact.html")

def hire(request):
    return render(request,"core/hire.html")

def category(request):
    return render(request,"core/category.html")