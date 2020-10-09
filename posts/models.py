from django.db import models
from phone_field import PhoneField
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=100)
	location = models.CharField(max_length=35,help_text='Kindly atleast mention City,Country')
	brief = models.TextField(max_length=500, help_text='Write an overview to be displayed on Homepage')
	description= models.TextField(help_text='Please Mention your Jazzcash or EasyPaisa account (If Any)')

	amount = models.DecimalField( max_digits = 10 ,decimal_places=2, help_text='Enter the amount in US Dollars $') 

# For Transactions
	mobileAccount = models.CharField(max_length=15,blank=True,null=True,help_text='Enter your Jazzcash or EasyPaisa Account</br>This is for Jazzcash or EasyPaisa money transfer')
	cNIC= models.CharField(max_length = 13,blank=True,null=True,help_text='This is for Jazzcash / EasyPaisa money transfer')
	bankAccount = models.CharField(max_length = 26,help_text='This is for Jazzcash / EasyPaisa / Bank money transfer' ,blank=True,null=True)
	
	
	email = models.EmailField( help_text='Enter the email so that someone can contact you in case of any help ')
	phone = PhoneField(blank=True,null=True, help_text = '+[country code][number]x[extension]')

	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('posts-detail', kwargs={'pk':self.pk})
		# IT IS FOR THE REDIRECTING TO DETAILED VIEW OF POST JUST CREATED

