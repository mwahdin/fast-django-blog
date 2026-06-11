from django.contrib.auth import get_user_model
from django.db.models import Count, Q, Sum
from blog.models import Post,Category
from django.shortcuts import get_object_or_404

User = get_user_model()

def top_authors_processor(request):
    top_author = User.objects.annotate(
        published_post_count=Count('posts', filter=Q(posts__status=Post.Status.PUBLISHED))
    ).filter(published_post_count__gt=0).order_by('-published_post_count')[:5]
    
    return {'top_author': top_author}

# def category_list_footer(request):
#     category = Category.objects.annotate(category_list = Count('post_set', filter=Q(post_set__status=Post.Status.PUBLISHED))).filter(category__gt=0).order_by('name')
#     return {'category':category}

# def sum_user_post_views(request, username):
#     author_obj = get_object_or_404(User, username=username)
#     author_post = Post.objects.filter(author=author_obj, status=Post.Status.PUBLISHED).aggregate(sum_all_post_views=Sum('views_count'))

# def top_author(request):
#     top_author1 = User.objects.annotate(post_count = Count('blog_post', filter=Q(blog_post__status=Post.Status.PUBLISHED))).
