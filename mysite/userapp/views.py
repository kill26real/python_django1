from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .forms import AuthForm, RegisterForm
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView


# def another_login_view(request: HttpRequest):
#     if request.method == 'POST':
#         auth_form = AuthForm(request.POST)
#         if auth_form.is_valid():
#             username = auth_form.cleaned_data['username']
#             password = auth_form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 if user.is_active:
#                     if not user.is_superuser:
#                         login(request, user)
#                         return HttpResponse('Вы успешно вошли в систему')
#                     else:
#                         auth_form.add_error('__all__', 'Ошибка! Администраторы входят в другом месте!')
#                 else:
#                     auth_form.add_error('__all__', 'Ошибка! Учетная запись с пользователем не активна!')
#             else:
#                 auth_form.add_error('__all__', 'Ошибка! Проверьте правильность написании логина и пароля')
#
#     else:
#         auth_form = AuthForm()
#     context = {
#         'form': auth_form
#     }
#     return render(request, 'userapp/user_form.html', context=context)


class MyLoginView(LoginView):
    template_name = 'userapp/user_form.html'


# def another_logout_view(request: HttpRequest):
#     logout(request)
#     return HttpResponse('Вы успешно вышли из своей учетной записи')

class MyLogoutView(LogoutView):
    # template_name = 'users/logout.html'
    next_page = '/'


def register_view(request: HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                date_of_birth=date_of_birth

            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'userapp/register.html', context=context)
