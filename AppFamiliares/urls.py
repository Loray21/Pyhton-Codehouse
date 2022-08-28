from django.urls import path
from AppFamiliares.views import *

urlpatterns = [
    path('', get_familiares),
]
