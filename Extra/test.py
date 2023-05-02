import requests
import base64

# Open and encode image as base64
with open("test_2.png", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Send resize request
data = {
    "image_data": encoded_image,
    "width": 200,
    "height": 200
}
response = requests.post("http://localhost:5000/resize", json=data)

# Save resized image
with open("resized_image.jpg", "wb") as resized_image_file:
    resized_image_file.write(response.content)