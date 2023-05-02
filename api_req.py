import requests
import json
import base64
import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(filetypes=[('Image Files', ('*.jpg', '*.jpeg', '*.png', '*.bmp')), ('All Files', '*.*')])

print(f'Selected file: {file_path}')


options = ['Compress', 'Resize']

print('Please choose an option:')
for i, option in enumerate(options):
    print(f'{i+1}: {option}')

choice = input()

while not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
    print('Invalid choice. Please choose again:')
    choice = input()

selected_option = options[int(choice)-1]

print(f'You selected "{selected_option}"')

with open(file_path, 'rb') as f:
    image_data = f.read()

image_base64 = base64.b64encode(image_data).decode('utf-8')

if int(choice) == 1:
    # Create a dictionary containing the image data
    image_dict = {'image': image_base64}
    url = "http://127.0.0.1:5000/compress"
    payload = json.dumps(image_dict)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    img_data = response.json()['image']
    nparr = np.frombuffer(base64.b64decode(img_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow('Image.jpg', img)
    

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[('JPEG files', '*.jpg'), ('PNG files', '*.png')])

    if not file_path:
        print('No file selected')
    else:
        # save the image file using OpenCV
        cv2.imwrite(file_path, img)
        print(f'Saved image to {file_path}')

    cv2.waitKey(0)
    cv2.destroyAllWindows()


elif int(choice) == 2:
    width = int(input("Enter New Width: "))
    height = int(input("Enter New Height: "))
    url = "http://127.0.0.1:5000/resize"
    image_dict = {'image': image_base64, 'new_width': width, 'new_height': height}
    payload = json.dumps(image_dict)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    img_data = response.json()['image']
    nparr = np.frombuffer(base64.b64decode(img_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow('Image.jpg', img)
    
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[('JPEG files', '*.jpg'), ('PNG files', '*.png')])

    if not file_path:
        print('No file selected')
    else:
        cv2.imwrite(file_path, img)
        print(f'Saved image to {file_path}')

    cv2.waitKey(0)
    cv2.destroyAllWindows()