from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages


# Create your views here.
class HomeView(TemplateView):
    template_name = "website/index.html"


class AboutView(TemplateView):
    template_name = "website/about.html"


class ContactUsView(FormView):
    form_class = ContactForm
    template_name = "website/contact.html"
    success_url = reverse_lazy("website:contact_page")

    def form_valid(self, form):

        fullName = form.cleaned_data["fullName"]
        email = form.cleaned_data["email"]
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]

        print(f"new message from: {fullName} ({email})")
        print(f"subject: {subject} | message: {message}")

        messages.success(self.request, "we got your message. i'll call back you")

        return super().form_valid(form)
