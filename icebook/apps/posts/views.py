from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Post
from .forms import PostForm, CommentForm


@login_required
def add_post_view(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
			messages.success(request, "Post has been created.")
			return redirect("/posts")
	form = PostForm()
	template_name = "posts/add_post.html"
	context = {
		"form":form
	}
	return render(request, template_name, context)

@login_required
def display_posts_view(request):
	posts = Post.objects.get_posts(False)
	liked = []
	like_no = []

	for post in posts:
		liked.append(check_like(request.user, post)[0])
		like_no.append(check_like(request.user, post)[1])

	master_list = zip(posts, liked, like_no)
	context = {
		"master":master_list
	}
	
	template_name = "posts/display_posts.html"
	return render(request, template_name, context)

@login_required
def detail_post_view(request, pk):
	post = Post.objects.get(pk=pk)
	comments = post.comment_set.all()
	num_comments = len(comments)
	template_name = "posts/detail_post.html"
	liked, like_no = check_like(request.user, post)

	context = {
		"post":post,
		"comments":comments,
		"liked":liked,
		"like_no":like_no,
		"num_comments":num_comments
	}

	return render(request, template_name, context)

@login_required
def comments_view(request, pk):
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			post = Post.objects.get(pk=pk)
			obj.post = post
			obj.user = request.user
			obj.save()
			return redirect(f"/posts/{pk}")

	form = CommentForm()
	template_name = "posts/add_comment.html"
	context={
	"form":form
	}
	return render(request, template_name, context)

def check_like(user, post):
	likes = post.likes
	if user in likes.all():
		return True, len(likes.all())
	return False, len(likes.all())

def like_view(request, pk, destination):
	post = Post.objects.get(pk=pk)
	liked, like_no = check_like(request.user, post)
	if liked:
		post.likes.remove(request.user)
	else:
		post.likes.add(request.user)
	print(post.likes.all())
	post.save()
	print(request.POST)
	next_url = request.POST.get("next")
	return redirect(next_url)

@login_required
def delete_post_view(request, pk):
	obj = Post.objects.get(pk=pk)
	if request.method == "POST":
		obj.delete()
		messages.error(request, "Post has been deleted.")
		return redirect("profile")
	template_name = "posts/delete_post.html"
	context = {
		"post":obj
	}
	return render(request, template_name, context)

@login_required
def update_post_view(request, pk):
	obj = Post.objects.get(pk=pk)
	if request.method == "POST":
		post = PostForm(request.POST, request.FILES, instance=obj)
		if post.is_valid():
			post.save()
			messages.success(request, "Post has been updated.")
			return redirect("profile")

	form = PostForm(instance=obj)
	template_name = "posts/update-post.html"
	context = {
		"form":form
	}
	return render(request, template_name, context)

@login_required
def archive_post_view(request, pk):
	obj = Post.objects.get(pk=pk)
	obj.archived = True
	obj.save()
	return redirect("profile")

@login_required
def unarchive_post_view(request, pk):
	obj = Post.objects.get(pk=pk)
	obj.archived = False
	obj.save()
	return redirect("profile")
