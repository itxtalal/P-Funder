from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# LOGIN REQUIRED MIXIN --- used in class of creating a post and updating a post
from django.contrib.auth.models import User
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
	)

from .models import Post


# Create your views here.

def landing(request):
	return render(request,'posts/landing.html')

def home(request):
	context = {
		'posts':Post.objects.all()
	}
	return render(request,'posts/home.html',context)






# Class based views are looked as <app>/<model>_<viewtype>.html
class PostListView(ListView):
	model = Post
	template_name = 'posts/home.html' 	# <app>/<model>_<viewtype>.html
# Class will by default call the variable of posts  'Objects post', but we called it 'posts'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 4 		




class UserPostListView(ListView):
	model = Post
	template_name = 'posts/user_posts.html' 	
	context_object_name = 'posts'
	paginate_by = 4 		

	def get_queryset(self):
		user = get_object_or_404(User, username = self.kwargs.get('username'))
		return Post.objects.filter(author = user).order_by("-date_posted")




class PostDetailView(DetailView):
	model = Post




class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title','brief','description','location','amount','mobileAccount','cNIC','bankAccount','phone','email']

	def form_valid(self,form):
		form.instance.author = self.request.user
# Author of the post will be the logged in user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title','brief','description','location','amount','mobileAccount','cNIC','bankAccount','phone','email']

	def form_valid(self,form):
		form.instance.author = self.request.user
# Author of the post will be the logged in user
		return super().form_valid(form)
# CHECK OF SOMEONE ELSE UPDATING SOMEONE ELSE POST
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False




class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False




def about(request):
	return render(request,'posts/about.html',{'title':'About'})
