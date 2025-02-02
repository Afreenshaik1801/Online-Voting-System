#Online Voting System

Online Voting System with Biometric Authentication
This project is an Online Voting System that incorporates Biometric Authentication using face recognition and fingerprint scanning for secure user authentication.

Project Overview
This system allows registered voters to securely cast their votes online using biometric authentication (face and fingerprint recognition). It includes an admin panel for managing voters and viewing results, as well as a voter registration process with biometric data capture.

Key Features
Voter Registration: Capture and store biometric data (face and fingerprint) for voter identification.
Biometric Authentication: Secure voting through face and fingerprint recognition.
Admin Panel: Admins can view registered voters and monitor election results.
Vote Management: Admins can manage voting activities and view the voting results in real-time.
Technologies Used
Python: Backend logic
Flask: Web framework
OpenCV: For face recognition
PyMySQL: MySQL database connector for Python
HTML/CSS/JS: Frontend design and interactivity
Bootstrap: For responsive UI design
MySQL: Database for storing voter information, votes, etc.

Setup Instructions
1. Clone the Repository
Clone this repository to your local machine using the following command:
git clone https://github.com/your-username/online-voting-system.git

2. Install Required Libraries
Navigate to the project directory and install the required Python libraries:
pip install -r requirements.txt

4. Set Up MySQL Database
Ensure MySQL is installed on your system.
Create a new database and tables based on the schema in database.py.
Update the database credentials in config.py.

5. Configure Flask App
Make sure the following configurations are correct in config.py:
Database: Update the MySQL username, password, and database name.
Secret Key: Set a secure secret key for Flask sessions.

6. Run the Application
Run the Flask application:
python app.py

The application will be available at http://127.0.0.1:5000.

Project Structure
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

Contributing
Feel free to fork this repository, make changes, and submit pull requests. If you encounter any issues, please feel free to open an issue.

License
This project is licensed under the MIT License - see the LICENSE file for details.
