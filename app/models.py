import uuid
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

class Item(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
	name = models.CharField(max_length=50)
	img = models.ImageField(blank=True, null=True)
	url= models.TextField()
	status = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	unique_id = models.UUIDField(default=uuid.uuid4, editable=False)

	def __str__(self):
		return str(self.unique_id)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)