from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
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
			return redirect("/posts")
	form = PostForm()
	template_name = "posts/add_post.html"
	context = {
		"form":form
	}
	return render(request, template_name, context)

@login_required
def display_posts_view(request):
	posts = Post.objects.annotate(num_comments=Count("comment"))
	liked = []
	like_no = []

	for post in posts:
		liked.append(check_like(request.user, post)[0])
		like_no.append(check_like(request.user, post)[1])

	template_name = "posts/display_posts.html"
	master_list = zip(posts, liked, like_no)
	context = {
		"master":master_list
	}
	return render(request, template_name, context)

@login_required
def detail_post_view(request, slug):
	post = Post.objects.get(slug=slug)
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

def check_like(user, post):
	likes = post.likes
	if user in likes.all():
		return True, len(likes.all())
	return False, len(likes.all())

def like_view(request, slug, destination):
	post = Post.objects.get(slug=slug)
	liked, like_no = check_like(request.user, post)
	if liked:
		post.likes.remove(request.user)
	else:
		post.likes.add(request.user)
	print(post.likes.all())
	post.save()
	if destination == "detail":
		return redirect("detail-post", slug=slug)
	else:
		return redirect("display-posts")