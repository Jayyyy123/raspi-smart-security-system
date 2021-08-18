from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client_secret_928305625059-ilfpsogk9rgm774cl8kqrei6qbi47c57.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '1j44Fz9O0H0zhLWhZv5N-kLfXxQpJiB6M'

file_name = 'test.jpg'
mime_types = 'image/jpeg'

file_metadata = {
    'name': file_name,
    'parents': [folder_id]
}

media = MediaFileUpload('{0}'.format(file_name), mimetype=mime_types)

service.files().create(
    body=file_metadata,
    media_body=media,
    fields='id'
).execute()
