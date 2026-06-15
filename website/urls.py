from django.urls import path
from website.views import HomeView, ContactUsView, AboutView

app_name = "website"

urlpatterns = [
    path("", HomeView.as_view(), name="main_page"),
    path("contact_us/", ContactUsView.as_view(), name="contact_page"),
    path("about_us/", AboutView.as_view(), name="about_page"),
]
