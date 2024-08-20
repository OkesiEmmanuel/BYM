from django.urls import path
from .views import member_form, success

urlpatterns = [
    path('', member_form, name='member_form'),
    path('success/', success, name='success'),
]
