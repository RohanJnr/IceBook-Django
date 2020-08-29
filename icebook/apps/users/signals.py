import os

from PIL import Image

def resize_profile_pic(sender, instance, **kwargs):
    """Resize profile picture when a profile instance is saved."""
    profile_pic = instance.profile_picture
    if profile_pic.name != "default.png":
        img = Image.open(profile_pic.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(profile_pic.path)


def delete_profile_pic(sender, instance, **kwargs):
    """Delete profile pic when User/Profile is deleted."""
    if instance.profile_picture:
        if instance.profile_picture.name != "default.png":
            path = instance.profile_picture.path
            os.remove(path)
