import face_recognition
from datetime import datetime
import cv2
import numpy as np
import csv
import os
import pickle

# ------------------------------------------
#      LOAD OR CREATE FACE ENCODINGS
# ------------------------------------------


print("Loading student encodings...")

encoding_file = "encodings.pkl"
image_folder = "photos"

if os.path.exists(encoding_file):
    # Load precomputed encodings
    with open(encoding_file, "rb") as f:
        known_face_encodings, known_face_names = pickle.load(f)
    print("Encodings loaded instantly!")
else:
    # If encodings not found, compute and save them
    print("Generating encodings (first-time setup)...")
    known_face_encodings = []
    known_face_names = []

    for filename in os.listdir(image_folder):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            path = os.path.join(image_folder, filename)
            name = os.path.splitext(filename)[0]  # filename without extension

            image = face_recognition.load_image_file(path)
            # Resize image for faster encoding (optional but helpful)
            image = cv2.resize(image, (500, 500))

            encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(encoding)
            known_face_names.append(name)

    with open(encoding_file, "wb") as f:
        pickle.dump((known_face_encodings, known_face_names), f)

    print("Encodings created and saved for future use!")

# ---------------- SHOW FULL STUDENT LIST -----------------


print("\n===== STUDENT LIST =====")
for s in known_face_names:
    print("•", s)
print("========================\n")

students_left = known_face_names.copy()
students_present = []

# -------------------------------------------------------
#                 CREATE CSV FOR TODAY
# -------------------------------------------------------
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

csv_file = open(current_date + ".csv", "w", newline="")
writer = csv.writer(csv_file)
writer.writerow(["Name", "Time"])

# -------------------------------------------------------
#                    START CAMERA
# -------------------------------------------------------


video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
process_frame = True

print("Starting attendance system... Press 'q' to exit.\n")

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Resize for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame, model="hog")
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, encoding, tolerance=0.5)
            distances = face_recognition.face_distance(known_face_encodings, encoding)
            best_match = np.argmin(distances)

            name = ""
            if matches[best_match]:
                name = known_face_names[best_match]

            if name != "":
                if name in students_left:
                    students_left.remove(name)
                    students_present.append(name)

                    now = datetime.now()
                    time_now = now.strftime("%H:%M:%S")

                    writer.writerow([name, time_now])
                    print(f"PRESENT → {name}")

    process_frame = not process_frame
    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -------------------------------------------------------
#                MARK ABSENT STUDENTS
# -------------------------------------------------------


print("\n===== ATTENDANCE SUMMARY =====")
print("\nPresent:")
for p in students_present:
    print("•", p)

print("\nAbsent:")
for a in students_left:
    print("•", a)

writer.writerow([])
writer.writerow(["ABSENT STUDENTS"])
for a in students_left:
    writer.writerow([a])

# -------------------------------------------------------
#                      CLEANUP
# -------------------------------------------------------


video_capture.release()
cv2.destroyAllWindows()
csv_file.close()

print("\nAttendance saved to:", current_date + ".csv")
print("Program finished.")
