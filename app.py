import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

DB_NAME = "logs/monitoring.db"


@app.route("/")
def dashboard():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row

    logs = connection.execute(
        "SELECT * FROM log_events ORDER BY id DESC"
    ).fetchall()

    alerts = connection.execute(
        "SELECT * FROM alerts ORDER BY id DESC"
    ).fetchall()

    total_logs = connection.execute(
        "SELECT COUNT(*) FROM log_events"
    ).fetchone()[0]

    error_count = connection.execute(
        "SELECT COUNT(*) FROM log_events WHERE level = 'ERROR'"
    ).fetchone()[0]

    warning_count = connection.execute(
        "SELECT COUNT(*) FROM log_events WHERE level = 'WARNING'"
    ).fetchone()[0]

    connection.close()

    return render_template(
        "index.html",
        logs=logs,
        alerts=alerts,
        total_logs=total_logs,
        error_count=error_count,
        warning_count=warning_count
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True) 
