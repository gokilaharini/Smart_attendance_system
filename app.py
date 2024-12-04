from flask import Flask, request, jsonify, render_template
from werkzeug.security import check_password_hash
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    user = cursor.execute(
        'SELECT * FROM users WHERE username = ? AND role = ?',
        (username, role)
    ).fetchone()
    
    conn.close()
    
    if user and check_password_hash(user['password_hash'], password):
        return jsonify({
            'success': True,
            'redirect': f"/{role}dashboard.html"
        })
    
    return jsonify({
        'success': False,
        'message': 'Invalid credentials'
    }), 401

if __name__ == '__main__':
    app.run(debug=True)