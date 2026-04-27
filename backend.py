from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Funkcia na pripojenie k PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname="netusim_uz",
        user="netusim_uz_user",
        password="7qvI8csutUe7Xr5sk3i8H7BGxZLWdsoc",
        host="dpg-d7ng6tiqqhas73frvtt0-a.frankfurt-postgres.render.com",
        port=5432
    )
    return conn

# Domovská stránka
@app.route('/')
def home():
    return jsonify({"message": "Vitaj v mojom Flask backende napojenom na SQL databázu!"})

# Všetci študenti
@app.route('/api')
def get_all_students():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, surname, nickname, image, bio FROM students ORDER BY id")
    rows = cur.fetchall()

    students = []
    for row in rows:
        students.append({
            "id": row[0],
            "name": row[1],
            "surname": row[2],
            "nickname": row[3],
            "image": row[4],
            "bio": row[5]
        })

    cur.close()
    conn.close()

    return jsonify(students)

# Jeden študent podľa ID
@app.route('/api/student/<int:student_id>')
def get_student_by_id(student_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, name, surname, nickname, image, bio FROM students WHERE id = %s",
        (student_id,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row:
        student = {
            "id": row[0],
            "name": row[1],
            "surname": row[2],
            "nickname": row[3],
            "image": row[4],
            "bio": row[5]
        }
        return jsonify(student)

    return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)