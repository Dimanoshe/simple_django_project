from django.contrib import admin

from .models import Lead, LeadState


@admin.register(Lead)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state')

@admin.register(LeadState)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
    

