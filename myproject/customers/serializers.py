from datetime import date
from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'dob', 'id']
        extra_kwargs = {
            'dob': {
                'format': '%d-%m-%Y',
                'input_formats': ['%d-%m-%Y', ]
            },
        }

    def validate_dob(self, value):
        # Asegúrate de que la fecha de nacimiento no es en el futuro, por ejemplo
        if value > date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        return value



