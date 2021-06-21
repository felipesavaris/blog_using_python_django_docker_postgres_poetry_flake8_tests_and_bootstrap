from unittest import result
from django.http import response
from django.shortcuts import redirect
from django.test import TestCase

from .models import PostBlog


class TestViewsTemplatesModel(TestCase):

    def setUp(self):
        post = PostBlog.objects.create(
            title='titulo 1', descriptiom='texto do post')
        post.save()
        self.response_get = self.client.get('/blog/')

    # test routes
    def test_route_list_all_posts_returning_status_code_200(self):
        self.assertEqual(self.response_get.status_code, 200)
    
    def test_route_create_post(self):
        response = self.client.get('/blog/create')
        self.assertEqual(response.status_code, 200)

    def test_route_update_post(self):
        last_post = PostBlog.objects.last()
        response = self.client.post(f'/blog/update/{last_post.id}')
        self.assertEqual(response.status_code, 200)

    def test_route_delete_post(self):
        last_post = PostBlog.objects.last()
        response = self.client.post(f'/blog/delete/{last_post.id}')
        self.assertEqual(response.status_code, 302)

    # test route returning a expected response
    def test_route_list_all_returning_a_expected_response(self):
        self.assertEqual(
            self.response_get.context['posts'][0].title, 'titulo 1')
    
    # tests templates
    def test_route_list_all_posts_returning_a_valid_template(self):
        self.assertTemplateUsed(self.response_get, 'list_all_posts.html')

    def test_route_creatd_post_returning_a_valid_template(self):
        response = self.client.get('/blog/create')
        self.assertTemplateUsed(response, 'form.html')

    def test_route_update_post_returning_a_valid_templase(self):
        last_post = PostBlog.objects.last()
        response = self.client.get(f'/blog/update/{last_post.id}')
        self.assertTemplateUsed(response, 'form.html')

    def test_route_delete_post_returning_a_valid_template(self):
        last_post = PostBlog.objects.last()
        response = self.client.post(f'/blog/delete/{last_post.id}')
        self.assertTemplateNotUsed(response, None)
        self.assertRedirects(response, '/blog/')

    # test model postblog
    def test_model_postbog(self):
        new_post = PostBlog(title='title post', descriptiom='desc at post')
        assert isinstance(new_post, PostBlog)
        assert isinstance(new_post.title, str)
        assert isinstance(new_post.descriptiom, str)

        assert new_post.title == 'title post'
        assert 'at' in new_post.descriptiom
