from django.contrib.auth import get_user_model
from django.db.models import Count, Q
from blog.models import Post

User = get_user_model()

def top_authors_processor(request):
    top_author = User.objects.annotate(
        poblished_post_count = Count("blog_post", filter=Q(blog__Post__status=Post.Status.PUBLISHED))
        ).filter(poblished_post_count__gt=0).order_by('-poblished_post_count')
    
    return {'top_author': top_author}