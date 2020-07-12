

from django.urls import path
from . import views

app_name = 'sa_account_app'

urlpatterns = [
    path('', views.profile, name='profile'),

]
