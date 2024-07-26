from django.contrib import admin

from .models import User, TransientHouseLocations, TransientHouse, Owner, RoomSpecifiction, Room, PensionHouse
from django.contrib.auth.admin import UserAdmin

admin.site.register(TransientHouse)
admin.site.register(TransientHouseLocations)
admin.site.register(Owner)
admin.site.register(RoomSpecifiction)
admin.site.register(Room)
admin.site.register(PensionHouse)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name','last_name', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    list_display = ('username', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('username',)

