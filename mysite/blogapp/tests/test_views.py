from django.core.files.uploadedfile import SimpleUploadedFile
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
            image = SimpleUploadedFile("photo.jpg", "photo_content", content_type="image/gif")
            Image.objects.create(post=post, img=image)

    def test_post_list(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogapp/posts-list.html')

    def test_numbers_posts(self):
        response = self.client.get(reverse('posts-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['BlogPost_list']) == 5)


class BlogPostCreateTest(TestCase):
    def post_create_from_post_form(self):
        image = SimpleUploadedFile("photo.jpg", "photo_content", content_type="image/gif")
        data = {"img": image, 'text': 'post text'}
        response = self.client.post("blog/create/", data, content_type="multipart/form-data")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogapp/post_form.html')

    def post_create_from_upload_post_form(self):
        file = SimpleUploadedFile("posts.csv", "post_content", content_type="text/plain")
        response = self.client.post("blog/upload/", {'file': file})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogapp/upload-posts.html')


class PostDetailsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        post = BlogPost.objects.create(text='blog text', user_id=0)
        image = SimpleUploadedFile("photo.jpg", "photo_content", content_type="image/gif")
        Image.objects.create(post=post, img=image)

    def test_post_list(self, post):
        pk = post.pk
        response = self.client.get(f'/blog/{pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogapp/post_detail.html')


class BlogLoginErrorTest(TestCase):
    def test_post_list(self):
        response = self.client.get('/blog/login_error')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogapp/login-error.html')
