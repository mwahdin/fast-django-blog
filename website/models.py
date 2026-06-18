from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False) 
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        if self.user.profile.first_name:
            return f"کامنت از طرف {self.user.profile.first_name} {self.user.profile.last_name}"
        return f"کامنت از طرف {self.user.email}"
    

class ArticleSuggestion(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(_("description"), max_length= 100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

