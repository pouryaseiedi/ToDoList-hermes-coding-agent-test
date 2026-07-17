"""
Flask + SQLite To-Do app.
Data persists across restarts because it lives in todo.db (SQLite file).
"""

import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "todo.db")

app = Flask(__name__)


def get_db():
    """Open a connection with row access by column name."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create the table if it doesn't exist."""
    with get_db() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS todos (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                title     TEXT NOT NULL,
                done      INTEGER NOT NULL DEFAULT 0,
                created   TEXT NOT NULL
            )
            """
        )


@app.route("/")
def index():
    with get_db() as conn:
        rows = conn.execute(
            "SELECT * FROM todos ORDER BY done ASC, created DESC, id DESC"
        ).fetchall()
    return render_template("index.html", todos=rows)


@app.route("/add", methods=["POST"])
def add():
    title = (request.form.get("title") or "").strip()
    if title:
        from datetime import datetime
        created = datetime.now().strftime("%Y-%m-%d %H:%M")
        with get_db() as conn:
            conn.execute(
                "INSERT INTO todos (title, done, created) VALUES (?, 0, ?)",
                (title, created),
            )
    return redirect(url_for("index"))


@app.route("/toggle/<int:todo_id>")
def toggle(todo_id):
    with get_db() as conn:
        conn.execute(
            "UPDATE todos SET done = 1 - done WHERE id = ?", (todo_id,)
        )
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    with get_db() as conn:
        conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    return redirect(url_for("index"))


@app.route("/clear_done")
def clear_done():
    with get_db() as conn:
        conn.execute("DELETE FROM todos WHERE done = 1")
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="127.0.0.1", port=5000)
