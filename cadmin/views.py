import requests 
from django.shortcuts import render

def investor_profiles_view(request):
    # Correct way to use requests.get for external API calls
    url = "https://unix-aquatics.com/app/investorprofile/"
    try:
        response = requests.get(url)  # Make the GET request
        if response.status_code == 200:
            profiles = response.json()  # Parse JSON response
        else:
            profiles = []  # Fallback if API returns an error
    except requests.RequestException as e:
        print(f"Error fetching investor profiles: {e}") 
        profiles = []  # Fallback in case of a network error

    # Pass profiles to the template
    return render(request, 'cadmin/investers_profile.html', {'profiles': profiles})


import requests
from django.shortcuts import render

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






def index(request):
    # URLs for fetching data
    investor_profile_url = "https://unix-aquatics.com/app/investorprofile/"
    project_page_url = "https://unix-aquatics.com/app/Projectpage/"
    my_project_url="http://unix-aquatics.com/app/myprojects/"
    team_url="https://unix-aquatics.com/app/teammember/"
    
    # Initialize empty data containers
    profiles = []
    projects = []
    myprojects = []

    try:
        # Fetch investor profile data
        investor_response = requests.get(investor_profile_url)
        if investor_response.status_code == 200:
            profiles = investor_response.json()  # Parse JSON response
        else:
            profiles = []  # Fallback if API returns an error


        # Fetch project page data
        project_response = requests.get(project_page_url)
        if project_response.status_code == 200:
            projects = project_response.json()  # Parse JSON response
        else:
            projects = []  # Fallback if API returns an error


        myproject_response = requests.get(my_project_url)
        if myproject_response.status_code == 200:
            myprojects = myproject_response.json() 
        else:
            myprojects = []  # Fallback if API returns an error


        team_response = requests.get(team_url)
        if team_response.status_code == 200:
            team_members = team_response.json()  # Parse JSON response
        else:
            team_members= []  # Fallback if API returns an error



    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        profiles = []  # Fallback in case of a network error
        projects = []  # Fallback in case of a network error
        myprojects = []
        team_members= []

    # Pass both profiles and projects to the template
    return render(request, 'cadmin/index.html', {
        'profiles': profiles,
        'projects': projects,
        'myprojects': myprojects,
        'team_members' : team_members
    })



