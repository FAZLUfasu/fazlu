from django.shortcuts import render




def home(request):
    return render(request, 'landpageapp/index.html')


def about(request):
    return render(request, 'landpageapp/about.html') 

def privacy(request):
    return render(request, 'landpageapp/privacy.html') 

def support(request):
    return render(request, 'landpageapp/support.html') 
def team(request):
    return render(request, 'landpageapp/team.html') 


def subscribe(request):
    # You can handle the subscription logic here
    if request.method == 'POST':
        email = request.POST.get('email')
        # You could add logic to save the email or send a confirmation email
        print(f"Email received: {email}")  # Just an example; replace with actual logic
    return render(request, 'subscribe.html')  # Make sure you have a subscribe.html template


