from rest_framework.permissions import BasePermission

from .models import Item

class IsOwner(BasePermission):
	message = "This item does not belong to your list!"

	def has_permission(self, request, view):
		item = Item.objects.get(id=view.kwargs['item_id'])
		if item.user.id == request.user.id: 
			return True
		else:
			return False
