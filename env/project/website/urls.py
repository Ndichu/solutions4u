from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('About-us/', views.about, name="about"),
    path('FAQs/', views.faqs, name="faqs"),
    path('Contact-Us/', views.contact, name="contact"),
    path('Job-Openings/', views.job, name="job"),
    path('Our-portfolio/', views.portfolio, name="portfolio"),
    path('Case-study/', views.casestudy, name="casestudy"),
]