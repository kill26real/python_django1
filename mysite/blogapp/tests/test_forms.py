from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from mysite.blogapp.forms import BlogPostForm, UploadPostForm


# class MyTests(TestCase):
#     def test_BlogPostForm(self):
#         image = SimpleUploadedFile("photo.jpg", "photo_content", content_type="image/gif")
#         form_data = {'img': image, 'text': 'blog text'}
#         form = BlogPostForm(data=form_data)
#         self.assertTrue(form.is_valid())
#
#     def test_UploadPostForm(self):
#         file = SimpleUploadedFile("posts.csv", "post_content", content_type="text/plain")
#         form_data = {'file': file}
#         form = UploadPostForm(data=form_data)
#         self.assertTrue(form.is_valid())
