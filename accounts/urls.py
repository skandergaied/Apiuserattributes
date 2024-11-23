from django.urls import path
from .views import UserRegistrationView
from .views import TaskViewSet


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('task/', TaskViewSet.as_view(),  name='task_list'),
]
