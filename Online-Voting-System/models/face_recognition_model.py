import cv2
import os
import face_recognition

def capture_face(aadhar_id):
    """Captures a face using the webcam and saves it for the given Aadhar ID."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Error: Could not access the webcam.")
        return None

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Error: Failed to capture image.")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            for (x, y, w, h) in faces:
                face = frame[y:y+h, x:x+w]
                folder_path = f"images/{aadhar_id}"
                os.makedirs(folder_path, exist_ok=True)
                image_path = f"{folder_path}/face.jpg"
                cv2.imwrite(image_path, face)  

                print("✅ Face captured successfully!")
                cap.release()
                cv2.destroyAllWindows()
                return image_path  

        cv2.imshow("Capture Face", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None

def verify_face(aadhar_id):
    """Compares a newly captured face with the stored one for authentication."""
    registered_image_path = f"images/{aadhar_id}/face.jpg"
    captured_image_path = capture_face(aadhar_id)

    if not (registered_image_path and captured_image_path):
        return False

    # Load and process the images
    registered_face = face_recognition.load_image_file(registered_image_path)
    captured_face = face_recognition.load_image_file(captured_image_path)

    # Get face encodings
    registered_encoding = face_recognition.face_encodings(registered_face)
    captured_encoding = face_recognition.face_encodings(captured_face)

    if not registered_encoding or not captured_encoding:
        print("❌ Error: No faces found in one or both images.")
        return False

    # Compare faces
    return face_recognition.compare_faces([registered_encoding[0]], captured_encoding[0])[0]
