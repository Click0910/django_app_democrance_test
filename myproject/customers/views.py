from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Customer
from .serializers import CustomerSerializer


class CreateCustomerAPIView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerSearchAPIView(APIView):
    def get(self, request):
        queryset = Customer.objects.all()
        name = request.query_params.get('name')
        dob = request.query_params.get('dob')
        policy_type = request.query_params.get('policy_type')

        if name:
            queryset = queryset.filter(name__icontains=name)
        if dob:
            queryset = queryset.filter(dob=dob)
        if policy_type:
            queryset = queryset.filter(policies__type__icontains=policy_type)

        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)
