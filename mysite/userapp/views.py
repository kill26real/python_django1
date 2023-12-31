from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView, UpdateView
from .forms import RegisterForm
from .models import Profile
from .forms import AuthForm, RegisterForm
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from shopapp.models import Sale, Offer, Order
from django.core.cache import cache




class MyLoginView(LoginView):
    template_name = 'userapp/user_form.html'


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
            phone = form.cleaned_data.get('phone_number')
            Profile.objects.create(
                user=user,
                city=city,
                date_of_birth=date_of_birth,
                phone_number=phone,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            my_group = Group.objects.get(name='Пользователи')
            my_group.user_set.add(user)

            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'userapp/register.html', context=context)

class AccountView(DetailView):
    template_name = 'userapp/account.html'
    model = User
    context_object_name = 'user'

    def get_context_data(self, pk, **kwargs):
        if self.request.user.id != pk and not self.request.user.is_staff:
            raise PermissionError
        context = super().get_context_data(**kwargs)
        username = self.request.user.username

        sales_cache_key = f'sales:{username}'
        offers_chache_key = f'offers:{username}'
        offers = Offer.objects.filter(user=self.object)
        sales = Sale.objects.filter(user=self.object)

        user_account_cache_data = {
            sales_cache_key: sales,
            offers_chache_key: offers
        }

        data = cache.get_many(user_account_cache_data)

        if not data:
            cache.set_many(user_account_cache_data)
        context['offers'] = offers
        context['sales'] = sales
        context['orders'] = Order.objects.filter(user=self.object)
        return context


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['city', 'date_of_birth', 'phone_number']
    template_name = 'userapp/profile_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs['pk']
        if request.user.id != pk and not request.user.is_staff:
            raise PermissionError
        return super().dispatch(request, *args, **kwargs)


    def get_success_url(self):
        return reverse(
            'userapp:account',
            kwargs={'pk': self.object.user.pk},
        )


class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'userapp/user_update_form.html'

    def get_success_url(self):
        return reverse(
            'userapp:account',
            kwargs={'pk': self.object.pk},)

# def another_logout_view(request: HttpRequest):
#     logout(request)
#     return HttpResponse('Вы успешно вышли из своей учетной записи')


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
