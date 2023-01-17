from django.contrib.auth import authenticate, login, logout
from .forms import AuthForm
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView, LogoutView


def login_view(request: HttpRequest):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    if not user.is_superuser:
                        login(request, user)
                        return HttpResponse('Вы успешно вошли в систему')
                    else:
                        auth_form.add_error('__all__', 'Ошибка! Администраторы входят в другом месте!')
                else:
                    auth_form.add_error('__all__', 'Ошибка! Учетная запись с пользователем не активна!')
            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность написании логина и пароля')

    else:
        auth_form = AuthForm()
    context = {
        'form': auth_form
    }
    return render(request, 'userapp/user_form.html', context=context)


class AnotherLoginView(LoginView):
    template_name = 'userapp/user_form.html'


def logout_view(request: HttpRequest):
    logout(request)
    return HttpResponse('Вы успешно вышли из своей учетной записи')

class AnotherLogoutView(LogoutView):
    # template_name = 'users/logout.html'
    next_page = '/'