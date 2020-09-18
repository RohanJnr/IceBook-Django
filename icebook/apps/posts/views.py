from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PostForm


class AddPost(LoginRequiredMixin, View):
    template_name = "posts/add-post.html"

    def get(self, request: WSGIRequest) -> HttpResponse:
        post_form = PostForm()
        context = {"post_form": post_form}
        return render(request, self.template_name, context)

    def post(self, request: WSGIRequest) -> HttpResponse:
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            obj = post_form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("posts:list-posts")
        context = {"post_form": PostForm()}
        return render(request, self.template_name, context)


class ListPosts(LoginRequiredMixin, TemplateView):
    template_name = "posts/list-posts.html"


class DetailPost(LoginRequiredMixin, TemplateView):
    template_name = "posts/detail-post.html"
