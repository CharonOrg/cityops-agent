import unittest

from app import (
    build_triage_plan,
    create_incident,
    requires_escalation,
)


class TestIncident(unittest.TestCase):

    def test_create_incident(self):
        incident = create_incident(
            "Streetlight outage",
            "Lighting",
            "High",
        )

        self.assertEqual(
            incident["title"],
            "Streetlight outage",
        )

        self.assertEqual(
            incident["priority"],
            "High",
        )

        self.assertEqual(
            incident["status"],
            "New",
        )

    def test_empty_title(self):
        with self.assertRaises(ValueError):
            create_incident(
                "",
                "Lighting",
            )

    def test_empty_service(self):
        with self.assertRaises(ValueError):
            create_incident(
                "Outage",
                "",
            )

    def test_invalid_priority(self):
        with self.assertRaises(ValueError):
            create_incident(
                "Outage",
                "Lighting",
                "Critical",
            )

    def test_high_investigating_escalates(self):
        incident = create_incident(
            "Streetlight outage",
            "Lighting",
            "High",
        )

        incident["status"] = "Investigating"

        self.assertTrue(
            requires_escalation(incident)
        )

    def test_medium_does_not_escalate(self):
        incident = create_incident(
            "Streetlight outage",
            "Lighting",
            "Medium",
        )

        incident["status"] = "Investigating"

        self.assertFalse(
            requires_escalation(incident)
        )

    def test_triage_plan(self):
        incident = create_incident(
            "Streetlight outage",
            "Lighting",
        )

        plan = build_triage_plan(
            incident
        )

        self.assertEqual(
            len(plan),
            5,
        )


if __name__ == "__main__":
    unittest.main()