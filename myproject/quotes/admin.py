# insurance/admin.py
from django.contrib import admin
from .models import Policy, PolicyStateHistory


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ['type', 'customer', 'premium', 'cover', 'state']
    # ...


@admin.register(PolicyStateHistory)
class PolicyStateHistoryAdmin(admin.ModelAdmin):
    list_display = ['policy', 'state', 'date_changed']
    # ...

# You should also register the Customer model if it's not already registered.
