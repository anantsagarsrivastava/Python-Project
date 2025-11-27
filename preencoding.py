import face_recognition
import numpy as np
import pickle
import os

# Folder with photos
image_folder = "photos"

encodings = []
names = []

for filename in os.listdir(image_folder):
    if filename.endswith((".jpg", ".png", ".jpeg")):
        path = os.path.join(image_folder, filename)
        name = os.path.splitext(filename)[0]

        image = face_recognition.load_image_file(path)
        encoding = face_recognition.face_encodings(image)[0]

        encodings.append(encoding)
        names.append(name)

# Save encodings & names
with open("encodings.pkl", "wb") as f:
    pickle.dump((encodings, names), f)

print("Encodings saved successfully!")
