from django.urls import path

from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView
	)

from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='posts-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='posts-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='posts-update'),
    path('post/new/', PostCreateView.as_view(), name='posts-create'), 	#THis NEEDS A TEMPLATE OF PATTERN (posts/post_form.html) 
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='posts-delete'),
    path('about/', views.about, name='posts-about')
]


# pk means PrimaryKey (ID) of post stored in Database


# We had a problem where any logged in user can edit or delete any post , 
# Solved by importing USERPASSESTESTMIXIN and creating a test_func()