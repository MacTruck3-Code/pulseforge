# Contributing to PulseForge

PulseForge is a production-oriented learning project. Contributions should improve both the repository and the contributor's understanding of the engineering decisions involved.

## Development Principles

Contributions should favor:

* Simplicity over cleverness
* Maintainability over shortcuts
* Small improvements over large rewrites
* Automation over repetitive manual work
* Documentation alongside implementation

Avoid adding complexity before it provides clear value.

## Development Workflow

All changes follow this workflow:

1. Start with a defined issue or lesson.
2. Create a branch from the latest `main`.
3. Make small, focused changes.
4. Validate the changes locally.
5. Commit with a clear message.
6. Push the branch to GitHub.
7. Open a Pull Request.
8. Address review feedback.
9. Merge only after the acceptance criteria are met.

Direct pushes to `main` are not allowed.

## Branch Naming

Use a branch name that communicates the type and purpose of the work.

```text
lesson/<number>-<short-description>
docs/<short-description>
fix/<short-description>
chore/<short-description>
```

Examples:

```text
lesson/01-python-project-setup
docs/update-architecture-overview
fix/health-check-response
chore/phase-1-repository-foundation
```

Use lowercase words separated by hyphens.

## Keeping a Branch Current

Before starting new work:

```bash
git switch main
git pull --ff-only
git switch -c <branch-name>
```

If the branch already exists:

```bash
git switch <branch-name>
```

Do not use force pushes unless there is a documented and reviewed reason.

## Commit Guidelines

Commits should be small, focused, and understandable.

Use this format:

```text
<type>: <short description>
```

Recommended types:

* `docs` — documentation changes
* `feat` — new application behavior
* `fix` — defect corrections
* `test` — test changes
* `refactor` — internal changes without new behavior
* `chore` — repository maintenance
* `ci` — continuous integration changes

Examples:

```text
docs: add AI collaboration guide
chore: add repository formatting rules
feat: add health check endpoint
fix: handle missing configuration value
```

Each commit should represent one meaningful change.

## Pull Request Expectations

Every lesson must end with a Pull Request.

A Pull Request should explain:

* What changed
* Why the change was needed
* How it was validated
* What was learned
* Which issue it addresses
* Whether documentation was updated

Keep Pull Requests small enough to review and understand.

Use a closing reference when the Pull Request completes an issue:

```text
Closes #1
```

## Review Feedback

Review feedback is part of the learning process.

When addressing feedback:

1. Understand why the change was requested.
2. Ask for clarification when the reasoning is unclear.
3. Make the smallest appropriate correction.
4. Respond with what changed.
5. Resolve the conversation after the concern is addressed.

Do not dismiss feedback only because the current implementation works.

## Documentation

Update documentation whenever a change affects:

* Architecture
* Development workflow
* Configuration
* Deployment
* Operations
* Troubleshooting
* Learning progress

Documentation must describe the repository as it currently exists. Future plans should be clearly identified as future work.

For phase implementation work:

* Relevant documentation must be reviewed before the implementation Pull Request is opened.
* Once implementation and validation acceptance criteria are satisfied, phase documentation must describe the phase as Complete before the implementation Pull Request is merged.
* `learning/progress.md` and `learning/roadmap.md` must identify the completed phase and the next phase before merge.
* The implementation Pull Request is the final documentation update for the phase.
* Do not use temporary statuses such as `In progress` or `PR pending` in final phase documentation merely because the implementation Pull Request has not yet merged.
* After merge, only verify the merge, issue closure, CI results, and branch cleanup.
* Do not create a separate post-merge documentation change solely to mark the phase complete.

## Validation

Before committing, review the changed files:

```bash
git diff
git diff --check
git status
```

Before opening a Pull Request, run all checks relevant to the current lesson locally.

For Python changes, the established validation commands are:

```bash
python3 -m pytest
python3 -m ruff format --check .
python3 -m ruff check .
```

GitHub Actions also runs automated Python, container, and Kubernetes validation as part of continuous integration.

Kubernetes CI creates an ephemeral kind cluster, applies the repository manifests, and validates Deployment readiness, Job completion, and Service access.

Local validation remains important because it provides faster feedback and makes CI failures easier to reproduce and troubleshoot.

## Definition of Done

A lesson or change is complete when:

* Acceptance criteria are met.
* The implementation works as intended.
* Relevant validation has passed.
* Documentation is current.
* The reasoning behind the solution is understood.
* The work has been reviewed through a Pull Request.
* The repository is left in a better state than before.
