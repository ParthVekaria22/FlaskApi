import json
import base64

with open('test.jpg', 'rb') as f:
    image_data = f.read()

# Encode the image data as a base64 string
image_base64 = base64.b64encode(image_data).decode('utf-8')

# Create a dictionary containing the image data
image_dict = {'image': image_base64}

# Convert the dictionary to a JSON object
json_data = json.dumps(image_dict)

# Print the JSON object
with open('image/img.json', 'w') as f:
    f.write(json_data)
