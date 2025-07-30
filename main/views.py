from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.

def single_slug(request, single_slug):
    try:
        categories = [c.category_slug for c in TutorialCategory.objects.all()]
        if single_slug in categories:
            matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)

            series_urls = {}
            for m in matching_series.all():
                part_ones = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest('created_at')
                series_urls[m] = part_ones
            return render(request,
                          'main/category.html',
                          context={'part_ones': series_urls})

        tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
        if single_slug in tutorials:
            this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
            tutorials_from_series = Tutorial.objects.filter(tutorial_series=this_tutorial.tutorial_series).order_by('created_at')
            this_tutorial_index = list(tutorials_from_series).index(this_tutorial)
            return render(request,
                          'main/tutorial.html',
                          {'tutorial': this_tutorial,
                          'sidebar': tutorials_from_series,
                          'this_tutorial_index': this_tutorial_index})
                          
        return HttpResponse(f"{single_slug} is a tutorial")

    except TutorialCategory.DoesNotExist:
        return HttpResponse(f"{single_slug} does not exist")

def homepage(request):
    return render(request=request,
                  template_name='main/categories.html',
                  context={'categories': TutorialCategory.objects.all()})

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            messages.info(request, f'You are now logged in as {username}!')
            return redirect('main:homepage')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = NewUserForm() 
        return render(request, 'main/register.html', context={'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('main:homepage')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = AuthenticationForm()
        return render(request, 'main/login.html', context={'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('main:homepage')