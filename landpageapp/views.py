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




# def about_view(request):
#     url = "https://unix-aquatics.com/app/AboutUs/"
#     response = request.get(url)
#     about_data = response.json() if response.status_code == 200 else {}

#     return render(request, 'about.html', {'about_data': about_data})


def team_page(request):
    response = request.get("https://unix-aquatics.com/app/teammember/")
    team_members = response.json()  # Assuming the API returns the team data in JSON format

    return render(request, 'team_page.html', {'team_members': team_members})


