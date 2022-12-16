
from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
        path('', views.IndexView.as_view(), name='q_index'),
        path('<int:pk>/', views.DetailView.as_view(), name='q_info'),
        path('<int:pk>/count', views.ResultsView.as_view(), name='q_count'),
        path('<int:question_id>/vote', views.question_vote, name='q_vote'),
        ]
