from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.main, name="main-page"),
    path('basket/', views.basket, name='basket-page'),
    path('reg/', views.reg, name="reg-page"),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name="login-page"),
    path('logout/', auth_views.LogoutView.as_view(template_name='shop/logout.html'), name="logout-page"),
    path('<str:category>/', views.get_products , name="products-page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
