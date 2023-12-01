from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, jsonify

import sqlite3

app = Flask(__name__)
app.secret_key = "mahsjdshdssdkdd_ncjdjkl"


# Database initialization function
def db(create_table=False):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    if create_table:
        c.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            ''')
    conn.commit()
    conn.close()


db()


# Route for the signin page
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    show_flash_message = False  # Flag to determine if flash message should be displayed

    if request.method == 'POST':
        username_or_email = request.form['username_or_email']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? OR email = ?',
                       (username_or_email, username_or_email))
        user = cursor.fetchone()
        conn.close()

        if user and user['password'] == password:
            flash('signin successful', 'success')  # Display a success message
            return redirect(url_for('index'))
        else:
            # Display an error message
            flash('Invalid username or password', 'error')
            show_flash_message = True  # Set the flag to True to show the flash message

    return render_template('signin.html', show_flash_message=show_flash_message)


# Route for the forgot password page
@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    show_flash_message = False  # Flag to determine if flash message should be displayed

    if request.method == 'POST':
        username = request.form['username']
        new_password = request.form['new-password']
        confirm_new_password = request.form['confirm-new-password']

        # Check if the passwords match
        if new_password != confirm_new_password:
            flash('Passwords do not match', 'error')
            show_flash_message = True  # Set the flag to True to show the flash message

    return render_template('forgot.html', show_flash_message=show_flash_message)


# Route for the sign-up page


# Route for the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    show_flash_message = False  # Flag to determine if flash message should be displayed

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        # Check if the passwords match
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            show_flash_message = True  # Set the flag to True to show the flash message
        else:
            # If passwords match, insert the user into the database
            conn = get_db_connection()
            cursor = conn.cursor()

            # Check if the username or email already exists in the database
            cursor.execute(
                'SELECT * FROM users WHERE username = ? OR email = ?', (username, email))
            existing_user = cursor.fetchone()

            if existing_user:
                flash('Username or email already exists', 'error')
                show_flash_message = True  # Set the flag to True to show the flash message
            else:
                # Insert the new user into the database
                cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                               (username, email, password))
                conn.commit()
                flash('Signup successful', 'success')
                return redirect(url_for('index'))

            conn.close()

    return render_template('signup.html', show_flash_message=show_flash_message)


# Route for the index page
@app.route('/')
@app.route('/index')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


# Route for serving static files (CSS, JS, images, etc.)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


# Route for "about.html" page
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')


# Route for the admin dashboard
@app.route('/admin/dashboard')
def admin_dashboard():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('admin_dashboard.html', users=users)


# Route for deleting a user based on username
@app.route('/delete_user/<string:username>', methods=['GET', 'DELETE'])
def delete_user(username):
    if request.method == 'DELETE':
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if the user exists
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user:
            # Delete the user from the database
            cursor.execute('DELETE FROM users WHERE username = ?', (username,))
            conn.commit()
            conn.close()
            flash(f'User {username} deleted successfully', 'success')
        else:
            flash(f'User {username} not found', 'error')

        return redirect(url_for('admin_dashboard'))
    else:
        # Handle the GET request to render the admin dashboard
        conn = get_db_connection()
        users = conn.execute('SELECT * FROM users').fetchall()
        conn.close()
        return render_template('admin_dashboard.html', users=users)


# Route for updating a user based on username
@app.route('/update_user/<string:username>', methods=['PUT'])
def update_user(username):
    if request.method == 'PUT':
        new_username = request.form['new_username']
        new_email = request.form['new_email']

        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if the user exists
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user:
            # Update the user in the database
            cursor.execute('UPDATE users SET username=?, email=? WHERE username=?',
                           (new_username, new_email, username))
            conn.commit()
            conn.close()
            flash(f'User {username} updated successfully', 'success')
        else:
            flash(f'User {username} not found', 'error')

        return redirect(url_for('admin_dashboard'))


# Route for fetching user information based on username
@app.route('/get_user/<string:username>', methods=['GET'])
def get_user(username):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if the user exists
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()

    if user:
        # Convert the user information to a dictionary and return as JSON
        user_dict = {
            'username': user['username'],
            'email': user['email'],
            'password': user['password'],
        }
        return jsonify(user_dict)
    else:
        return jsonify({'error': 'User not found'}), 404


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


if __name__ == '__main__':
    db(create_table=True)
    app.run(debug=True)
