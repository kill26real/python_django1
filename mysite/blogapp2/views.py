from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Article
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from .forms import ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import View


# class ArticlesListView(ListView):
#     template_name = 'blogapp2/article_list.html'
#     queryset = Article.objects.filter(archivated=False)
#     context_object_name = 'articles'


class ArticlesListView(ListView):
    queryset = (
        Article.objects
        .defer('content')
        .select_related('author', 'category')
        .prefetch_related('tags')
    )


class ArticleDetailsView(DetailView):
    template_name = 'blogapp2/article_details.html'
    model = Article
    context_object_name = 'article'


# class ArticleCreateView(LoginRequiredMixin, CreateView):
#     login_url = '/blog2/login-error/'
#     redirect_field_name = 'redirect_to'
#     model = Article
#     form_class = ArticleForm
#
#
#     def form_valid(self, form):
#         if self.request.user.id:
#             form.instance.author = self.request.user.username
#             form.save()
#             return HttpResponseRedirect(reverse_lazy('blogapp2:articles-list'))
#         else:
#             return redirect(reverse('blogapp2:login-error'))

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('blogapp2:articles-list')


# class LoginErrorView(View):
#     def get(self, request: HttpRequest) -> HttpResponse:
#         context = {
#         }
#         return render(request, 'blogapp2/login-error.html', context=context)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = 'title', 'content', 'author', 'category', 'tags'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse(
            'blogapp2:article-details',
            kwargs={'pk': self.object.pk},
        )

