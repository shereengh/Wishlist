from django.urls import path
from .views import UserCreateAPIView, ItemList, MyTokenObtainPairView


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('items/', ItemList.as_view(), name="item-list" ),
    
]