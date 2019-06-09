from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import index, about, contact

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('logout', LogoutView.as_view(
        template_name='logout.html'), name='logout'),
        path('login', LoginView.as_view(template_name='login.html'), name='login')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
