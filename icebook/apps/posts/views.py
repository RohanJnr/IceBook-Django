from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class AddPost(LoginRequiredMixin, TemplateView):
    template_name = "posts/add-post.html"


class ListPosts(LoginRequiredMixin, TemplateView):
    template_name = "posts/list-posts.html"