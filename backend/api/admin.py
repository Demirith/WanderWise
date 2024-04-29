from django.contrib import admin
from .models import Suggestion, Trip

class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('prompt', 'content', 'role', 'model_used', 'created_at')  # Customize to display these fields
    list_filter = ('role', 'model_used')  # Enable filtering by these fields
    search_fields = ('content', 'prompt')  # Enable search by these fields

admin.site.register(Suggestion, SuggestionAdmin)
admin.site.register(Trip)