

from django.urls import path
from . import views

app_name = 'sa_plan_app'

urlpatterns = [
    path('', views.index, name='index'),
    # path('proctor/', views.proctor, name='proctor'),
    path('proctors/', views.proctors, name='proctors'),
    path('plan/', views.plan, name='plan'),
    path('plan_description/<int:pid>', views.plan_description, name='plan_description'),
    # path('project_description/<int:pid>', views.project_description, name='project_description'),
    path('proctor_description/<int:pid>', views.proctor_description, name='proctor_description'),
    path('project/', views.project, name='project'),

    # path('user_register/', views.user_register, name='user_register'),
    # path('user_login/', views.user_login, name='user_login'),
    # path('admin/', views.admin, name='admin'),
    # path('homes/', views.IndexView.as_view()),
]
