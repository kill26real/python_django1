"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import MainView
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Author and Books API",
        default_version='v1',
        description='Описание проекта',
        terms_of_service='https://www.google.com/politics/terms/',
        contact=openapi.Contact(email='k.safelkin@mail.ru'),
        license=openapi.License(name=''),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny),
    # TODO ошибка в том, что вы указали одно значение (сами по себе одни лишь круглые скобки не создают кортежа),
    #  а требуется список - замените круглые скобки на квадратные)
)


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('shop/', include('shopapp.urls')),
    path('req/', include('requestdataapp.urls')),
    path('user/', include('userapp.urls')),
    path('emp/', include('employmentapp.urls')),
    path('news/', include('newsapp.urls')),
    path('blog/', include('blogapp.urls')),
    path('blog2/', include('blogapp2.urls')),
    path('api/', include('libraryapp.urls')),
    path('i18n', include('django.conf.urls.i18n')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
