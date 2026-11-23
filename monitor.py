import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from alert_manager import generate_alerts


LOG_FILE = "logs/sample.log"


class LogMonitor(FileSystemEventHandler):

    def on_modified(self, event):

        if event.src_path.endswith("sample.log"):
            print("\nNew log activity detected!")

            alerts = generate_alerts(LOG_FILE)

            if alerts:
                print("Monitoring alerts generated!")
            else:
                print("No alerts found.")


if __name__ == "__main__":

    event_handler = LogMonitor()
    observer = Observer()

    observer.schedule(
        event_handler,
        path="logs",
        recursive=False
    )

    observer.start()

    print("Automatic Log Monitoring Started...")
    print("Waiting for new log entries...")
    print("Press CTRL+C to stop.")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()
