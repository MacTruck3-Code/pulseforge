# PulseForge Learning Progress

This file records meaningful learning outcomes from the PulseForge project.

It is not intended to be a daily activity log. Entries should capture completed milestones, important engineering decisions, challenges, and concepts that need further practice.

## Current Status

| Area | Status |
|---|---|
| Most recently completed phase | Phase 3 — Testing and Code Quality |
| Completion issue | #5 — Establish testing and code quality |
| Completion Pull Request | #6 — Establish testing and code quality |
| Phase status | Complete |
| Next phase | Phase 4 — Containerization |

## Phase 1 — Repository Foundation

### Completed

* Created the public PulseForge GitHub repository.
* Selected the MIT License.
* Protected the `main` branch with a GitHub ruleset.
* Created Issue #1 to define the Phase 1 scope and acceptance criteria.
* Established a feature-branch workflow.
* Added AI collaboration guidance.
* Added contribution guidelines.
* Added the initial architecture overview.
* Added documentation and learning indexes.
* Added the high-level learning roadmap.

### Concepts Reinforced

* The default branch should represent reviewed and approved work.
* Issues provide traceability between planned work and implementation.
* Feature branches isolate changes from the stable branch.
* Pull Requests are both a review mechanism and a learning record.
* Documentation should distinguish current implementation from future plans.
* Architecture should evolve incrementally as requirements become clear.
* System documentation and learning records serve different purposes.

### Decisions Made

* PulseForge will use `main` as the protected default branch.
* Every lesson will be completed through a Pull Request.
* The repository will use the MIT License.
* CI workflows will not be added until there are meaningful checks to automate.
* Application and infrastructure directories will be added only when their lessons begin.
* AI assistants must prioritize teaching and review before code generation.

### Areas to Reinforce

* Writing focused commit messages.
* Reviewing changes before committing.
* Connecting Pull Requests to issues.
* Evaluating Pull Requests against acceptance criteria.
* Keeping documentation accurate as the repository changes.

## Phase 2 — Python Application Foundation

### Completed

* Created Issue #3 to define the Phase 2 scope and acceptance criteria.
* Created a Python project using a `src` directory layout.
* Added project metadata and package configuration with `pyproject.toml`.
* Created a project-local Python virtual environment using VS Code.
* Added an installable `pulseforge` command-line entry point.
* Added support for running PulseForge with `python3 -m pulseforge`.
* Added standard-library logging, type hints, and explicit exit codes.
* Separated application logic, logging configuration, and startup handling into focused modules.
* Documented local installation and execution steps.
* Validated the application through both supported execution paths.

### Concepts Reinforced

* A module is a Python file, while a package groups related modules.
* A `src` layout helps prevent accidental imports directly from the repository root.
* `pyproject.toml` provides project metadata, build configuration, package discovery, and command-line entry points.
* A virtual environment isolates project packages from the system Python environment.
* Editable installation makes source changes immediately available without reinstalling after every edit.
* `__main__.py` enables a package to run with `python3 -m pulseforge`.
* Logging is more appropriate than `print()` for application operational messages.
* Explicit exit codes communicate success or failure to calling processes.
* Refactoring should improve structure without changing external behavior.

### Decisions Made

* PulseForge supports Python 3.12 or newer.
* The application uses a `src` directory layout.
* Setuptools is used as the initial build backend.
* Runtime dependencies remain empty for the initial application foundation.
* Python’s standard logging library is used instead of a third-party logging package.
* Application logic, logging configuration, and process startup are kept in separate modules.
* Package version duplication is temporarily accepted to avoid premature version-management tooling.

### Challenges

* The initial editable installation stopped resolving the package correctly.
* Recreating the virtual environment provided a cleaner solution than introducing path workarounds.
* A pushed commit message was corrected safely by amending the commit and using force push with lease.
* Pull Request review identified outdated documentation and missing final newlines.

### Areas to Reinforce

* Understanding Python packaging and editable installations.
* Distinguishing application errors from unexpected programming errors.
* Writing maintainable Python modules as application behavior grows.
* Reviewing documentation against actual application output.
* Adding automated tests before expanding application behavior.

## Phase 3 — Testing and Code Quality

### Completed

* Created Issue #5 to define the Phase 3 scope and acceptance criteria.
* Added pytest as a development dependency.
* Configured pytest discovery through `pyproject.toml`.
* Created a focused unit-test structure under `tests/`.
* Added unit tests for application behavior and startup handling.
* Used pytest fixtures to capture application log records.
* Used standard-library mocking to isolate startup dependencies and error paths.
* Added Ruff for automated formatting and linting.
* Configured Ruff through `pyproject.toml`.
* Documented the local testing and quality-check workflow.

### Concepts Reinforced

* Unit tests validate small pieces of behavior in isolation.
* The testing pyramid favors a larger number of fast unit tests and fewer expensive higher-level tests.
* pytest discovers tests through predictable file and function naming conventions.
* Test names should describe the behavior being verified.
* Tests should be independent and should not rely on execution order.
* Fixtures provide temporary support and controlled state for tests.
* `patch()` temporarily replaces a dependency where the code under test looks it up.
* `return_value` controls what a mock returns.
* `side_effect` can make a mock raise a controlled exception.
* Formatters standardize code layout automatically.
* Linters identify potential code-quality problems.
* Tests, formatting, and linting solve different engineering problems.

### Decisions Made

* pytest is used as the unit-testing framework.
* Tests use a flat `tests/` directory while the application remains small.
* pytest configuration is stored in `pyproject.toml`.
* The `src` directory is explicitly included in pytest’s import path.
* Ruff is used for both formatting and linting.
* Ruff’s default lint rules are extended with import-order checks.
* Testability improvements will not be made unless existing code boundaries require them.
* Coverage enforcement, pre-commit hooks, and CI automation remain deferred.

### Challenges

* The existing editable virtual-environment installation initially failed to resolve the PulseForge package.
* pytest required an explicit `src` import path in the project configuration.
* The first logging test failed because INFO-level records were filtered by the default logging level.
* The test was corrected by configuring the `caplog` fixture for the application logger.
* Ruff exposed an incorrect TOML table boundary in `pyproject.toml`.

### Areas to Reinforce

* Distinguishing unit tests from integration and end-to-end tests.
* Identifying the single behavior that each test should verify.
* Understanding where dependencies must be patched.
* Choosing when mocking improves isolation and when it adds unnecessary complexity.
* Reviewing formatter changes separately from behavioral changes.
* Running all quality checks before opening a Pull Request.

## Future Entries

Add a new section after each completed phase or major lesson.

Each entry should answer:

* What was completed?
* What problem did the work solve?
* What engineering concepts were learned?
* What decisions were made?
* What was difficult?
* What should be practiced again?
