from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
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
    success_url = reverse_lazy('newsapp:news-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(NewsCreateView, self).form_valid(form)  # TODO метод должен вернуть это значение, добавьте  return перед super(...)



#
# class NewsDetailView(DetailView):
#     queryset = (
#         News.objects
#         .select_related('user')
#     )

class NewsDetailView(DetailView):
    template_name = 'newsapp/news_detail.html'
    model = News
    context_object_name = 'news'



class NewsDeleteView(DeleteView):
    model = News
    success_url = reverse_lazy('newsapp:news-list')



class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm


    def get_success_url(self):
        return reverse(
            'newsapp:news-details',
            kwargs={'pk': self.object.pk},
        )


@login_required
def create_news(request: HttpRequest):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user  # TODO надо из объекта пользователя получить значение поля id: instance.user_id = request.user.id
            instance.save()
            News.objects.create(**form.cleaned_data)  # TODO это попытка создать туже новость повторно, это ошибка, уберите эту строку
            url = reverse('newsapp:news-list')
            return redirect(url)
    else:
        form = NewsForm()
    return render(request, 'newsapp/news_form.html', {'form': form})

# def create_order(request: HttpRequest):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             products = form.cleaned_data['products']
#             instance = form.save()
#             instance.products.add(*form.cleaned_data['products'])
#             url = reverse('shopapp:orders-list')
#             return redirect(url)
#     else:
#         form = OrderForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'shopapp/order_form.html', context=context)