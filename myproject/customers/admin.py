from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob')  # Los campos que se mostrarán en la lista de administración
    search_fields = ('first_name', 'last_name')  # Los campos por los cuales se podrá buscar
    list_filter = ('dob',)  # Campo para filtrar en la barra lateral

# Registre el modelo con la clase personalizada


admin.site.register(Customer, CustomerAdmin)
