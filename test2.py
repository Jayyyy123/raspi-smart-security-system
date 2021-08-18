from google.cloud import storage
from firebase import firebase

firebase = firebase.FirebaseApplication('https://gs://images-6e75.appspot.com')
client = storage.Client()
bucket = client.get_bucket('gs://images-6e75.appspot.com')
# posting to firebase storage
imageBlob = bucket.blob("/")
# imagePath = [os.path.join(self.path,f) for f in os.listdir(self.path)]
imagePath = "image.png"
imageBlob = bucket.blob("image.png")
imageBlob.upload_from_filename(imagePath)