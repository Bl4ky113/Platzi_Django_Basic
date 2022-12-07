
from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
        path('', views.index, name='index'),
        path('<int:question_id>/', views.question_info, name='info'),
        path('<int:question_id>/count', views.question_count, name='count'),
        path('<int:question_id>/vote', views.question_vote, name='vote'),
        ]
