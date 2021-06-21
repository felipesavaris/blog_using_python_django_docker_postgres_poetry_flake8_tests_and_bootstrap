from django import forms

from .models import PostBlog


class PostBlogForms(forms.ModelForm):

    class Meta:
        model = PostBlog
        fields = '__all__'
