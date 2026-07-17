# Flask To-Do List

A simple, persistent to-do list web app built with **Flask** and **SQLite**. Your tasks are saved to a local database file, so they survive page reloads and server restarts.

## Features

- ✅ Add, complete, and delete tasks
- 💾 Persistent storage via SQLite (`todo.db`)
- 🧹 Clear all completed tasks at once
- 📱 Clean, responsive UI

## Tech Stack

- [Flask](https://flask.palletsprojects.com/) (web framework)
- SQLite3 (built-in Python module for data storage)
- Jinja2 templates + vanilla HTML/CSS

## Setup

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd todoapp

# 2. Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## Project Structure

```
todoapp/
├── app.py                # Flask app + SQLite logic
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # UI template
└── todo.db               # SQLite database (auto-created on first run)
```

## Routes

| Method | Route             | Description                  |
|--------|-------------------|------------------------------|
| GET    | `/`               | Show all tasks               |
| POST   | `/add`            | Add a new task               |
| GET    | `/toggle/<id>`    | Toggle complete/incomplete   |
| GET    | `/delete/<id>`    | Delete a task                |
| GET    | `/clear_done`     | Delete all completed tasks   |

## Notes

- `todo.db` is created automatically on first launch. Add it to `.gitignore` if you don't want to commit your local data.
- The app uses Flask's development server — fine for local use. For production, run it behind a WSGI server like **gunicorn** or **waitress**.

## License

MIT
