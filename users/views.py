from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomAuthForm

# Create your views here.


def custom_page_not_found_view(request, exception=None):
    context = {'title': 'Ошибка 404. Страница не найдена'}
    return render(request, 'errors/error_page.html', context=context, status=404)


def custom_error_view(request, exception=None):
    context = {'title': 'Ошибка 500. Внутренняя ошибка сервера'}
    return render(request, 'errors/error_page.html', context=context, status=500)


def custom_permission_denied_view(request, exception=None):
    context = {'title': 'Ошибка 403. Доступ запрещен'}
    return render(request, 'errors/error_page.html', context=context, status=403)


def custom_bad_request_view(request, exception=None):
    context = {'title': 'Ошибка 400. Ошибка запроса'}
    return render(request, 'errors/error_page.html', context=context, status=400)


class CustomLoginView(LoginView):
    authentication_form = CustomAuthForm
    redirect_authenticated_user = True
    template_name = 'users/login.html'
    extra_context = {'title': 'Вход в систему'}


class CustomLogoutView(LogoutView):
    template_name = 'users/logout.html'

