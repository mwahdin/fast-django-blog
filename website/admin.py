from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_summary', 'is_approved', 'created_date', 'content_object')
    list_editable = ('is_approved',)
    list_filter = ('is_approved', 'created_date')
    search_fields = ('content', 'user__email')
    def content_summary(self, obj):
        if obj.content:
            return obj.content[:30] + '...' if len(obj.content) > 30 else obj.content
        return ""
    
    content_summary.short_description = 'خلاصه متن دیدگاه'