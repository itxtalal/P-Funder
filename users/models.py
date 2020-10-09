from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	image = models.ImageField(default='default.png' , upload_to = 'profile_pics')


	def __str__(self):
		return f'{self.user.username} Profile'


# OVER RIDING SAVE METHOD , CREATING OUR OWN TO ADD SOME FUNCTIONALITY.
	def save(self,*args, **kwargs):
		# RUNNING SAVE METHOD OF OUR PARENT CLASS
		super().save()

		# GRABBING THE IMAGE SAVED AND RESIZING IT
		img = Image.open(self.image.path) 	 #OPENING IMAGE OF CURRENT INSTANCE

		if img.height>300 or img.width>300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)


