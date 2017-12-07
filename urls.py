from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('', views.index_view, name='index'),
	path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
	path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),	
	path('accounts/profile/', views.account_view, name='account'),
	path('shop/', views.shop_view, name='shop'),
	path('history/', views.history_view, name='history'),
	path('shop/submit/', views.submit_view, name='shopsubmit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
