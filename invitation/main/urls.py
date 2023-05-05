from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('gallery/', gallery, name='gallery'),
    path('checking_form/', checking_form, name='checking_form'),
    path('send_mails/', send_mails, name='send_mails'),
    path('not_will_be/', not_will_be, name='not_will_be'),
]