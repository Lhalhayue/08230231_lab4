from django.contrib import admin
from .models import TimelineEvent, Profile
# Register your models here.


# TimelineEvent admin
@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ('year', 'title')           # Columns shown in admin list view
    list_filter = ('year',)                    # Filter sidebar by year
    search_fields = ('title', 'description')  # Search bar fields
    ordering = ('year',)                       # Default ordering

# Profile admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)                   # Only name shown in admin list
    search_fields = ('name', 'introduction', 'hobbies', 'strengths', 'weaknesses')
