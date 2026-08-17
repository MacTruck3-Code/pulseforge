# PulseForge Learning

This directory tracks the structured learning journey behind PulseForge.

PulseForge is both an engineering project and a practical learning environment. The goal is not only to complete features, but to understand the tools, decisions, trade-offs, and operational practices used to build them.

## Purpose

The learning records are intended to:

* Show how the project progresses over time
* Connect technical lessons to repository changes
* Record meaningful learning outcomes
* Identify concepts that need reinforcement
* Provide evidence of professional growth
* Support future portfolio and interview discussions

## Contents

* [Roadmap](roadmap.md) — The planned progression of technologies and engineering practices
* [Progress](progress.md) — Completed milestones, lessons learned, and areas for continued development

## Learning Workflow

Each lesson should follow this general process:

1. Define the lesson objective.
2. Identify the problem the technology or practice solves.
3. Create an issue with clear acceptance criteria.
4. Complete the work on a feature branch.
5. Validate the implementation.
6. Update and review the relevant documentation.
7. Record the completed learning outcomes and update the roadmap.
8. Open and review the implementation Pull Request.
9. Finalize all phase documentation inside that Pull Request before merge.
10. Merge the Pull Request only after the implementation, validation, documentation, and acceptance criteria are complete.
11. After merge, verify the merge, issue closure, CI results, and branch cleanup.

Final phase documentation should describe the completed implementation state and identify the next phase before the implementation Pull Request is merged.

Do not create a separate post-merge documentation change solely to mark a phase complete.

## Recording Progress

Progress entries should focus on meaningful outcomes rather than listing every command or activity.

Useful entries include:

* New concepts understood
* Engineering decisions made
* Important trade-offs considered
* Problems encountered and resolved
* Skills that need more practice
* Connections between previously learned concepts

Avoid turning this directory into a daily activity log.

## Documentation Boundaries

Use:

* `docs/` for system architecture, operations, deployment, and technical guidance
* `learning/` for roadmap progress, reflections, and skill development
* GitHub Issues for planned lessons and acceptance criteria
* Pull Requests for implementation history and review discussions
