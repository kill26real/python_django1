from django import forms
from .models import Article, Tag


class ArticleForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple(),
                                            required=True)
    class Meta:
        model = Article
        fields = 'title', 'content', 'author', 'category', 'tags'
