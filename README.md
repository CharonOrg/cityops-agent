# CityOps Agent

A small GitHub Copilot agentic software-development workshop.

## Scenario

City operations receives incidents such as:

> 18 streetlights are not working in Sector 21.

The goal is to demonstrate how GitHub can turn an operational
incident into an agent-assisted software-development workflow.

## Application

The application supports:

- incident creation
- triage planning
- escalation detection
- audit events

## Test

```powershell
python -m unittest discover -s tests -v