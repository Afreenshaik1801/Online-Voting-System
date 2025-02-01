from flask import Flask, render_template, request, session, flash, redirect, url_for
import pymysql
import os
from database import db_connect
from models.face_recognition_model import capture_face  # Import capture_face function

app = Flask(__name__)
app.secret_key = "voting_secret"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        voter_id = request.form['voter_id']
        aadhar_id = request.form['aadhar_id']
        email = request.form['email']

        # Store aadhar_id in session for use in /capture
        session['aadhar'] = aadhar_id

        db = db_connect()
        cursor = db.cursor()
        try:
            # Check if aadhar_id already exists
            cursor.execute("SELECT * FROM voters WHERE aadhar_id = %s", (aadhar_id,))
            existing_user = cursor.fetchone()
            if existing_user:
                flash("Aadhar ID already registered", "danger")
                return redirect(url_for('register'))

            sql = "INSERT INTO voters (first_name, voter_id, aadhar_id, email) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (first_name, voter_id, aadhar_id, email))
            db.commit()
            flash("Registration successful", "success")
            
            # Call capture_face and store the face image path
            face_image_path = capture_face(aadhar_id)
            print(f"Face images saved to: {face_image_path}")
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
        finally:
            db.close()

        return redirect('/')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
