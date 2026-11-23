import sqlite3

DB_NAME = "logs/monitoring.db"


def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS log_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            level TEXT,
            message TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alert_type TEXT,
            message TEXT
        )
    """)

    cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS unique_log
        ON log_events(timestamp, level, message)
    """)

    cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS unique_alert
        ON alerts(alert_type, message)
    """)

    connection.commit()
    connection.close()


def save_logs(logs):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    for log in logs:
        cursor.execute("""
            INSERT OR IGNORE INTO log_events
            (timestamp, level, message)
            VALUES (?, ?, ?)
        """, (log["timestamp"], log["level"], log["message"]))

    connection.commit()
    connection.close()


def save_alerts(alerts):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    for alert in alerts:
        alert_type, message = alert.split(":", 1)

        cursor.execute("""
            INSERT OR IGNORE INTO alerts
            (alert_type, message)
            VALUES (?, ?)
        """, (alert_type.strip(), message.strip()))

    connection.commit()
    connection.close()
