from django.urls import path
from .views import (
	UserCreateAPIView, MyList, MyTokenObtainPairView, 
	AddItem, DeleteItem, ItemsList)


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),

    path('items/', MyList.as_view(), name="my-items-list" ),
    path('items/<str:unique_id>/', ItemsList.as_view(), name="items-list" ),

    path('add/', AddItem.as_view(), name= "item-add"),
    path('items/<int:item_id>/delete/',DeleteItem.as_view(), name="item-delete"),

]