from django.urls import path
from . views import *


urlpatterns=[
    path('register/',register_user),
    path('login/',postlogin),
    path('logout/',logout_user)
]