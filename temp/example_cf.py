import cognitive_face as CF

KEY = 'a08b05d050b3412e953d444b74de98e3'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)
# southcentralus south central us
BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
BASE_URL = 'https://567334982645648512.cognitiveservices.azure.com/face/v1.0/'  # Replace with your regional Base URL
# BASE_URL = "https://567334982645648512.cognitiveservices.azure.com/"
CF.BaseUrl.set(BASE_URL)

img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
result = CF.face.detect(img_url)
print(result)

