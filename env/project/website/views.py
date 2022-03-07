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

def send_mail_plain_with_file(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    name = request.POST.get('name', '')
    mail_id = request.POST.get('email', '')
    email=EmailMessage(subject,message,name,EMAIL_HOST_USER,[mail_id])
    email.content_subtype = 'html'

    file = request.FILES['file']
    email.attach(file.name, file.read(), file.content_type)

    email.send()
    return HttpResponse("Sent")