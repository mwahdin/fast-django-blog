from django.urls import path
from website.views import HomeView, ContactUsView, AboutView, CommentCreateView, CommentUpdateView,PostViewFormView,ApplyDiscountView

app_name = "website"

urlpatterns = [
    path("", HomeView.as_view(), name="main_page"),
    path("contact_us/", ContactUsView.as_view(), name="contact_page"),
    path("about_us/", AboutView.as_view(), name="about_page"),
    path('comment/edit/<int:pk>/', CommentUpdateView.as_view(), name='comment_edit'),
    path('post/create/', PostViewFormView.as_view(), name='post'),
    path('/discount-code/', ApplyDiscountView.as_view(), name='discount'),

]