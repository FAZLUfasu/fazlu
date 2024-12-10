from google_auth_oauthlib.flow import InstalledAppFlow

# Load the client_secrets.json file
flow = InstalledAppFlow.from_client_secrets_file(
    r'D:\unix\client_secret_659084782744-iebvskanf18l42ic1hfkg521l4lr4rp7.apps.googleusercontent.com.json',  # Update this to the correct path
    scopes=['https://www.googleapis.com/auth/gmail.send'],
)

credentials = flow.run_local_server(port=0)

# Save the refresh token and client ID/secret
print("Refresh Token:", credentials.refresh_token)
