
from django.shortcuts import render
from django.http import HttpResponse

def flutter_app(request):
    # Serve the Flutter web app index.html
    return render(request, 'unixapp/index.html')
