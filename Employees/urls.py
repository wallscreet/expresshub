from django.urls import path
from .views import UserRegisterView, UserEditView

urlpatterns = [
    path('4040HIEnS/register/', UserRegisterView.as_view(), name='register'),
    path('4040HIEnS/edit_profile/', UserEditView.as_view(), name='edit_profile'),

]
