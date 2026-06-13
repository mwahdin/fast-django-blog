from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
import math

User = get_user_model()

class Tag(models.Model):
    title = models.CharField(_("tag title"), max_length=50)
    slug = models.SlugField(_("tag_slug"))

    class meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
    
    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(_("name"), max_length=200, unique=True)
    content = models.TextField(_('content'))
    image = models.ImageField(_('image'), null=True, blank=True, upload_to='category_images/')
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
    slug = models.SlugField(_('slug'), max_length=255, unique=True, allow_unicode=True)
    content = models.TextField(_('content'))
    snippet = models.CharField(_('snippet'), max_length=400, blank=True)
    category = models.ManyToManyField('Category', blank=True, related_name='posts', verbose_name=_('category'))
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts', verbose_name=_('tags'))
    publish_date = models.DateTimeField(_('publish date'), blank=True, null=True)
    views_count = models.PositiveIntegerField(_('views count'), default=0)
    created_date = models.DateTimeField(_('created date'), auto_now_add=True)
    updated_date = models.DateTimeField(_('updated date'), auto_now=True)
    

    @property
    def read_time(self):
        if not self.content:
            return 0
        word_count = len(self.content.split())
        minutes = math.ceil(word_count / 200)
        return minutes
    
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ['-publish_date'] 

    def __str__(self):
        return self.title