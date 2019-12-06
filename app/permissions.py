from rest_framework.permissions import BasePermission

from .models import Item

class IsOwner(BasePermission):
	message = "You must be a owner of list!"

	def has_permission(self, request, view):
		item = Item.objects.get(id=view.kwargs['user'])
		if item.filter(username=request.user): 
			return True
		else:
			return False
