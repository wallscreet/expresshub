from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path('4040HIEnS/register/', UserRegisterView.as_view(), name='register'),

]
