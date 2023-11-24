from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os
import sqlite3

app = Flask(__name__)
app.secret_key = "mahsjdshdssdkdd_ncjdjkl"


# Database initialization function
# Database initialization function
def db(create_table=False):
    if not os.path.exists('database.db'):
        open('database.db', 'w').close()

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    if create_table:
        # Create the users table
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        # Create the posts table
        c.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL
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


# ... (other routes and functions remain unchanged)


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


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


if __name__ == '__main__':
    db(create_table=True)
    app.run(debug=True)