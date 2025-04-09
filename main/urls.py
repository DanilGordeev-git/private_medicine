from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('clinics/', views.clinics, name='clinics'),
    path('clinics/moscow/', views.moscow, name='moscow'),
    path('clinics/chita/', views.chita, name='chita'),
    path('clinics/samara/', views.samara, name='samara'),
    path('clinics/sochi/', views.sochi, name='sochi'),
    path('services/', views.services_list, name='services_list'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
