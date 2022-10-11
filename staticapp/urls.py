from django.urls import path
from .views import *

urlpatterns = [
    path('res/',response,name='response'),
    path('',home,name='home'),
]
