
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def flutter_app(request):
    # Serve the Flutter web app index.html
    return render(request, 'unixapp/index.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace with your desired redirect after login
    else:
        form = AuthenticationForm()

    return render(request, 'unixapp/index.html', {'form': form})
