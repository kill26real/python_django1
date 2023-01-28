from django.test import TestCase
from mysite.blogapp.views import create_post, PostsListView, PostDetailView, LoginErrorView, upload_post
from django.urls import reverse
from mysite.blogapp.models import BlogPost, Image


NUMDER_OF_POSTS = 5

class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(NUMDER_OF_POSTS):
            post = BlogPost.objects.create(text='blog text', user_id=0)
            Image.objects.create(post=post, img=f'{i}.jpg')
    def test_post_list(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogapp/posts-list.html')

    def test_numbers_posts(self):
        response = self.client.get(reverse('posts-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['BlogPost_list']) == 5)

class BlogPostCreateTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        post = BlogPost.objects.create(text='blog text', user_id=None)
        Image.objects.create(post=post, img='image.jpg')
    def post_list_exist_at_desired_location(self):
        response = self.client.get('/blog/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogapp/post_form.html')


class PostDetailsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        post = BlogPost.objects.create(text='blog text', user_id=0)
        Image.objects.create(post=post, img=f'{i}.jpg')
    def test_post_list(self, post):
        pk = post.pk
        response = self.client.get(f'/blog/{pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogapp/post_detail.html')


class BlogPostTest(TestCase):
    def test_post_list(self):
        response = self.client.get('/blog/login_error')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogapp/login-error.html')
