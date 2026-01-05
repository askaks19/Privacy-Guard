import cv2
import mediapipe as mp
import pyautogui
import time


mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.6
)


cap = cv2.VideoCapture(0)


last_minimize_time = 0
MINIMIZE_COOLDOWN = 3  # seconds


print("🔐 Privacy Guard Started")
print("✔ 1 face → Normal")
print("⚠ 2+ faces → Window minimizes")


while True:
    ret, frame = cap.read()
    if not ret:
        break


    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb)


    face_count = 0


    if results.detections:
        face_count = len(results.detections)


        for det in results.detections:
            bbox = det.location_data.relative_bounding_box
            h, w, _ = frame.shape
            x = int(bbox.xmin * w)
            y = int(bbox.ymin * h)
            bw = int(bbox.width * w)
            bh = int(bbox.height * h)
            cv2.rectangle(frame, (x, y), (x + bw, y + bh), (0, 255, 0), 2)


    # Display face count
    cv2.putText(
        frame,
        f"Faces Detected: {face_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255) if face_count > 1 else (0, 255, 0),
        2
    )


    # Minimize window if more than one face
    current_time = time.time()
    if face_count > 1 and (current_time - last_minimize_time) > MINIMIZE_COOLDOWN:
        pyautogui.hotkey('win', 'down')
        last_minimize_time = current_time
        print("⚠ Extra face detected → Window minimized")


    cv2.imshow("Privacy Camera", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
