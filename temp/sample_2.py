# import modules
import requests

# Request headers set Subscription key which provides access to this API. Found in your Cognitive Services accounts.
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'a08b05d050b3412e953d444b74de98e3',
}



body = dict()
body["url"] = "http://www.imagozone.com/var/albums/vedete/Matthew%20Perry/Matthew%20Perry.jpg?m=1355670659"
body = str(body)

# Request URL 
FaceApiDetect = 'https://westus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceAttributes=age,gender,headPose,smile,facialHair' 

FaceApiDetect = "https://567334982645648512.cognitiveservices.azure.com/face/v1.0/detect?returnFaceId=true&returnFaceAttributes=age,gender,headPose,smile,facialHair"

try:
    # REST Call 
    response = requests.post(FaceApiDetect, data=body, headers=headers) 
    print("RESPONSE:" + str(response.json()))

except Exception as e:
    print(e)