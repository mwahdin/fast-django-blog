from django.shortcuts import render
from django.views.generic import TemplateView, FormView, UpdateView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, redirect
from blog.models import Post
from .models import Comment, ArticleSuggestion
from .forms import CommentForm, suggestionForm


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


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        post_id = self.kwargs.get('post_id')
        post_obj = get_object_or_404(Post, id=post_id)
        form.instance.content_object = post_obj
        form.save()
        
        return redirect(post_obj.get_absolute_url())
    

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_edit.html'
    success_url = reverse_lazy('blog:post_list')
    
    def get_queryset(self):
        base_queryset = super().get_queryset()
        return base_queryset.filter(user=self.request.user)

    
class SuggestionCreateView(CreateView):
    model = ArticleSuggestion
    form_class = suggestionForm
    template_name = 'blog/suggestionArticle.html'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
