from rest_framework import serializers
from .models import Policy
from .models import Quote
from .models import PolicyStateHistory


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['customer', 'policy', 'age_band', 'quoted_premium', 'id']


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'

    def validate_dob(self, value):
        # Handle date formatting validation if necessary
        return value


class PolicyStateHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyStateHistory
        fields = ['state', 'date_changed']
