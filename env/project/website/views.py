from email.message import EmailMessage
from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from project.settings import EMAIL_HOST_USER

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def faqs(request):
    return render(request, 'faq-page.html', {})

def contact(request):
    return render(request, 'contact-us.html', {})

def hireweb(request):
    return render(request, 'hireweb.html', {})


def hireapp(request):
    return render(request, 'hireapp.html', {})


def hiredes(request):
    return render(request, 'hiregd.html', {})

def hiresom(request):
    return render(request, 'hiresm.html', {})


def job(request):
    return render(request, 'job.html', {})

def portfolio(request):
    return render(request, 'portfolio.html', {})


def portfolio2(request):
    return render(request, 'portfolio2.html', {})


def portfolio3(request):
    return render(request, 'portfolio3.html', {})


def portfolio4(request):
    return render(request, 'portfolio4.html', {})


def portfolio5(request):
    return render(request, 'portfolio5.html', {})


def portfolio6(request):
    return render(request, 'portfolio6.html', {})


def casestudy(request):
    return render(request, 'casestudy.html', {})

def contact_mail(request):
    if request.method == "POST":
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        name = request.POST.get('name')
        email = request.POST.get('email')
        send_mail(name + ' reached out for business or inquiry with the subject:... '+ subject + ' ...and this is the used email address- '+ email, message, email,['georgemiriendichu@gmail.com'],)

        return render(request, 'contact-us.html',{'name':name})

    else: 
        return render(request, 'contact-us.html',{})

def contact_web(request):
    if request.method == "POST":
        message = request.POST.get('message')
        hire = request.POST.get('hire')
        name = request.POST.get('name')
        email = request.POST.get('email')
        send_mail(name + ' wants to hire a:... '+ hire + ' ...and this is the used email address- '+ email, message, email,['georgemiriendichu@gmail.com'],)

        return render(request, 'hireweb.html',{'name':name})

    else: 
        return render(request, 'hireweb.html',{})

def contact_app(request):
    if request.method == "POST":
        message = request.POST.get('message')
        hire = request.POST.get('hire')
        name = request.POST.get('name')
        email = request.POST.get('email')
        send_mail(name + ' wants to hire a:... '+ hire + ' ...and this is the used email address- '+ email, message, email,['georgemiriendichu@gmail.com'],)

        return render(request, 'hireapp.html',{'name':name})

    else: 
        return render(request, 'hireapp.html',{})


def contact_media(request):
    if request.method == "POST":
        message = request.POST.get('message')
        hire = request.POST.get('hire')
        name = request.POST.get('name')
        email = request.POST.get('email')
        send_mail(name + ' wants to hire a:... '+ hire + ' ...and this is the used email address- '+ email, message, email,['georgemiriendichu@gmail.com'],)

        return render(request, 'hiresm.html',{'name':name})

    else: 
        return render(request, 'hiresm.html',{})

def contact_design(request):
    if request.method == "POST":
        message = request.POST.get('message')
        hire = request.POST.get('hire')
        name = request.POST.get('name')
        email = request.POST.get('email')
        send_mail(name + ' wants to hire a:... '+ hire + ' ...and this is the used email address- '+ email, message, email,['georgemiriendichu@gmail.com'],)

        return render(request, 'hiregd.html',{'name':name})

    else: 
        return render(request, 'hiregd.html',{})

def send_mail_plain_with_file(request):
    if request.method == "POST":
        message = request.POST.get('message')
        hire = request.POST.get('hire')
        name = request.POST.get('name')
        email = request.POST.get('email')
        send_mail(name + 's Job application as a '+ hire + ' from user email '+ email, message, email,['georgemiriendichu@gmail.com'],)

        return render(request, 'job.html',{'name':name})

    else: 
        return render(request, 'job.html',{})
