from django import forms
from .models import BlogPost, Image


class BlogPostForm(forms.Form):
    img = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 8, 'cols': '30'}))



# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ('text',)


class UploadPostForm(forms.Form):
    file = forms.FileField()


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('img',)
        img = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
