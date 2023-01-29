from django.test import TestCase
from mysite.blogapp.forms import BlogPostForm, UploadPostForm


class MyTests(TestCase):
    def test_BlogPostForm(self):
        form_data = {'img': '123.jpg', 'text': 'blog text'}
        form = BlogPostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_UploadPostForm(self):
        form_data = {'file': '123.jpg'}
        form = UploadPostForm(data=form_data)
        self.assertTrue(form.is_valid())
