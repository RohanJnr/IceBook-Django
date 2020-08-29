from django.http import Http404


class NoLoginRequiredMixin():
	"""Denies to show a web page when user is logged-in."""
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			raise Http404("You cannot access this page as you are logged in.")
		return super().dispatch(request, *args, **kwargs)
