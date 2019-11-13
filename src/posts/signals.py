import os


def delete_pic(sender, instance, **kwargs):
	if instance.img:
		pic_path = instance.img.path
		os.remove(pic_path)
		print("Image deleted!")
