from django.db import connection
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth
from django.db.models import Count
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.list import ListView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from projectapp.models import TransientHouseLocations, TransientHouse, Owner,PensionHouseLocations, PensionHouse, Profile
from .forms import TransientHouseForm, UserProfileForm
from datetime import timedelta
import json
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import logout
from django.db.models import Q 

class HomePageView(ListView):
    model = TransientHouseLocations
    context_object_name = 'home'
    template_name = "home.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        pass

def is_superuser(user):
    return user.is_superuser

def login_view(request):
    if request.user.is_authenticated:
         return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')


def transient_house_location(request):
    # Fetch all TransientHouseLocations
    transient_house_locations = TransientHouseLocations.objects.all()

    search_query = request.GET.get('search')
    if search_query:
        transient_house_locations = transient_house_locations.filter(
            Q(transient_house_locations__icontains=search_query) 
        )
    # Serialize the necessary fields including TransientHouse details through reverse relationship
    transient_house_json = serialize('json', transient_house_locations, 
                                     fields=('name', 'latitude', 'longitude', 'transienthouse__id'))

    context = {
        'transient_house_json': transient_house_json, 'search_query': search_query
    }

    return render(request, 'transient_house.html', context)

def transient_house_detail(request, transient_house_id):
    transient_house = get_object_or_404(TransientHouse, pk=transient_house_id)
    context = {
        'transient_house': transient_house
    }
    return render(request, 'transient_house_detail.html', context)

@user_passes_test(is_superuser)
@login_required

def dashboard(request):
    # Add logic here to fetch data for your dashboard
    context = {
        # Example data to pass to the template
        'user': request.user,
        'page_title': 'Dashboard',
    }
    return render(request, 'dashboard.html', context)

def edit_transient_house(request, pk):
    transient_house = get_object_or_404(TransientHouse, pk=pk)

    if request.method == 'POST':
        form = TransientHouseForm(request.POST, request.FILES, instance=transient_house)
        if form.is_valid():
            form.save()
            return redirect('transient_house_detail', transient_house_id=pk)  # Redirect to detail view after successful edit
    else:
        form = TransientHouseForm(instance=transient_house)
    
    return render(request, 'edit_transient_house.html', {'form': form})


def pension_house_location(request):
    # Fetch all Pension Houses
    pension_houses = PensionHouse.objects.all()
    
    # Serialize the necessary fields
    pension_house_json = serialize('json', pension_houses, 
                                   fields=('name', 'latitude', 'longitude', 'id'))
    
    context = {
        'pension_house_json': pension_house_json,
    }
    
    return render(request, 'pension_house.html', context)

def pension_house_detail(request, pension_house_id):
    pension_house = get_object_or_404(PensionHouse, pk=pension_house_id)
    
    context = {
        'pension_house': pension_house
    }
    
    return render(request, 'pension_house_detail.html', context)



def profile_view(request):
    # Retrieve the user's profile or create it if it doesn't exist
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    
    return render(request, 'profile.html', {'user_profile': user_profile})

def edit_profile(request):
    user = request.user
    profile = Profile.objects.get_or_create(user=user)[0]  # Retrieve or create Profile for the user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')  # Replace with your profile view name or URL
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'edit_profile.html', {'form': form})


def home_view(request):
    return render(request, 'home.html')

def pension_view(request):
    return render(request, 'pension.html')

def transient_view(request):
    return render(request, 'transient.html')

def lodge_view(request):
    return render(request, 'lodge.html')

def about_us_view(request):
    return render(request, 'about_us.html')

def transient_house_view(request):
    return render(request, 'transient_house.html')