from django.db import models
# from ckeditor.fields import RichTextField


class PostBlog(models.Model):

    title = models.CharField(max_length=60)
    # description = RichTextField()
    descriptiom = models.TextField()  # blank=True
