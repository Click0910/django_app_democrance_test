from django.urls import path
from .views import CreateCustomerAPIView, CustomerSearchAPIView

urlpatterns = [
    path('create_customer/', CreateCustomerAPIView.as_view(), name='create_customer'),
    path('search/', CustomerSearchAPIView.as_view(), name='customer-search'),
]
