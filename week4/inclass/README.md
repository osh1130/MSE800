# 🧑‍💼 User and Course Manager (SQLite)

A simple command-line application in Python for managing users and their assigned courses using an SQLite database.

## 📁 Project Structure

```
├── main.py              # Main menu logic
├── user_manager.py      # Add, search, view, delete users
├── course_manager.py    # Insert and search courses linked to users
├── database.py          # DB connection and table creation
├── sql_statment.py      # (Optional) MySQL test script
└── users.db             # SQLite database file (auto-created)
```

## 🛠 Features

### 👤 User Management
- Add user (name, email)
- View all users
- Search user by name (fuzzy match)
- Search user by name & ID
- Delete user by ID

### 📚 Course Management
- Insert course (name, unit, linked to user ID)
- Search course by course ID and user ID

## 🏗️ Setup Instructions

1. **Clone or download this repo**
2. Make sure you have **Python 3** installed
3. Install any required packages (if needed):
   ```bash
   pip install python-dotenv mysql-connector-python
   ```
4. Run the app:
   ```bash
   python main.py
   ```

## 📝 Notes

- Database is stored in `users.db` and created automatically on first run.
- `unit` in the course table represents course weight or credit value.
- Email must be **unique** for each user.
- Course records are linked to users via `user_id` (foreign key).

## 📌 Optional

`sql_statment.py` contains sample code for connecting to **MySQL**, not used in this project by default.