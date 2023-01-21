from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import NewsForm, CommentForm
from .models import News, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class NewsListView(ListView):
    template_name = 'newsapp/news-list.html'
    queryset = News.objects.all()
    context_object_name = 'news'


class NewsCreateView(LoginRequiredMixin, CreateView):
    login_url = '/news/error/'
    redirect_field_name = 'redirect_to'
    model = News
    form_class = NewsForm

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.save()
        return HttpResponseRedirect(reverse_lazy('newsapp:news-list'))



class LoginErrorView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'news': True
        }
        return render(request, 'newsapp/login-error.html', context=context)


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
        if self.request.user.id:
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                form.instance.user_id = self.request.user.id
                form.instance.new_id = pk
                form.save()
            return redirect(reverse('newsapp:news-details',kwargs={'pk': pk},))
        else:
            return redirect(reverse('newsapp:login-error'))



class NewsDeleteView(DeleteView):
    model = News
    success_url = reverse_lazy('newsapp:news-list')

