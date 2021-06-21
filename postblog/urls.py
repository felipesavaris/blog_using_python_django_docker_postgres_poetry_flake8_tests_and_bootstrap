from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_all_posts, name='list_all_posts'),
    path('update/<int:id>', views.update_post, name='update_post'),
    path('delete/<int:id>', views.delete_post, name='delete_post'),
]
