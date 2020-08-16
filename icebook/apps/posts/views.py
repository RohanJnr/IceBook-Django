from django.shortcuts import render, redirect
from django.views import View

from .forms import PostForm


class NewPost(View):
    """Create a new Post."""
    
    template_name = "posts/new-post.html"

    def get(self, request):
        """Display new post form."""
        post_form = PostForm()
        context = {
            "post_form": post_form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        """Validate form and save."""
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save(commit=False)
            post_form.user = request.user
            post_form.save()
            return redirect("posts:list-posts")
        
        return render(request, self.template_name, context)


