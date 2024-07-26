"""
URL configuration for projectsite project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from projectapp.views import transient_house_location, transient_house_detail, edit_transient_house, pension_house_location, pension_house_detail, profile_view, edit_profile, logout_view, login_view, dashboard, home_view, pension_view, transient_view, lodge_view, about_us_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),
    path('transient/', transient_house_location, name='transient-house'),
    path('transient_house/<int:transient_house_id>/', transient_house_detail, name='transient_house_detail'),
    path('edit/<int:pk>/', edit_transient_house, name='edit_transient_house'),
    path('pension/', pension_house_location, name='pension-house'),
    path('pension_house/<int:pension_house_id>/', pension_house_detail, name='pension_house_detail'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),

    path('dashboard/', dashboard, name='dashboard'),
    path('home', home_view, name='homeview'),
    path('pension_view/', pension_view, name='pension'),
    path('transient_view/', transient_view, name='transient'),
    path('lodge_view/', lodge_view, name='lodge'),
    path('about-us/', about_us_view, name='about_us'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)