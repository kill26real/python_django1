from django.contrib.auth.decorators import login_required, permission_required
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
from django.contrib.auth.models import AnonymousUser


class NewsListView(ListView):
    template_name = 'newsapp/news-list.html'
    context_object_name = 'news'


    def get_queryset(self):
        if self.request.GET.get('tag', None):
            tag = self.request.GET.get('tag')
            queryset = News.objects.all().filter(tag=tag)
        else:
            queryset = News.objects.all()
        return queryset


class NewsCreateView(LoginRequiredMixin, CreateView):
    login_url = '/news/error/'
    redirect_field_name = 'redirect_to'
    model = News
    form_class = NewsForm


    def form_valid(self, form):
        if self.request.user.id:
            if self.request.user.profile.is_verificied:
                form.instance.user_id = self.request.user.id
                self.request.user.profile.news += 1
                self.request.user.profile.save()
                form.save()
                return HttpResponseRedirect(reverse_lazy('newsapp:news-list'))
            else:
                return redirect(reverse('newsapp:verify-error'))
        else:
            return redirect(reverse('newsapp:login-error'))


class LoginErrorView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
        }
        return render(request, 'newsapp/login-error.html', context=context)


class VerifyErrorView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
        }
        return render(request, 'newsapp/verify-error.html', context=context)


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
        if self.request.user.id:
            if form.is_valid():
                form.save(commit=False)
                form.instance.user_id = self.request.user.id
                form.instance.new_id = pk
                form.save()
            return redirect(reverse('newsapp:news-details',kwargs={'pk': pk},))
        else:
            if form.is_valid():
                form.save(commit=False)
                form.instance.user_id = 9  # TODO Почему 9? А если такого пользователя нет? Это не корректно. Просто
                                           #  оставьте пустым это поле, для чего в модели надо указать null=True, blank=True
                form.instance.new_id = pk
                form.save()
            return redirect(reverse('newsapp:news-details', kwargs={'pk': pk}, ))



class NewsDeleteView(DeleteView):
    model = News
    success_url = reverse_lazy('newsapp:news-list')

