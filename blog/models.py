from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Category(models.Model):
    name = models.CharField(_("name"), max_length=200, unique=True)
    slug = models.SlugField(_('slug'), max_length=200, unique=True)
    
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name
    

class Post(models.Model):
    """
    Docstring for Post:
    this model creates posts for the blog.
    """
    class Status(models.TextChoices):
        DRAFT = 'DF', _('Draft')
        PUBLISHED = 'PB', _('Published')

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='blog_posts', verbose_name=_('author'))
    status = models.CharField(_('status'), max_length=2, choices=Status.choices, default=Status.DRAFT)
    image = models.ImageField(_('image'), null=True, blank=True, upload_to='post_images/')
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255, unique=True)
    content = models.TextField(_('content'))
    snippet = models.CharField(_('snippet'), max_length=400, blank=True)
    category = models.ManyToManyField('Category', null=True, related_name='posts', verbose_name=_('category'))
    
    publish_date = models.DateTimeField(_('publish date'), blank=True, null=True)
    
    views_count = models.PositiveIntegerField(_('views count'), default=0)
    
    created_date = models.DateTimeField(_('created date'), auto_now_add=True)
    updated_date = models.DateTimeField(_('updated date'), auto_now=True)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ['-publish_date'] 

    def __str__(self):
        return self.title