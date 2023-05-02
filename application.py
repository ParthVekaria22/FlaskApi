from flask import Flask, request, jsonify
import base64
import numpy as np
import cv2

application = Flask(__name__)

@application.route('/compress', methods=['POST'])
def compress():
    # Get the image data from the request
    json_data = request.get_json()
    image_base64 = json_data['image']

    # Decode the base64-encoded image data
    image_data = base64.b64decode(image_base64)

    # Convert the image data to a NumPy array
    image_array = np.frombuffer(image_data, dtype=np.uint8)

    # Decode the NumPy array as an image using OpenCV
    image = cv2.imdecode(image_array, flags=cv2.IMREAD_COLOR)

    # Compress the image using JPEG compression
    _, compressed_image_data = cv2.imencode('.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 50])

    # Encode the compressed image data as a base64 string
    compressed_image_base64 = base64.b64encode(compressed_image_data).decode('utf-8')

    # Create a JSON response containing the compressed image data
    response_data = {
        'image': compressed_image_base64
    }
    # Return the JSON response
    return jsonify(response_data)

@application.route('/resize', methods=['POST'])
def resize_image():
    data = request.get_json()

    # read image from base64 encoded string
    img_data = data['image'].encode('utf-8')
    nparr = np.frombuffer(base64.b64decode(img_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # get the new size of the image
    new_width = data['new_width']
    new_height = data['new_height']

    # resize the image
    resized_img = cv2.resize(img, (new_width, new_height))

    # convert resized image to base64 encoded string
    retval, buffer = cv2.imencode('.jpg', resized_img)
    img_as_text = base64.b64encode(buffer).decode('utf-8')

    # return the resized image as a JSON response
    response = {
        'image': img_as_text
    }

    return jsonify(response)

if __name__ == '__main__':
    application.run(debug=True)
