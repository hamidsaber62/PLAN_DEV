#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~<START>    With God's help     </START>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.urls import path
from . import views

app_name = 'sa_plan_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('plan/', views.plan, name='plan'),
    path('<str:plan_slug>-<int:plan_id>/', views.plan_description, name='plan-description'),
    # plan-description
    path('-<str:proctor_slug>-/', views.proctor_description, name='proctor-description'),
    # proctor_description
    path('<str:project_slug>--/', views.project, name='project'),
    path('--<str:card_slug>/', views.more_info, name='more-info'),
    path('change-seen-status/', views.change_seen_status, name='change-seen-status'),

    # path('user_register/', views.user_register, name='user_register'),
    # path('user_login/', views.user_login, name='user_login'),
    # path('admin/', views.admin, name='admin'),
    # path('homes/', views.IndexView.as_view()),
]
