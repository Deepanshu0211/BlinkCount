import cv2
import dlib
import json

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

blink_count = 0
prev_blink_state = False

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)

        left_eye = landmarks.part(36).x, landmarks.part(36).y, landmarks.part(39).x, landmarks.part(39).y
        right_eye = landmarks.part(42).x, landmarks.part(42).y, landmarks.part(45).x, landmarks.part(45).y

        cv2.rectangle(frame, (left_eye[0], left_eye[1]), (left_eye[2], left_eye[3]), (0, 255, 0), 2)
        cv2.rectangle(frame, (right_eye[0], right_eye[1]), (right_eye[2], right_eye[3]), (0, 255, 0), 2)

        aspect_ratio_left = 0
        aspect_ratio_right = 0

        if left_eye[3] - left_eye[1] != 0:
            aspect_ratio_left = (left_eye[2] - left_eye[0]) / (left_eye[3] - left_eye[1])

        if right_eye[3] - right_eye[1] != 0:
            aspect_ratio_right = (right_eye[2] - right_eye[0]) / (right_eye[3] - right_eye[1])

        blink_threshold = 5.7

        if aspect_ratio_left < blink_threshold and aspect_ratio_right < blink_threshold:
            if not prev_blink_state:
                blink_count += 1
                prev_blink_state = True
        else:
            prev_blink_state = False

    cv2.putText(frame, f"Blinks: {blink_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Blink Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

with open("blink_count.json", "w") as json_file:
    json.dump({"blink_count": blink_count}, json_file)

cap.release()
cv2.destroyAllWindows()
