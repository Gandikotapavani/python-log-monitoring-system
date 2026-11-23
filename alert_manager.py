from log_parser import parse_log_file
from database import initialize_database, save_logs, save_alerts


ERROR_THRESHOLD = 3


def generate_alerts(file_path):
    logs = parse_log_file(file_path)

    error_count = 0
    warning_count = 0
    alerts = []

    for log in logs:
        level = log["level"]
        message = log["message"]

        if level == "ERROR":
            error_count += 1
            alerts.append(f"ERROR ALERT: {message}")

        elif level == "WARNING":
            warning_count += 1
            alerts.append(f"WARNING ALERT: {message}")

        if "failed login" in message.lower():
            alerts.append(f"SECURITY ALERT: {message}")

    if error_count >= ERROR_THRESHOLD:
        alerts.append(
            f"THRESHOLD ALERT: Error count reached {error_count}"
        )

    initialize_database()
    save_logs(logs)
    save_alerts(alerts)

    print("\n===== LOG MONITORING REPORT =====")
    print(f"Total Logs: {len(logs)}")
    print(f"Error Count: {error_count}")
    print(f"Warning Count: {warning_count}")

    print("\n===== GENERATED ALERTS =====")

    for alert in alerts:
        print(alert)

    print("\nLogs and alerts saved to SQLite database!")

    return alerts


if __name__ == "__main__":
    generate_alerts("logs/sample.log")
