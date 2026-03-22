import sqlite3

def create_connection():
    conn = sqlite3.connect("students.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_student(name, age, grade, email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade, email) VALUES (?, ?, ?, ?)",
                   (name, age, grade, email))
    conn.commit()
    conn.close()

def get_all_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()
    return data

def search_student(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    data = cursor.fetchall()
    conn.close()
    return data

def update_student(student_id, name, age, grade, email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=?, age=?, grade=?, email=? WHERE id=?",
                   (name, age, grade, email, student_id))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()

create_table()