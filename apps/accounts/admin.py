from django.contrib import admin

from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserManagerAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
    )
    search_fields = (
        'email',
        'username',
        'first_name',
        'last_name',
    )
    ordering = (
        'email',
    )
    exclude = (
        'password',
    )
