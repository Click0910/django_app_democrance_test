from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Policy, PolicyStateHistory
from ..serializers import PolicyStateHistorySerializer, PolicySerializer


class ListPoliciesAPIView(APIView):
    def get(self, request, *args, **kwargs):
        customer_id = request.query_params.get('customer_id')
        if customer_id is not None:
            policies = Policy.objects.filter(customer_id=customer_id)
        else:
            policies = Policy.objects.all()
        serializer = PolicySerializer(policies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Policy Details
class PolicyDetailsAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            policy = Policy.objects.get(pk=pk)
        except Policy.DoesNotExist:
            return Response({'error': 'Policy not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PolicySerializer(policy)
        return Response(serializer.data)


# Policy History
class PolicyHistorySerializer:
    pass


class PolicyHistoryAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            policy_history = PolicyStateHistory.objects.filter(policy_id=pk)
        except PolicyStateHistory.DoesNotExist:
            return Response({'error': 'Policy history not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PolicyHistorySerializer(policy_history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AcceptPolicyAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PolicySerializer(data=request.data)
        if serializer.is_valid():
            policy = serializer.save()
            return Response(PolicySerializer(policy).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        policy = Policy.objects.get(pk=pk)
        serializer = PolicySerializer(policy, data=request.data)
        if serializer.is_valid():
            policy = serializer.save()
            return Response(PolicySerializer(policy).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PolicyStateHistoryAPIView(APIView):
    def get(self, request, pk):
        policy = Policy.objects.get(pk=pk)
        history = PolicyStateHistory.objects.filter(policy=policy).order_by('-date_changed')
        serializer = PolicyStateHistorySerializer(history, many=True)
        return Response(serializer.data)
