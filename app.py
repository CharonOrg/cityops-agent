from datetime import datetime, timezone
import json
from pathlib import Path


AUDIT_FILE = Path("data/audit.json")


VALID_PRIORITIES = {
    "Low",
    "Medium",
    "High",
}


def create_incident(
    title: str,
    service: str,
    priority: str = "Medium",
) -> dict:
    """Create a city operations incident."""

    if not title.strip():
        raise ValueError("Title cannot be empty.")

    if not service.strip():
        raise ValueError("Service cannot be empty.")

    if priority not in VALID_PRIORITIES:
        raise ValueError("Invalid priority.")

    return {
        "title": title.strip(),
        "service": service.strip(),
        "priority": priority,
        "status": "New",
    }


def requires_escalation(
    incident: dict,
) -> bool:
    """Determine whether an incident requires escalation."""

    return (
        incident["priority"] == "High"
        and incident["status"] == "Investigating"
    )


def build_triage_plan(
    incident: dict,
) -> list[str]:
    """Create a simple deterministic triage plan."""

    return [
        "Confirm incident scope",
        f"Inspect {incident['service']} health",
        "Collect evidence",
        "Identify owner",
        "Record outcome",
    ]


def record_event(
    incident_id: str,
    event: str,
) -> None:
    """Record an event in the local audit trail."""

    AUDIT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    records = []

    if AUDIT_FILE.exists():
        records = json.loads(
            AUDIT_FILE.read_text(
                encoding="utf-8"
            )
        )

    records.append(
        {
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
            "incident_id": incident_id,
            "event": event,
        }
    )

    AUDIT_FILE.write_text(
        json.dumps(
            records,
            indent=2,
        ),
        encoding="utf-8",
    )