from django.urls import path
from .policy.views import AcceptPolicyAPIView, PolicyStateHistoryAPIView, ListPoliciesAPIView, PolicyDetailsAPIView, \
    PolicyHistoryAPIView
from .views import CreateQuoteAPIView


urlpatterns = [
    path('quotes', CreateQuoteAPIView.as_view(), name='create-quote'),
    path('quotes/<int:pk>/accept/', AcceptPolicyAPIView.as_view(), name='accept-quote'),
    path('quotes/<int:pk>/update', AcceptPolicyAPIView.as_view(), name='update-policy'),
    # path('<int:pk>/pay/', PayQuoteAPIView.as_view(), name='pay-quote'),
    path('policies/', ListPoliciesAPIView.as_view(), name='list-policies'),
    path('policies/<int:pk>/', PolicyDetailsAPIView.as_view(), name='policy-details'),
    path('policies/<int:pk>/history/', PolicyHistoryAPIView.as_view(), name='policy-history'),
]
