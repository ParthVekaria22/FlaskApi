import json
import base64
import numpy as np
import cv2

# Read the JSON file
with open('test.json', 'r') as f:
    json_data = json.load(f)

# Get the base64-encoded image data from the JSON data
image_base64 = json_data['resized_image']

# Decode the base64-encoded image data
image_data = base64.b64decode(image_base64)

# Convert the image data to a NumPy array
image_array = np.frombuffer(image_data, dtype=np.uint8)

# Decode the NumPy array as an image using OpenCV
image = cv2.imdecode(image_array, flags=cv2.IMREAD_COLOR)

# Show the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
