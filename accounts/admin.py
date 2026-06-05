from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'پروفایل کاربر'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
   
    model = CustomUser
    
   
    list_display = ('email', 'is_staff', 'is_superuser', 'is_active', 'created_date')
    
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('دسترسی‌ها', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('تاریخ‌ها', {'fields': ('created_date', 'updated_date')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password'),
        }),
    )
    
    search_fields = ('email',)
    ordering = ('email',)
    readonly_fields = ('created_date', 'updated_date')

    inlines = (ProfileInline,)

admin.site.register(CustomUser, CustomUserAdmin)