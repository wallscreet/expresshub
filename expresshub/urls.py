from django.contrib import admin
from django.urls import path
from . import views
from .views import HomeView, post_detail, AddPostView, EditPostView, DraftView, authorview, UpcomingView, AddUpcomingView, postm_detail, posth_detail, AddPostMView, AddPostHView, EditPostHView, EditPostMView, MaintenanceView, HousekeepingView, authorhview, authormview

urlpatterns = [
    # path('', views.home, name='home')
    path('', HomeView.as_view(), name='home'),
    path('maintenance/', MaintenanceView.as_view(), name='maintenance'),
    path('housekeeping/', HousekeepingView.as_view(), name='housekeeping'),
    path('post/<str:pk>/', post_detail, name='post_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('drafts/', DraftView.as_view(), name='drafts'),
    path('post/author/<str:author>/', authorview, name='author'),
    path('authorm/<str:authorm>/', authormview, name='authorm'),
    path('authorh/<str:authorh>/', authorhview, name='authorh'),
    path('upcoming/', UpcomingView.as_view(), name='upcoming'),
    path('add_upcoming/', AddUpcomingView.as_view(), name='add_upcoming'),
    path('postm/<str:pk>/', postm_detail, name='postm_detail'),
    path('add_postm/', AddPostMView.as_view(), name='add_postm'),
    path('postm/edit/<int:pk>', EditPostMView.as_view(), name='edit_postm'),
    path('posth/<str:pk>/', posth_detail, name='posth_detail'),
    path('add_posth/', AddPostHView.as_view(), name='add_posth'),
    path('posth/edit/<int:pk>', EditPostHView.as_view(), name='edit_posth'),
]