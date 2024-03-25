from django.shortcuts import render, get_object_or_404
from .models import BlogModel
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from datetime import datetime
from home.forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import redirect

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

def contact(request):
    today_date = datetime.now().strftime('%Y-%m-%d')
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            content = form.cleaned_data['content']

            html = render_to_string('core/email.html', {
                'name': name,
                'email': email,
                'phone': phone,
                'content': content,
            })

            send_mail("The contact form subject", 'this is the message', email, ['anurag6569201@gmail.com'], html_message=html)
            return redirect("home:index")
    else:
        form = ContactForm()

    context={
        'today_date': today_date,
        'form': form,
    }
    return render(request,"core/contact.html",context)