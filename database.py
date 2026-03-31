import sqlite3

# ------------------ Database Connection ------------------ #
def create_connection():
    conn = sqlite3.connect("/tmp/students.db")
    return conn

# ------------------ Table Creation ------------------ #
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

# ------------------ Add Student ------------------ #
def add_student(name, age, grade, email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade, email) VALUES (?, ?, ?, ?)",
                   (name, age, grade, email))
    conn.commit()
    conn.close()

# ------------------ Get All Students ------------------ #
def get_all_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()
    return data

# ------------------ Search Student ------------------ #
def search_student(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    data = cursor.fetchall()
    conn.close()
    return data

# ------------------ Update Student ------------------ #
def update_student(student_id, name, age, grade, email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=?, age=?, grade=?, email=? WHERE id=?",
                   (name, age, grade, email, student_id))
    conn.commit()
    conn.close()

# ------------------ Delete Student ------------------ #
def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()

# ------------------ Reset Students (Fresh Start) ------------------ #
def reset_students():
    """
    Deletes all student records and resets the AUTOINCREMENT counter.
    Use this for testing/demo purposes only.
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students")  # Delete all data
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='students'")  # Reset AUTOINCREMENT
    conn.commit()
    conn.close()

# ------------------ Initialize Table ------------------ #
create_table()
