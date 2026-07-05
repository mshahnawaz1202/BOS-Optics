from django.contrib import admin
from .models import Service, Appointment

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'price', 'duration')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'date', 'created_at')
    list_filter = ('service', 'date')
    search_fields = ('name', 'email', 'phone')
