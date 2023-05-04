import urllib.request
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Function to check for internet connection
def check_internet():
    try:
        urllib.request.urlopen('http://www.google.com')
        return True
    except:
        return False

# Check for internet connection
if check_internet():
    # Authenticate with Google Drive
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() # Follow the authentication steps in the browser
    drive = GoogleDrive(gauth)

    # Set the path of the folder to upload
    folder_path = '/path/to/folder/'

    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Upload each file to Google Drive
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        file_drive = drive.CreateFile({'title': file_name})
        file_drive.Upload()
        print('File "%s" uploaded to Google Drive' % file_name)

    print('All files uploaded to Google Drive')
else:
    print('No internet connection found')
