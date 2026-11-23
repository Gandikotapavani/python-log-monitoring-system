from log_parser import parse_log_file


def test_parse_valid_logs(tmp_path):
    log_file = tmp_path / "test.log"

    log_file.write_text(
        "2026-11-23 10:00:01 INFO Server started\n"
        "2026-11-23 10:01:15 ERROR Database failed\n"
    )

    logs = parse_log_file(log_file)

    assert len(logs) == 2
    assert logs[0]["level"] == "INFO"
    assert logs[1]["level"] == "ERROR"


def test_ignore_invalid_log_lines(tmp_path):
    log_file = tmp_path / "invalid.log"

    log_file.write_text(
        "This is an invalid log line\n"
        "2026-11-23 10:00:01 INFO Server started\n"
    )

    logs = parse_log_file(log_file)

    assert len(logs) == 1
    assert logs[0]["message"] == "Server started"
