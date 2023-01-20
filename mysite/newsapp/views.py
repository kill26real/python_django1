from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import NewsForm, CommentForm
from .models import News, Comment


class NewsListView(ListView):
    template_name = 'newsapp/news-list.html'
    queryset = News.objects.all()
    context_object_name = 'news'


class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm

    def form_valid(self, form):
        if self.request.user.id:
            form.instance.user_id = self.request.user.id
            form.save()
            return HttpResponseRedirect(reverse_lazy('newsapp:news-list'))
        else:
            raise PermissionDenied('Чтобы создавать новости нужно сначало войти в систему')




class NewsDetailView(DetailView):
    template_name = 'newsapp/news_detail.html'
    model = News
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(new=self.object)
        context['form'] = CommentForm
        return context


    def post(self, request: HttpRequest, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user_id = self.request.user.id
            form.instance.new_id = self.object.id
            form.save()
        return reverse(
            'newsapp:news-details',
            kwargs={'pk': pk},
        )




class NewsDeleteView(DeleteView):
    model = News
    success_url = reverse_lazy('newsapp:news-list')

