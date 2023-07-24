from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import CustomUser, Group
from .forms import CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_author')


class CustomGroupAdmin(GroupAdmin):
    pass


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(Group)
