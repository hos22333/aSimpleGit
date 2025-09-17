from django.contrib import admin
from .models import Page1Log, UserPagePermission

@admin.register(Page1Log)
class Page1LogAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'result')
    list_filter = ('timestamp', 'user')
    search_fields = ('user__username',)

@admin.register(UserPagePermission)
class UserPagePermissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'can_access_page1', 'can_access_page2', 'can_access_page3')
    list_filter = ('can_access_page1', 'can_access_page2', 'can_access_page3')
    search_fields = ('user__username',)