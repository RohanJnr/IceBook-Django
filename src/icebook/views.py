from django.shortcuts import render


def home_page(request):
	template_name = "home.html"
	context = {}
	return render(request, template_name, context)
