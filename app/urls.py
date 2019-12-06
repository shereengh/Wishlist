from django.urls import path
from .views import UserCreateAPIView, ItemList, MyTokenObtainPairView, AddItem, DeleteItem


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('items/', ItemList.as_view(), name="item-list" ),
    path('items/add/', AddItem.as_view(), name= "item-add"),
    path('items/<int:item_id>/delete/',DeleteItem.as_view(), name="item-delete")
]