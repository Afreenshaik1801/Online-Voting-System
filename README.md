# Online Voting System

## Online Voting System with Biometric Authentication
This project is an **Online Voting System** that incorporates **Biometric Authentication** using face recognition and fingerprint scanning for secure user authentication.

---

## Project Overview
This system allows registered voters to securely cast their votes online using **biometric authentication** (face and fingerprint recognition).  
It includes:
- **Admin Panel**: Manage voters and view results.  
- **Voter Registration**: Capture biometric data for authentication.  

---

## Key Features
✅ **Voter Registration**: Capture and store biometric data (face and fingerprint).  
✅ **Biometric Authentication**: Secure voting via face and fingerprint recognition.  
✅ **Admin Panel**: View registered voters and monitor election results.  
✅ **Vote Management**: Manage voting activities and view real-time results.  

---

## Technologies Used
- **Python**: Backend logic  
- **Flask**: Web framework  
- **OpenCV**: Face recognition  
- **PyMySQL**: MySQL database connector for Python  
- **HTML/CSS/JS**: Frontend design and interactivity  
- **Bootstrap**: Responsive UI design  
- **MySQL**: Database for storing voter information and votes  

---

## Setup Instructions

### 1️⃣ Clone the Repository
Clone this repository to your local machine using:
git clone https://github.com/your-username/online-voting-system.git

### 2️⃣ Install Required Libraries
Navigate to the project directory and install dependencies:
pip install -r requirements.txt

### 3️⃣ Set Up MySQL Database
Ensure MySQL is installed on your system.
Create a new database and tables based on database.py.
Update the database credentials in config.py.

### 4️⃣ Configure Flask App
In config.py, update:
Database: Set MySQL username, password, and database name.
Secret Key: Define a secure secret key for Flask sessions.

### 5️⃣ Run the Application
Start the Flask server:
python app.py

The application will be available at:
➡️ http://127.0.0.1:5000

### Project Structure
Online-Voting-System/
│
├── app.py                   # Main Flask application
├── config.py                # Database credentials and configuration
├── database.py              # Handles database connections
├── models/
│   ├── __init__.py          # Initializes models
│   ├── auth.py              # User authentication logic
│   ├── face_recognition_model.py   # Face capture and recognition logic
│   ├── fingerprint_recognition_model.py # Fingerprint capture (if implemented)
│   ├── register.py          # Registration logic
├── static/
│   ├── css/                 # Contains stylesheets (style.css)
│   ├── images/              # Stores biometric images
│   ├── js/                  # JavaScript files (script.js, webcam.js)
├── templates/               # HTML templates for the frontend (index.html, register.html, etc.)
├── requirements.txt         # List of Python dependencies
└── README.md                # Project overview and instructions

### Contributing
Feel free to fork this repository, make changes, and submit pull requests.
If you encounter any issues, open an issue on GitHub.

### License
📜 This project is licensed under the MIT License - see the LICENSE file for details.


