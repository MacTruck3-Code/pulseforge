# AI Collaboration Guide

This file defines how AI assistants should collaborate on the PulseForge repository.

## Project Purpose

PulseForge is a long-term engineering project designed to develop production-quality Platform Engineering skills through incremental application development.

The project includes learning paths for:

* Python
* Docker
* Kubernetes
* Helm
* Terraform
* OpenTelemetry
* Elastic Stack
* GitHub Actions
* CI/CD
* Observability
* DevOps
* Site Reliability Engineering

The goal is not only to build a working application. The goal is to understand the engineering decisions, trade-offs, and operational practices behind it.

## Collaboration Priorities

AI assistants must prioritize:

1. Teaching
2. Explaining trade-offs
3. Reviewing decisions
4. Generating code

Code generation should not replace explanation unless the user explicitly requests code only.

## Working Principles

AI assistants must:

* Explain the problem before recommending an implementation.
* Prefer simple and maintainable solutions.
* Introduce new technology only when it provides clear value.
* Break work into small, manageable steps.
* Reinforce previously introduced concepts.
* Distinguish industry best practices from personal recommendations.
* Challenge poor architectural decisions respectfully.
* Identify assumptions, risks, and technical debt.
* Review existing repository files before recommending changes.
* Update relevant documentation alongside meaningful changes.

## Development Workflow

The repository uses the following workflow:

1. Work begins with a defined issue or lesson.
2. Development occurs on a feature branch.
3. Changes are made incrementally.
4. Commits should be small and intentional.
5. Every lesson ends with a Pull Request.
6. Pull Requests are reviewed before merging.
7. Direct pushes to `main` are not allowed.

AI assistants must not recommend bypassing branch protection or the Pull Request process.

## Scope Control

AI assistants must implement only what is required for the current lesson or phase.

Future improvements may be documented, but they should not be implemented prematurely.

Avoid:

* Unnecessary abstractions
* Large rewrites
* Unrequested dependencies
* Premature infrastructure
* Premature automation
* Unrelated file changes

## Code and Configuration Changes

Before modifying code or configuration, AI assistants should:

1. Review the relevant existing files.
2. Explain the intended change.
3. Identify important trade-offs.
4. Make the smallest useful change.
5. Explain how the change should be validated.

Generated code should be readable, maintainable, and appropriate for a production-oriented learning project.

## Documentation Expectations

Documentation should describe the repository as it currently exists.

Planned components must be clearly labeled as future work.

Avoid documenting proposed architecture as though it has already been implemented.

For phase implementation work:

* Review all relevant documentation before opening the implementation Pull Request.
* Once implementation and validation acceptance criteria are satisfied, final phase documentation must describe the phase as Complete before merge.
* `learning/progress.md` and `learning/roadmap.md` must identify the completed phase and the next phase before merge.
* Do not use temporary statuses such as `In progress` or `PR pending` in final phase documentation merely because the implementation Pull Request has not yet merged.
* The implementation Pull Request is the final documentation update for the phase.
* After merge, only verify the merge, issue closure, CI results, and branch cleanup.
* Do not create a separate post-merge documentation change solely to mark the phase complete.

## Review Expectations

When reviewing a change, AI assistants should evaluate:

* Correctness
* Simplicity
* Maintainability
* Security
* Operational impact
* Testability
* Documentation
* Alignment with the current lesson
* Alignment with the project’s long-term architecture

Review feedback should explain why a change is recommended.

## Definition of Done

A lesson is complete when:

* Acceptance criteria are met.
* The change functions correctly.
* Relevant documentation is updated.
* The reasoning behind the solution is understood.
* The work is reviewed through a Pull Request.
* The repository is left in a better state than before.
