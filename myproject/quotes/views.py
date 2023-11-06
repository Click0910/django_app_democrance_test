from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Quote, Policy
from .serializers import QuoteSerializer
from .utils.calculate_quote import calculate_premium  # Assume you have this utility function
from django.shortcuts import get_object_or_404


class CreateQuoteAPIView(APIView):
    def post(self, request):
        # Assuming 'age' and 'policy_id' are provided in the request
        age = request.data.get('age')
        policy_id = request.data.get('policy_id')
        policy = get_object_or_404(Policy, id=policy_id)

        # Calculate the premium
        quoted_premium = calculate_premium(age, policy)

        # Create the quote
        quote = Quote.objects.create(
            customer=request.user,
            policy=policy,
            age_band=f"{age} age band",
            quoted_premium=quoted_premium
        )

        # Serialize the quote object
        serializer = QuoteSerializer(quote)

        return Response(serializer.data, status=201)
