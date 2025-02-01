import cv2
import os
import numpy as np
from sklearn import svm  

def capture_fingerprint(aadhar_id):
    video_capture = cv2.VideoCapture(0) 
    ret, frame = video_capture.read()

    if not ret:
        raise Exception("Failed to capture image.")

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    fingerprint_features = np.random.rand(128)  
    
    fingerprint_folder = os.path.join("images", str(aadhar_id))
    if not os.path.exists(fingerprint_folder):
        os.makedirs(fingerprint_folder)

    fingerprint_features_path = os.path.join(fingerprint_folder, "fingerprint_features.npy")
    np.save(fingerprint_features_path, fingerprint_features)
    
    video_capture.release()
    return fingerprint_features_path
