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
    path('Hire-full-stack-web-developer/', views.hireweb, name="hireweb"),
    path('Hire-Mobile-App-developer/', views.hireapp, name="hireapp"),
    path('Hire-Graphic-Designer/', views.hiredes, name="hiregd"),
    path('Hire-Social-Media-Manager/', views.hiresom, name="hiresm"),
    path('Job-Openings/', views.job, name="job"),
    path('Our-portfolio/', views.portfolio, name="portfolio"),
    path('Our-portfolio2/', views.portfolio2, name="portfolio2"),
    path('Our-portfolio3/', views.portfolio3, name="portfolio3"),
    path('Our-portfolio4/', views.portfolio4, name="portfolio4"),
    path('Our-portfolio5/', views.portfolio5, name="portfolio5"),
    path('Our-portfolio6/', views.portfolio6, name="portfolio6"),
    path('Case-study/', views.casestudy, name="casestudy"),
    path('Job_application', views.send_mail_plain_with_file, name="email"),
    path('Email_contact', views.contact_mail, name="contact_mail"),
    path('Web_design_request', views.contact_web, name="contact_web"),
    path('Mobile_app_request', views.contact_app, name="contact_app"),
    path('Graphic_design_request', views.contact_design, name="contact_design"),
    path('Social_Media_Manager_request', views.contact_media, name="contact_media"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)