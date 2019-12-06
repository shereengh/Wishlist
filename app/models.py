from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
	name = models.CharField(max_length=50)
	img = models.ImageField(blank=True, null=True)
	url= models.TextField()
	status = models.CharField(max_length=50)

	

	def __str__(self):
		return self.name