from datetime import datetime, timezone
from customers.models import Customer
from django.db import models
from django.conf import settings


# Se define un Choice Enum para el estado de la póliza
class PolicyState(models.TextChoices):
    NEW = 'new', 'New'
    QUOTED = 'quoted', 'Quoted'
    ACTIVE = 'active', 'Active'
    

class Policy(models.Model):
    type = models.CharField(max_length=100)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    cover = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(
        max_length=10,
        choices=PolicyState.choices,
        default=PolicyState.NEW,
    )
    is_accepted = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='policies')

    def change_state(self, new_state):
        self.state = new_state
        self.save()
        # Registrar el nuevo estado en el historial
        PolicyStateHistory.objects.create(policy=self, state=new_state)

    def __str__(self):
        return f"{self.type} - {self.state}"


class PolicyStateHistory(models.Model):
    policy = models.ForeignKey(Policy, related_name='state_history', on_delete=models.CASCADE)
    state = models.CharField(max_length=10, choices=PolicyState.choices)
    date_changed = models.DateTimeField(default=timezone)

    def __str__(self):
        return f"{self.policy.id} - {self.state} - {self.date_changed}"


class Quote(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    age_band = models.CharField(max_length=50)  # This could be a choice field or calculated field
    quoted_premium = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.customer}'s quote for {self.policy.type} - {self.age_band}"
