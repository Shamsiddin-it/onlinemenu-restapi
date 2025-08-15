from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Dish URLs
    path('', RunMigrationsView.as_view(), name='run-migrations'),
    path('dishes/', DishListAPIView.as_view(), name='dish-list'),
    path('dishes/create/', DishCreateAPIView.as_view(), name='dish-create'),
    path('dishes/<int:pk>/', DishRetrieveUpdateAPIView.as_view(), name='dish-retrieve-update'),
    path('dishes/<int:pk>/delete/', DishDestroyAPIView.as_view(), name='dish-destroy'),
    
    # Table URLs
    path('tables/', TableListAPIView.as_view(), name='table-list'),
    path('tables/create/', TableCreateAPIView.as_view(), name='table-create'),
    path('tables/<int:pk>/', TableRetrieveUpdateAPIView.as_view(), name='table-retrieve-update'),
    path('tables/<int:pk>/delete/', TableDestroyAPIView.as_view(), name='table-destroy'),
    
    # Bill URLs
    path('bills/', BillListAPIView.as_view(), name='bill-list'),
    path('bills/create/', BillCreateAPIView.as_view(), name='bill-create'),
    path('bills/<int:pk>/', BillRetrieveUpdateAPIView.as_view(), name='bill-retrieve-update'),
    path('bills/<int:pk>/delete/', BillDestroyAPIView.as_view(), name='bill-destroy'),
    
    # Order URLs
    path('orders/', OrderListAPIView.as_view(), name='order-list'),
    path('orders/create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateAPIView.as_view(), name='order-retrieve-update'),
    path('orders/<int:pk>/delete/', OrderDestroyAPIView.as_view(), name='order-destroy'),
]
