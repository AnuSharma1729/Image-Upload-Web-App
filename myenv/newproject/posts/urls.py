from django.urls import paths

from .views import HomePageView, CreatePostView

urlpatterns = [path('',HomePageView.as_view(),name = 'home'),
path('post',CreatePostView.as_view(), name = 'add_post')]
