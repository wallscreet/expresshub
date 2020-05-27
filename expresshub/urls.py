from django.contrib import admin
from django.urls import path
from . import views
from .views import HomeView, post_detail, AddPostView, EditPostView, DraftView, authorview, UpcomingView, AddUpcomingView

urlpatterns = [
    # path('', views.home, name='home')
    path('', HomeView.as_view(), name='home'),
    path('post/<str:pk>/', post_detail, name='post_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('drafts/', DraftView.as_view(), name='drafts'),
    path('post/author/<str:author>/', authorview, name='author'),
    path('upcoming/', UpcomingView.as_view(), name='upcoming'),
    path('add_upcoming/', AddUpcomingView.as_view(), name='add_upcoming'),
]