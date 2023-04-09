from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('send_mails/', send_mails, name='send_mails'),
    path('checking_form/', checking_form, name='checking_form'),
    path('check_form_name/', check_form_name, name='check_form_name'),
    path('check_form_email/', check_form_email, name='check_form_email'),
    path('check_form_address/', check_form_address, name='check_form_address'),
]