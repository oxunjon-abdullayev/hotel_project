from django.urls import path

from app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('account/', account, name='account'),
    path('blog/', blog, name='blog'),
    path('blog_single/', blog_single, name='blog_single'),
    path('booking/', booking, name='booking'),
    path('contact/', contact, name='contact'),
    path('pricing/', pricing, name='pricing'),
    path('room_details/', room_details, name='room_details'),
    path('room_listing/', room_listing, name='room_listing'),
    path('service_details/', service_details, name='service_details'),
    path('service_single/', service_single, name='service_single'),
    path('services/', services, name='services'),
    path('team/', team, name='team'),
    path('team_single/', team_single, name='team_single'),
    path('header/', header, name='header'),
]