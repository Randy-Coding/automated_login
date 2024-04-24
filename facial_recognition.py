import threading
import cv2
from deepface import DeepFace
from automate import (
    sign_in_with_1password,
)  # assuming automate.py is in the same directory


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_detected = False
reference_image = cv2.imread(r"C:\Users\Kage\Pictures\Camera Roll\reference_image.jpg")


def check_face(frame):
    global face_detected
    try:

        if DeepFace.verify(frame, reference_image)["verified"]:
            face_detected = True
        else:
            face_detected = False
    except ValueError:
        face_detected = False


while True:
    ret, frame = cap.read()
    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1
        if face_detected:
            sign_in_with_1password(r"C:\Program Files\1Password CLI\op.exe")
            break
    input = cv2.waitKey(1)
    if input == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
