from django.shortcuts import render

# Create your views here.


def profile(request):
    return render(request, 'sa_account_app/profile.html')
