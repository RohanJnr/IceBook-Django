import os

from django.dispatch import receiver, Signal


def delete_profile_pic(sender, instance, **kwargs):
	if instance.image:
		print(instance.image.name)
		if instance.image.name != "default.png":
			path = instance.image.path
			os.remove(path)
			print("Profile picture delete!")

profile_update_signal = Signal(providing_args=["old_img", "new_img"])

@receiver(profile_update_signal)
def profile_update_reciever(sender, **kwargs):
	new_img = kwargs['new_img']
	old_img = kwargs['old_img']
	print(old_img.name)
	print(new_img.name)
	print(type(old_img.name))
	if old_img.name != new_img.name:
		path = old_img.path
		os.remove(path)
		print("Deleted old profile image path.")
