from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf.urls.static import static
from project import settings
urlpatterns = [
    path('', views.home, name="home"),
    path('About-us/', views.about, name="about"),
    path('FAQs/', views.faqs, name="faqs"),
    path('Contact-Us/', views.contact, name="contact"),
    path('Job-Openings/', views.job, name="job"),
    path('Our-portfolio/', views.portfolio, name="portfolio"),
    path('Our-portfolio2/', views.portfolio2, name="portfolio2"),
    path('Our-portfolio3/', views.portfolio3, name="portfolio3"),
    path('Our-portfolio4/', views.portfolio4, name="portfolio4"),
    path('Our-portfolio5/', views.portfolio5, name="portfolio5"),
    path('Our-portfolio6/', views.portfolio6, name="portfolio6"),
    path('Case-study/', views.casestudy, name="casestudy"),
    path('send_mail_plain_with_file', views.send_mail_plain_with_file, name="email"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)