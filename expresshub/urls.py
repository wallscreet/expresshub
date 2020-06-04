from django.contrib import admin
from django.urls import path
from . import views
from .views import HomeView, post_detail, AddPostView, EditPostView, DraftView, authorview, UpcomingView, AddUpcomingView, postm_detail, posth_detail, AddPostMView, AddPostHView, EditPostHView, EditPostMView, MaintenanceView, HousekeepingView, authorhview, authormview, lostfound_detail, LostFoundView, AddLostFoundView, EditLostFoundView, FoundView, creatorview

urlpatterns = [
    # path('', views.home, name='home')
    path('', HomeView.as_view(), name='home'),
    path('maintenance/', MaintenanceView.as_view(), name='maintenance'),
    path('housekeeping/', HousekeepingView.as_view(), name='housekeeping'),
    path('lostfound/', LostFoundView.as_view(), name='lostfound'),\
    path('found/', FoundView.as_view(), name='found'),
    path('post/<str:pk>/', post_detail, name='post_detail'),
    path('lostfound/<str:pk>/', lostfound_detail, name='lostfound_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('add_lostfound/', AddLostFoundView.as_view(), name='add_lostfound'),
    path('lostfound/edit/<int:pk>', EditLostFoundView.as_view(), name='edit_lostfound'),
    path('drafts/', DraftView.as_view(), name='drafts'),
    path('post/author/<str:author>/', authorview, name='author'),
    path('authorm/<str:authorm>/', authormview, name='authorm'),
    path('authorh/<str:authorh>/', authorhview, name='authorh'),
    path('creator/<str:creator>/', creatorview, name='creator'),
    path('upcoming/', UpcomingView.as_view(), name='upcoming'),
    path('add_upcoming/', AddUpcomingView.as_view(), name='add_upcoming'),
    path('postm/<str:pk>/', postm_detail, name='postm_detail'),
    path('add_postm/', AddPostMView.as_view(), name='add_postm'),
    path('postm/edit/<int:pk>', EditPostMView.as_view(), name='edit_postm'),
    path('posth/<str:pk>/', posth_detail, name='posth_detail'),
    path('add_posth/', AddPostHView.as_view(), name='add_posth'),
    path('posth/edit/<int:pk>', EditPostHView.as_view(), name='edit_posth'),
]