from django.shortcuts import render, get_object_or_404
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

def blog(request, blog_id):
    blogs = get_object_or_404(BlogModel, id=blog_id)
    context={
        'blog':blogs,
    }
    return render(request,"core/blog.html",context)