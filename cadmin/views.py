import requests 
from django.shortcuts import render, redirect, get_object_or_404
from fasu.models import InvestorProfile
from .forms import InvestorProfileForm  # We will create this form next
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User



# def investor_profiles_view(request):
#     # Correct way to use requests.get for external API calls
#     url = "https://unix-aquatics.com/app/investorprofile/"
#     try:
#         response = requests.get(url)  # Make the GET request
#         if response.status_code == 200:
#             profiles = response.json()  # Parse JSON response
#         else:
#             profiles = []  # Fallback if API returns an error
#     except requests.RequestException as e:
#         print(f"Error fetching investor profiles: {e}") 
#         profiles = []  # Fallback in case of a network error

#     # Pass profiles to the template
#     return render(request, 'cadmin/investers_profile.html', {'profiles': profiles})




# 1. List View (Read)
def investor_profiles_view(request):
    profiles = InvestorProfile.objects.all()
    return render(request, 'cadmin/investers_profile.html', {'profiles': profiles})


def create_investor_profile(request):
    if request.method == 'POST':
        # Create user form (using built-in Django form for user creation)
        user_form = UserCreationForm(request.POST)
        profile_form = InvestorProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            email = profile_form.cleaned_data['email']

            # Check if the email already exists in the InvestorProfile database
            if InvestorProfile.objects.filter(email=email).exists():
                profile_form.add_error('email', 'This email is already associated with an investor profile.')
            else:
                # Save User first
                user = user_form.save()

                # Save InvestorProfile with the user
                profile = profile_form.save(commit=False)
                profile.user = user  # Associate the new user with this profile
                profile.save()

                # Optionally log the user in after registration
                login(request, user)

                # Redirect to the list of investor profiles after successful creation
                return redirect('cadmin:investor_profiles')

    else:
        user_form = UserCreationForm()
        profile_form = InvestorProfileForm()

    return render(request, 'cadmin/create_investor_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


# 3. Update View
def update_investor_profile(request, pk):
    profile = get_object_or_404(InvestorProfile, pk=pk)
    if request.method == 'POST':
        form = InvestorProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('cadmin:investor_profiles')
    else:
        form = InvestorProfileForm(instance=profile)
    return render(request, 'cadmin/update_investor_profile.html', {'form': form, 'profile': profile})

# 4. Delete View
def delete_investor_profile(request, pk):
    profile = get_object_or_404(InvestorProfile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('cadmin:investor_profiles')
    return render(request, 'cadmin/delete_investor_profile.html', {'profile': profile})

def project_page_view(request):
    # Correct way to use requests.get for external API calls
    url = "https://unix-aquatics.com/app/Projectpage/"  # Change this URL to the correct project API endpoint
    try:
        response = requests.get(url)  # Make the GET request
        if response.status_code == 200:
            projects = response.json()  # Parse JSON response
        else:
            projects = []  # Fallback if API returns an error
    except requests.RequestException as e:
        print(f"Error fetching project data: {e}") 
        projects = []  # Fallback in case of a network error

    # Pass projects to the template
    return render(request, 'cadmin/projectpage.html', {'projects': projects})



def my_project_page_view(request):
    # Correct API endpoint for My Projects data
    url = "https://unix-aquatics.com/app/myprojects/"
    
    try:
        response = requests.get(url)  # Make the GET request
        if response.status_code == 200:
            myprojects = response.json()  # Parse JSON response
        else:
            myprojects = []  # Fallback if API returns an error
    except requests.RequestException as e:
        print(f"Error fetching my projects data: {e}") 
        myprojects = []  # Fallback in case of a network error

    # Pass projects to the template
    return render(request, 'cadmin/myprojectpage.html', {'myprojects': myprojects})




def team_members_view(request):
    url = "https://unix-aquatics.com/app/teammember/"
    
    try:
        response = requests.get(url)  # Send a GET request to fetch the team member data
        response.raise_for_status()  # Raise an exception for HTTP errors
        team_members = response.json()  # Parse the JSON data into a Python object
    except requests.exceptions.RequestException as e:
        team_members = []  # In case of an error, set an empty list
        print(f"Error fetching team members: {e}")
    
    return render(request, 'cadmin/teammembers.html', {'team_members': team_members})






# def index(request):
#     # URLs for fetching data
#     investor_profile_url = "https://unix-aquatics.com/app/investorprofile/"
#     project_page_url = "https://unix-aquatics.com/app/Projectpage/"
#     my_project_url="http://unix-aquatics.com/app/myprojects/"
#     team_url="https://unix-aquatics.com/app/teammember/"
    
#     # Initialize empty data containers
#     profiles = []
#     projects = []
#     myprojects = []

#     try:
#         # Fetch investor profile data
#         investor_response = requests.get(investor_profile_url)
#         if investor_response.status_code == 200:
#             profiles = investor_response.json()  # Parse JSON response
#         else:
#             profiles = []  # Fallback if API returns an error


#         # Fetch project page data
#         project_response = requests.get(project_page_url)
#         if project_response.status_code == 200:
#             projects = project_response.json()  # Parse JSON response
#         else:
#             projects = []  # Fallback if API returns an error


#         myproject_response = requests.get(my_project_url)
#         if myproject_response.status_code == 200:
#             myprojects = myproject_response.json() 
#         else:
#             myprojects = []  # Fallback if API returns an error


#         team_response = requests.get(team_url)
#         if team_response.status_code == 200:
#             team_members = team_response.json()  # Parse JSON response
#         else:
#             team_members= []  # Fallback if API returns an error



#     except requests.RequestException as e:
#         print(f"Error fetching data: {e}")
#         profiles = []  # Fallback in case of a network error
#         projects = []  # Fallback in case of a network error
#         myprojects = []
#         team_members= []

#     # Pass both profiles and projects to the template
#     return render(request, 'cadmin/index.html', {
#         'profiles': profiles,
#         'projects': projects,
#         'myprojects': myprojects,
#         'team_members' : team_members
#     })

from django.db.models import Sum

def index(request):
    # URLs for fetching data
    investor_profile_url = "https://unix-aquatics.com/app/investorprofile/"
    project_page_url = "https://unix-aquatics.com/app/Projectpage/"
    my_project_url = "http://unix-aquatics.com/app/myprojects/"
    team_url = "https://unix-aquatics.com/app/teammember/"
    
    # Initialize empty data containers
    profiles = []
    projects = []
    myprojects = []
    team_members = []
    dividends = []
    project_dividends = {}
    user_dividends = {}
    total_net_dividend = 0

    try:
        # Fetch investor profile data
        investor_response = requests.get(investor_profile_url)
        if investor_response.status_code == 200:
            profiles = investor_response.json()  # Parse JSON response

        # Fetch project page data
        project_response = requests.get(project_page_url)
        if project_response.status_code == 200:
            projects = project_response.json()  # Parse JSON response

        # Fetch my projects data
        myproject_response = requests.get(my_project_url)
        if myproject_response.status_code == 200:
            myprojects = myproject_response.json()  # Parse JSON response

        # Fetch team members data
        team_response = requests.get(team_url)
        if team_response.status_code == 200:
            team_members = team_response.json()  # Parse JSON response

        # Get all dividends
        dividends = Dividend.objects.all()

        # Calculate total dividends for each project and user
        for dividend in dividends:
            project = dividend.project
            user = dividend.user

            # Add the dividend to the total for the project
            if project not in project_dividends:
                project_dividends[project] = 0
            project_dividends[project] += dividend.dividend_amount

            # Add the dividend to the total for the user
            if user not in user_dividends:
                user_dividends[user] = 0
            user_dividends[user] += dividend.dividend_amount

        # Calculate net dividend for all projects
        total_net_dividend = Dividend.objects.aggregate(total_net_dividend=Sum('dividend_amount'))['total_net_dividend'] or 0

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

    # Pass all data to the template
    return render(request, 'cadmin/index.html', {
        'profiles': profiles,
        'projects': projects,
        'myprojects': myprojects,
        'team_members': team_members,
        'dividends': dividends,
        'project_dividends': project_dividends,
        'user_dividends': user_dividends,
        'total_net_dividend': total_net_dividend,
    })


from django.shortcuts import render
from fasu.models import Dividend
from django.db.models import Sum



def dividend_view(request):
    # Get all dividends
    dividends = Dividend.objects.all()

    # Create dictionaries for project and user dividends
    project_dividends = {}
    user_dividends = {}

    # Calculate the total dividends for each project and user
    for dividend in dividends:
        project = dividend.project
        user = dividend.user

        # Add the dividend to the total for the project
        if project not in project_dividends:
            project_dividends[project] = 0
        project_dividends[project] += dividend.dividend_amount

        # Add the dividend to the total for the user
        if user not in user_dividends:
            user_dividends[user] = 0
        user_dividends[user] += dividend.dividend_amount

    # Calculate net dividend for all projects
    total_net_dividend = Dividend.objects.aggregate(total_net_dividend=Sum('dividend_amount'))['total_net_dividend'] or 0

    # Prepare context data
    context = {
        'dividends': dividends,
        'project_dividends': project_dividends,
        'user_dividends': user_dividends,
        'total_net_dividend': total_net_dividend,
    }

    # Render the template with context data
    return render(request, 'cadmin/dividend.html', context)
