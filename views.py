from django.shortcuts import render
from django.http import JsonResponse
from .forms import RegistrationForm
from django.db import transaction 

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            return JsonResponse({'success': True})
        else:
            # Print out form errors for debugging
            print(form.errors)
            return JsonResponse({'success': False, 'error': 'Invalid form data'})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})