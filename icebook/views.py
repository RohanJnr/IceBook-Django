from django.shortcuts import render


def home_page(request):
	template_name = "home.html"
	context = {}
	return render(request, template_name, context)

def about_page(request):
	template_name = "about.html"
	context = {}
	return render(request, template_name, context)
