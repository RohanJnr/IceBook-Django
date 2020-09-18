from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ["image", "description"]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["image"].widget.attrs.update({"id": "image_field"})
        self.fields["description"].widget.attrs.update({"id": "description_field"})
