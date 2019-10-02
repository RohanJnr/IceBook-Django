from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Likes
from .forms import PostForm, CommentForm


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

@login_required
def display_posts_view(request):
	if request.method == "POST":

		request_list = list(request.POST.keys())
		data = request_list[1]
		status, slug = data.split(" ")
		post = Post.objects.get(slug=slug)

		if status == "notliked":
			like = Likes()
			like.user = request.user
			like.post = post
			like.save()

		elif status == "liked":
			like = Likes.objects.get(user=request.user)
			like.delete()

		return redirect("/")

	posts = list(Post.objects.all())
	status = []
	likes = []
	for post in posts:

		like_no = len(post.likes_set.all())
		likes.append(like_no)
		if list(post.likes_set.filter(user=request.user)):
			status.append(True)
		else:
			status.append(False)
	template_name = "posts/display_posts.html"
	master_list = zip(posts, status, likes)
	context = {
		"master_list":master_list
	}
	return render(request, template_name, context)

@login_required
def detail_post_view(request, slug):
	post = Post.objects.get(slug=slug)

	if request.method == "POST":
        
		request_list = list(request.POST.keys())
		status = str(request_list[1])
		if status == "notliked":
			like = Likes()
			like.user = request.user
			like.post = post
			like.save()

		elif status == "liked":
			like = Likes.objects.get(user=request.user)
			like.delete()

		return redirect(f"/posts/{slug}")

	likes = post.likes_set.all()
	like_no = len(likes)
	user_like = False

	if list(post.likes_set.filter(user=request.user)):
		user_like = True

	comments = post.comment_set.all()
	template_name = "posts/detail_post.html"

	context = {
		"post":post,
		"comments":comments,
		"like_no":like_no,
		"user_like":user_like
	}

	return render(request, template_name, context)

@login_required
def comments_view(request, slug):
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			post = Post.objects.get(slug=slug)
			obj.post = post
			obj.user = request.user
			obj.save()
			return redirect(f"/posts/{slug}")

	form = CommentForm()
	template_name = "posts/add_comment.html"
	context={
	"form":form
	}
	return render(request, template_name, context)
