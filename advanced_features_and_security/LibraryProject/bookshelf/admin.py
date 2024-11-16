from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  
    search_fields = ('title', 'author')  
    list_filter = ('publication_year',)  





# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'profile_photo', 'is_staff']
    list_filter = ['is_staff', 'is_superuser', 'date_of_birth']
    search_fields = ['username', 'email']
    ordering = ['username']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)





from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from .models import Article

# Create a function to set up default groups and permissions
def setup_groups_and_permissions():
    # Get all permissions for the Article model
    permissions = Permission.objects.filter(codename__in=['can_view', 'can_create', 'can_edit', 'can_delete'])

    # Create Viewers group
    viewers_group, created = Group.objects.get_or_create(name="Viewers")
    viewers_group.permissions.set([permissions.get(codename="can_view")])

    # Create Editors group
    editors_group, created = Group.objects.get_or_create(name="Editors")
    editors_group.permissions.set([permissions.get(codename="can_create"),
                                   permissions.get(codename="can_edit"),
                                   permissions.get(codename="can_view")])

    # Create Admins group
    admins_group, created = Group.objects.get_or_create(name="Admins")
    admins_group.permissions.set([permissions.get(codename="can_create"),
                                  permissions.get(codename="can_edit"),
                                  permissions.get(codename="can_view"),
                                  permissions.get(codename="can_delete")])

admin.site.register(Article)

