# from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from postblog.views import PostBlogViewSet


route = routers.DefaultRouter()
route.register(r'postblog', PostBlogViewSet, basename='PostBlog') 

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('appbase.urls')),
    path('', include(route.urls)),
]
