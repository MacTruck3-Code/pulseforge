# PulseForge

PulseForge is a production-oriented learning project for developing practical skills in software engineering, Platform Engineering, DevOps, observability, and Site Reliability Engineering.

The project will grow incrementally from a small Python application into a containerized, observable service deployed to Kubernetes and supported by infrastructure as code and CI/CD automation.

The goal is not only to build a working application. Each phase is designed to develop an understanding of the engineering decisions, trade-offs, and operational practices behind the implementation.

## Current Status

PulseForge has completed **Phase 6: Kubernetes Fundamentals**.

**Phase 7: Helm** is next.

The repository currently contains:

* A protected `main` branch workflow
* Contribution guidelines
* AI collaboration guidelines
* Architecture documentation
* A learning roadmap and progress tracker
* Pull Request and Issue templates
* Repository formatting and file-handling rules
* A Python command-line application
* A long-running HTTP service mode
* A readiness endpoint at `/health/ready`
* Automated unit tests with pytest
* Formatting and linting with Ruff
* A Docker container running as a dedicated non-root user
* Plain Kubernetes manifests for a Namespace, Job, Deployment, and Service
* A Kubernetes readiness probe
* Deliberate CPU and memory requests and limits
* Local Kubernetes development with kind
* GitHub Actions continuous integration
* Automated Python testing and code-quality validation
* Automated container build and runtime validation
* Automated Kubernetes integration validation with kind
* Informational container vulnerability scanning with Trivy

The existing `pulseforge` command remains a run-to-completion application suitable for Kubernetes Jobs.

The `pulseforge serve` command provides a long-running HTTP service suitable for a Kubernetes Deployment.

The Kubernetes Deployment is exposed internally through a ClusterIP Service and uses `/health/ready` as its readiness probe.

The continuous integration workflow validates Python, container, and Kubernetes behavior on GitHub-hosted runners.

Container images are built and validated during CI but are not published to a registry or deployed to an external environment.

ConfigMap and application Secret usage remain intentionally deferred because PulseForge does not yet have meaningful runtime configuration or application credentials that require them.

Helm, Terraform, OpenTelemetry, Elastic integration, container publishing, and continuous delivery have not yet been introduced.

These capabilities will continue to be introduced incrementally when they provide clear learning and engineering value.

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

## Local Development

PulseForge requires Python 3.12 or newer.

Create and select a project-local virtual environment using VS Code:

1. Open the Command Palette.
2. Run `Python: Create Environment`.
3. Choose `Venv`.
4. Name the environment `.venv`.
5. Select a supported Python interpreter.
6. Skip package installation when prompted.

Install PulseForge in editable mode from the repository root:

```bash
python3 -m pip install --editable ".[dev]"
```

Run the application:
```bash
pulseforge
```

A successful run produces a log message similar to:
```bash
INFO pulseforge.app: PulseForge status: operational
```

The command should exit with status code 0.

## Local Quality Checks

Run the unit tests:
```bash
python3 -m pytest
```

Check whether the Python files follow the configured formatting rules:

```bash
python3 -m ruff format --check .
```

Apply Ruff formatting when changes are required:
```bash
python3 -m ruff format .
```

Run static analysis and linting:
```bash
python3 -m ruff check .
```

Before opening a Pull Request, verify that tests, formatting, and linting all pass:
```bash
python3 -m pytest
python3 -m ruff format --check .
python3 -m ruff check .
```

## Local Container Workflow

PulseForge can be built and run locally as a Docker container.

The container uses an official Python 3.12 slim base image, installs PulseForge through its Python package configuration, and runs as a dedicated non-root user.

Build the Phase 6 image from the repository root:

```bash
docker build --tag pulseforge:phase6 .
```

Run the original command-line mode:
```bash
docker run --rm pulseforge:phase6
```

A successful run produces a log message similar to:
```bash
INFO pulseforge.app: PulseForge status: operational
```
The container should exit with status code `0`.

Run the long-running HTTP service:
```bash
docker run --rm \
  --publish 8080:8080 \
  pulseforge:phase6 serve
```

Verify the readiness endpoint:
```bash
curl http://127.0.0.1:8080/health/ready
```

A successful response is:
```json
{"status":"ready"}
```

Verify that the container runs as a non-root user:
```bash
docker run --rm \
  --entrypoint id \
  pulseforge:phase6
```
The reported UID must not be `0`.

GitHub Actions automates container image builds, runtime validation, non-root user verification, and informational vulnerability scanning with Trivy.

The same container image supports both Kubernetes workload models introduced in Phase 6:
* `pulseforge` for finite Job execution.
* `pulseforge serve` for the long-running Deployment.

## Repository Guide

| Location                             | Purpose                                                                     |
| ------------------------------------ | --------------------------------------------------------------------------- |
| [`docs/`](docs/)                     | System architecture and technical documentation                             |
| [`learning/`](learning/)             | Learning roadmap, progress, and skill development                           |
| [`.github/`](.github/)               | Pull Request templates, Issue templates, and GitHub Actions workflows       |
| [`AGENTS.md`](AGENTS.md)             | Instructions for AI assistants collaborating on the project                 |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution and development workflow                                       |
| [`LICENSE`](LICENSE)                 | Project license                                                             |
| [`src/pulseforge/`](src/pulseforge/) | Python application package                                                  |
| [`tests/`](tests/)                   | Automated unit tests                                                        |
| [`k8s/`](k8s/)                       | Plain Kubernetes manifests for local deployment and validation              |

Containerization uses the root-level `Dockerfile` and `.dockerignore`.

Kubernetes deployment configuration is stored under `k8s/` as plain manifests.

Additional deployment and infrastructure directories will be added only when their corresponding phases provide a clear need.

## Architecture

PulseForge currently supports both finite command execution and long-running service execution.

```text
                    +----------------------+
                    |   PulseForge Image   |
                    +----------+-----------+
                               |
                 +-------------+-------------+
                 |                           |
                 v                           v
        Kubernetes Job               Kubernetes Deployment
          pulseforge                   pulseforge serve
                                             |
                                             v
                                      ClusterIP Service
                                             |
                                             v
                                      /health/ready
```

Local Kubernetes development uses kind and plain manifests stored under `k8s/`.

GitHub Actions independently validates:
* Python behavior and code quality
* Container build and runtime behavior
* Kubernetes Job, Deployment, and Service behavior in an ephemeral kind cluster

The Kubernetes layer intentionally remains small. Helm, Terraform, OpenTelemetry, Elastic integration, container publishing, and Continuous Delivery are deferred to later phases.

The next architectural expansion is Phase 7: Helm, where the existing plain Kubernetes manifests will provide the baseline for learning reusable deployment packaging and configuration.

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
