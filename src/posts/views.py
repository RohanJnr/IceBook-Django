from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


@login_required
def add_post_view(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
	form = PostForm()
	template_name = "posts/add_post.html"
	context = {
		"form":form
	}
	return render(request, template_name, context)

def display_posts_view(request):
	posts = Post.objects.all()
	template_name = "posts/display_posts.html"
	context = {
		"posts":posts
	}
	return render(request, template_name, context)

def detail_post_view(request, slug):
	post = Post.objects.get(slug=slug)
	template_name = "posts/detail_post.html"
	context = {
		"post":post
	}
	return render(request, template_name, context)
