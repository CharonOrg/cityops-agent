# CityOps Agent Instructions

## Purpose

This repository demonstrates an agentic software-development
workflow using GitHub Copilot.

Keep the application intentionally small.

## Engineering Rules

Use simple Python.

Prefer the standard library.

Do not introduce unnecessary frameworks.

Do not introduce unnecessary dependencies.

Make the smallest change that satisfies the issue.

Do not modify unrelated files.

## Testing

Every behavior change must have a unit test.

Run:

python -m unittest discover -s tests -v

Do not replace unittest with pytest.

## Security

Never:

- hard-code credentials;
- commit API keys;
- expose secrets;
- disable security checks;
- bypass CI;
- bypass branch protection;
- execute destructive commands.

## State

Use issue labels to communicate workflow state.

Valid states:

- agent:new
- agent:investigating
- agent:planned
- agent:implementing
- agent:review
- agent:resolved

Do not claim a state transition that did not occur.

## Agent Workflow

Before implementation:

1. Read the issue.
2. Inspect the repository.
3. Identify affected files.
4. Investigate the requirement.
5. Create a plan.

During implementation:

1. Make the smallest change.
2. Add tests.
3. Run tests.

After implementation:

1. Review the diff.
2. Explain the change.
3. Explain test results.
4. Identify remaining risks.

## Human Approval

Agents may investigate and implement.

Agents must not make the final merge decision.

A human must review and approve the pull request.