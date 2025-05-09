from database import create_connection
import sqlite3

def insert_course(course_name, unit, user_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO course (name, unit, user_id) VALUES (?, ?, ?)",
            (course_name, unit, user_id)
        )
        conn.commit()
        print(" Course inserted successfully.")
    except sqlite3.IntegrityError:
        print(" Failed to insert course.")
    conn.close()


def search_course_by_id_and_userid(course_id, user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT course.id, course.name, course.unit
        FROM course
        JOIN users ON course.user_id = users.id
        WHERE course.id = ? AND users.id = ?
    ''', (course_id, user_id))
    rows = cursor.fetchall()
    conn.close()
    return rows


