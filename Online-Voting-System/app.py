from flask import Flask, render_template, request, session, flash, redirect, url_for
import pymysql
import os
from database import db_connect
from models import capture_face, capture_fingerprint
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "voting_secret"

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Admin Login Route
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Hardcoded admin credentials (for testing only)
        admin_email = 'admin@voting.com'
        admin_password = generate_password_hash('admin')  # Store password securely
        
        if email == admin_email and check_password_hash(admin_password, password):
            session['IsAdmin'] = True
            flash('Admin login successful', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('admin.html')

# Admin Dashboard Route
@app.route('/admin/dashboard')
def admin_dashboard():
    if 'IsAdmin' not in session:
        flash("Access denied!", "danger")
        return redirect(url_for('admin'))
    return render_template('dashboard.html')

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        voter_id = request.form['voter_id']
        aadhar_id = request.form['aadhar_id']
        email = request.form['email']

        session['aadhar'] = aadhar_id  # Store Aadhar ID for biometric capture

        db = db_connect()
        cursor = db.cursor()
        try:
            cursor.execute("SELECT * FROM voters WHERE aadhar_id = %s", (aadhar_id,))
            existing_user = cursor.fetchone()
            if existing_user:
                flash("Aadhar ID already registered", "danger")
                return redirect(url_for('register'))

            cursor.execute("SELECT * FROM voters WHERE voter_id = %s", (voter_id,))
            existing_voter = cursor.fetchone()
            if existing_voter:
                flash("Voter ID already registered", "danger")
                return redirect(url_for('register'))

            sql = "INSERT INTO voters (first_name, voter_id, aadhar_id, email) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (first_name, voter_id, aadhar_id, email))
            db.commit()
            flash("Registration successful", "success")
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
        finally:
            db.close()

        return redirect('/')
    return render_template('register.html')

# Capture Biometric Data (Face/Fingerprint) Route
@app.route('/capture', methods=['GET', 'POST'])
def capture():
    if 'aadhar' not in session:
        flash("You must register first!", "warning")
        return redirect(url_for('register'))

    if request.method == 'POST':
        face_image_path = capture_face(session['aadhar'])  # Using capture_face from models
        fingerprint_image_path = capture_fingerprint(session['aadhar'])  # Optional fingerprint capture

        flash("Biometric data captured successfully", "success")
        return redirect('/')

    return render_template('capture.html')

# View Voters Route
@app.route('/view_voters')
def view_voters():
    if 'IsAdmin' not in session:
        flash("Access denied!", "danger")
        return redirect(url_for('admin'))

    db = db_connect()
    cursor = db.cursor()
    cursor.execute("SELECT first_name, voter_id, aadhar_id, email FROM voters")
    voters = cursor.fetchall()
    db.close()

    return render_template('view_voters.html', voters=voters)

# View Results Route
@app.route('/view_results')
def view_results():
    if 'IsAdmin' not in session:
        flash("Access denied!", "danger")
        return redirect(url_for('admin'))

    results = [
        {"candidate_name": "Candidate A", "votes": 1500},
        {"candidate_name": "Candidate B", "votes": 700},
        {"candidate_name": "Candidate C", "votes": 1200},
    ]
    
    return render_template('view_results.html', results=results)

# Manage Voting Route
@app.route('/manage-voting')
def manage_voting():
    return render_template('manage_voting.html')

# Vote Route
@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        selected_candidate = request.form.get('candidate')
        if not selected_candidate:
            flash("Please select a candidate", "danger")
            return redirect(url_for('vote'))  # Redirect back to the vote page if no candidate selected
        
        db = db_connect()
        cursor = db.cursor()
        try:
            cursor.execute("SELECT candidate_name FROM candidates WHERE candidate_name = %s", (selected_candidate,))
            candidate = cursor.fetchone()
            if not candidate:
                flash("Invalid candidate selected", "danger")
                return redirect(url_for('vote'))

            cursor.execute("UPDATE votes SET vote_count = vote_count + 1 WHERE candidate_name = %s", (selected_candidate,))
            db.commit()
            flash("Vote submitted successfully!", "success")
        except Exception as e:
            db.rollback()
            flash(f"Error: {str(e)}", "danger")
        finally:
            db.close()

        return redirect(url_for('thank_you'))

    db = db_connect()
    cursor = db.cursor()
    cursor.execute("SELECT candidate_name FROM candidates")
    candidates = cursor.fetchall()
    db.close()

    return render_template('vote.html', candidates=candidates)

# Thank You Route
@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

# Logout Route
@app.route('/logout')
def logout():
    session.pop('IsAdmin', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
