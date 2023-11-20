from django.urls import path
from app.views import *

urlpatterns = [
    path('forloop/',forloop,name='forloop')
]
