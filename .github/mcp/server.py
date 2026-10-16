from mcp.server.fastmcp import FastMCP


mcp = FastMCP("cityops-tools")


INCIDENTS = {
    "INC-1001": {
        "service": "Lighting",
        "location": "Sector 21",
        "priority": "High",
        "status": "Investigating",
        "owner": "Electrical Response Team",
    },
    "INC-1002": {
        "service": "Drainage",
        "location": "Sector 18",
        "priority": "Medium",
        "status": "New",
        "owner": "Drainage Team",
    },
}


RUNBOOKS = {
    "Lighting": [
        "Confirm outage scope",
        "Check recent maintenance",
        "Inspect service health",
        "Dispatch field team",
    ],
    "Drainage": [
        "Check sensor health",
        "Review recent readings",
        "Inspect affected zone",
    ],
}


@mcp.tool()
def get_incident(
    incident_id: str,
) -> dict:
    """Return read-only incident information."""

    return INCIDENTS.get(
        incident_id,
        {
            "status": "Unknown"
        },
    )


@mcp.tool()
def get_runbook(
    service: str,
) -> dict:
    """Return the operational runbook."""

    return {
        "service": service,
        "steps": RUNBOOKS.get(
            service,
            [
                "Contact service owner."
            ],
        ),
    }


if __name__ == "__main__":
    mcp.run(
        transport="stdio"
    )