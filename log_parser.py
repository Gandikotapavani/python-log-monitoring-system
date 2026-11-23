import re

def parse_log_file(file_path):
    events = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            match = re.match(
                r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|WARNING|ERROR) (.*)",
                line
            )

            if match:
                event = {
                    "timestamp": match.group(1),
                    "level": match.group(2),
                    "message": match.group(3)
                }
                events.append(event)

    return events


if __name__ == "__main__":
    logs = parse_log_file("logs/sample.log")

    for log in logs:
        print(log)
