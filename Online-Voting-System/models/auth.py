from models.face_recognition_model import recognize_face, compare_faces
from models.fingerprint_recognition_model import recognize_fingerprint
from database import db_connect
import logging
import pickle  # For handling stored binary data (face encoding, fingerprint)

# Setting up logging
logging.basicConfig(filename='authentication.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def authenticate_user(aadhar_id, face_image_path, fingerprint_image_path):
    """Authenticate user based on face and fingerprint biometrics."""
    # Fetch stored biometric data
    stored_face_encoding, stored_fingerprint_template = get_stored_biometrics(aadhar_id)

    if stored_face_encoding is None or stored_fingerprint_template is None:
        logging.error(f"Authentication failed: Missing biometrics for Aadhar {aadhar_id}")
        return False  # User does not exist or biometrics are missing

    # Compare the face image
    if not authenticate_face(stored_face_encoding, face_image_path):
        logging.error(f"Authentication failed: Face mismatch for Aadhar {aadhar_id}")
        return False  # Face authentication failed

    # Compare the fingerprint image
    if not authenticate_fingerprint(stored_fingerprint_template, fingerprint_image_path):
        logging.error(f"Authentication failed: Fingerprint mismatch for Aadhar {aadhar_id}")
        return False  # Fingerprint authentication failed

    # If both face and fingerprint are authenticated successfully
    logging.info(f"Authentication successful for Aadhar {aadhar_id}")
    return True

def authenticate_face(stored_face_encoding, face_image_path):
    """Authenticate face by comparing stored encoding with the captured face."""
    captured_face_encoding = recognize_face(face_image_path)

    if captured_face_encoding:
        return compare_faces(stored_face_encoding, captured_face_encoding)
    
    logging.error("Face recognition failed: No encoding detected")
    return False

def authenticate_fingerprint(stored_fingerprint_template, fingerprint_image_path):
    """Authenticate fingerprint by comparing stored template with the captured fingerprint."""
    captured_fingerprint_template = recognize_fingerprint(fingerprint_image_path)

    if captured_fingerprint_template:
        return captured_fingerprint_template == stored_fingerprint_template  # Simple equality check

    logging.error("Fingerprint recognition failed: No template detected")
    return False

def get_stored_biometrics(aadhar_id):
    """Fetch the stored face encoding and fingerprint template for a given user."""
    db = db_connect()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT face_encoding, fingerprint_template FROM voters WHERE aadhar_id = ?", (aadhar_id,))
        result = cursor.fetchone()

        if result:
            # Unpickle binary data if stored in binary format
            face_encoding = pickle.loads(result[0]) if result[0] else None
            fingerprint_template = pickle.loads(result[1]) if result[1] else None
            return face_encoding, fingerprint_template

        logging.error(f"No biometric data found for Aadhar {aadhar_id}")
        return None, None

    except Exception as e:
        logging.error(f"Error fetching biometrics for Aadhar {aadhar_id}: {str(e)}")
        return None, None

    finally:
        db.close()
