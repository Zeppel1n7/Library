"""
URL configuration for EraLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from users.admin import admin_site
from EraLibrary import settings

admin.site = admin_site

handler404 = 'users.views.custom_page_not_found_view'
handler500 = 'users.views.custom_error_view'
handler403 = 'users.views.custom_permission_denied_view'
handler400 = 'users.views.custom_bad_request_view'

urlpatterns = [
    path('', include('library.urls', namespace='library')),
    path(f'{settings.ADMIN_URL}/', admin.site.urls, name='admin'),
    path('auth/', include('users.urls', namespace='users')),
]

if settings.ENABLE_DEBUG_TOOLBAR:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
