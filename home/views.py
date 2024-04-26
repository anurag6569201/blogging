from django.shortcuts import render, get_object_or_404
from home.models import BlogModel,Subscriber
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from datetime import datetime
from home.forms import ContactForm,SubscriberForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives

@receiver(post_save, sender=BlogModel)
def send_newsletter_on_new_blog(sender, instance, created, **kwargs):
    if created:
        send_newsletter()

def index(request):
    blogs=BlogModel.objects.all().order_by('-creationDate')
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
    
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SubscriberForm()

    context={
        'blogs':blogs,
        "paginator":paginator,
        'newsletter':form,
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

def about(request):
    return render(request,"core/about.html")

def send_newsletter():
    subject = "New Blog Updates from Our Website"
    latest_blogs = BlogModel.objects.all().order_by('-creationDate')[:5]  # Get latest 5 blog posts
    context = {'latest_blogs': latest_blogs}

    html_content = render_to_string('core/newsletter_email.html', context)

    email = EmailMultiAlternatives(
        subject=subject,
        body="Check out our latest blog posts!",
        from_email='anurag6569201@gmail.com',
        to=Subscriber.objects.values_list('email', flat=True),
    )
    email.attach_alternative(html_content, "text/html")

    # Send email
    email.send()

    return redirect("home:index")

def privacy(request):
    return render(request,"core/privacy.html")


def advertise(request):
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
        
    return render(request,"core/advertise.html",context)