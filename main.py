import cv2
import dlib
import pygame
import time
import threading
from model_download import download_and_extract_shape_predictor


download_and_extract_shape_predictor()
count = 0
def calculate_ear(eye):
    A = euclidean_distance(eye[1], eye[5])
    B = euclidean_distance(eye[2], eye[4])
    C = euclidean_distance(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

def playSound():
    pygame.init()
    sound = pygame.mixer.Sound("mixkit-slot-machine-win-alarm-1995.wav")
    sound.play()
    time.sleep(0.5)
    sound.stop()


def euclidean_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray)

    for face in faces:
        landmarks = landmark_predictor(gray, face)
        landmarks = [(p.x, p.y) for p in landmarks.parts()]  # Convert to list of tuples

        left_eye = landmarks[42:48]
        right_eye = landmarks[36:42]

        left_ear = calculate_ear(left_eye)
        right_ear = calculate_ear(right_eye)

        eye_state = "Open"
        ear_threshold = 0.2

        if left_ear < ear_threshold and right_ear < ear_threshold:
            eye_state = "Closed"

        if eye_state == "Closed":
            count += 1


        if eye_state == "Open":
            count = 0

        if count > 10:
            Make_Sound = threading.Thread(target=playSound)
            Make_Sound.start()


        cv2.putText(frame, f"Eye State: {eye_state} ", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


    cv2.imshow("Eye Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
