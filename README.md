# PulseForge

PulseForge is a production-oriented learning project for developing practical skills in software engineering, Platform Engineering, DevOps, observability, and Site Reliability Engineering.

The project will grow incrementally from a small Python application into a containerized, observable service deployed to Kubernetes and supported by infrastructure as code and CI/CD automation.

The goal is not only to build a working application. Each phase is designed to develop an understanding of the engineering decisions, trade-offs, and operational practices behind the implementation.

## Current Status

PulseForge has completed **Phase 1: Repository Foundation**.

Phase 2, the Python application foundation, has not yet started.
The repository currently contains:

* A protected `main` branch workflow
* Contribution guidelines
* AI collaboration guidelines
* Initial architecture documentation
* A learning roadmap and progress tracker
* Pull Request and Issue templates
* Repository formatting and file-handling rules

PulseForge does not yet contain application code, containers, Kubernetes resources, Terraform configuration, or GitHub Actions workflows.

These capabilities will be introduced incrementally when they provide clear learning and engineering value.

## Learning Goals

PulseForge is designed to develop experience with:

* Python
* Testing and code quality
* Docker and containers
* Kubernetes
* Helm
* Terraform
* GitHub Actions
* CI/CD
* OpenTelemetry
* Elastic Stack
* Observability
* Platform Engineering
* DevOps
* Site Reliability Engineering

## Engineering Principles

The project follows these principles:

* Simplicity over cleverness
* Maintainability over shortcuts
* Small improvements over large rewrites
* Automation over repetitive manual work
* Documentation alongside implementation
* Production-quality practices without unnecessary complexity
* Understanding before automation
* Observability as part of system design

## Development Workflow

All project work follows this general workflow:

1. Define the lesson or change in a GitHub Issue.
2. Create a feature branch from the latest `main`.
3. Make small, focused changes.
4. Validate the changes locally.
5. Commit with clear and intentional messages.
6. Open a Pull Request.
7. Review the work against its acceptance criteria.
8. Merge through GitHub after the work is complete.

Direct pushes to `main` are not allowed.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the complete development workflow.

## Repository Guide

| Location                             | Purpose                                                                     |
| ------------------------------------ | --------------------------------------------------------------------------- |
| [`docs/`](docs/)                     | System architecture and technical documentation                             |
| [`learning/`](learning/)             | Learning roadmap, progress, and skill development                           |
| [`.github/`](.github/)               | Pull Request templates, Issue templates, and planned workflow documentation |
| [`AGENTS.md`](AGENTS.md)             | Instructions for AI assistants collaborating on the project                 |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution and development workflow                                       |
| [`LICENSE`](LICENSE)                 | Project license                                                             |

Application and infrastructure directories will be added when their corresponding phases begin.

## Architecture

The architecture will evolve incrementally as project requirements become clear.

The expected long-term direction includes:

```text
User or Client
      |
      v
PulseForge Application
      |
      v
OpenTelemetry Instrumentation
      |
      v
Telemetry Collection
      |
      v
Elastic Stack
```

The application is expected to run in Kubernetes, with deployment configuration packaged through Helm and infrastructure managed through Terraform.

These components represent future direction and have not yet been implemented.

See the [Architecture Overview](docs/architecture/overview.md) for more detail.

## Learning Roadmap

The planned progression includes:

1. Repository foundation
2. Python application foundation
3. Testing and code quality
4. Containerization
5. Continuous integration
6. Kubernetes fundamentals
7. Helm
8. Observability
9. Elastic Stack integration
10. Terraform
11. Continuous delivery
12. Reliability engineering

See the complete [Learning Roadmap](learning/roadmap.md).

## AI Collaboration

AI assistants are used as engineering mentors, architects, and reviewers.

They are expected to:

* Teach before generating code
* Explain trade-offs
* Work incrementally
* Respect the current lesson scope
* Avoid premature complexity
* Review existing files before recommending changes
* Keep documentation aligned with implementation

See [AGENTS.md](AGENTS.md) for the complete collaboration guide.

## License

PulseForge is available under the [MIT License](LICENSE).
