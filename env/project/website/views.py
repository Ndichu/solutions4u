from django.shortcuts import render

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

def casestudy(request):
    return render(request, 'casestudy.html', {})
