from pathlib import Path
import json

REPORT = Path("/app/report.json")

def test_report_exists():
    """Criterion 1: the agent must create /app/report.json."""
    assert REPORT.exists(), "no report.json found"

def test_report_valid_json():
    """Criterion 5: the report must be valid JSON."""
    data = json.loads(REPORT.read_text())
    assert isinstance(data, dict)

def test_report_values():
    """Criterion 1-6: the JSON values must match the access-log summary."""
    assert json.loads(REPORT.read_text()) == {
        "total_requests": 6,
        "unique_clients": 3,
        "top_path": "/index.html",
        "top_path_count": 3,
    }