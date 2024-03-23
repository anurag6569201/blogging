from django.shortcuts import render
from .models import BlogModel
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def index(request):
    blogs=BlogModel.objects.all()
    page=request.GET.get('page')
    num_of_items=7
    paginator=Paginator(blogs,num_of_items)

    try:
        blogs=paginator.page(page)
    except PageNotAnInteger:
        page=1
        blogs=paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        blogs=paginator.page(page)
    context={
        'blogs':blogs,
        "paginator":paginator,
    }
    return render(request,"core/index.html",context)

def blogs(request):
    return render(request,"core/blogs.html")

def contact(request):
    return render(request,"core/contact.html")

def hire(request):
    return render(request,"core/hire.html")

def category(request):
    return render(request,"core/category.html")