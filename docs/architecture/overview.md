# PulseForge Architecture Overview

## Purpose

PulseForge is a production-oriented learning project designed to develop practical skills in software engineering, Platform Engineering, DevOps, observability, and Site Reliability Engineering.

The architecture will grow incrementally as each new technology provides clear value to the project.

This document describes the current architectural direction. Planned components are not considered implemented until they exist in the repository and have been validated.

## Current State

PulseForge has completed **Phase 3: Testing and Code Quality**.

**Phase 4: Containerization** is next.

The repository currently contains:

* Project, architecture, and learning documentation
* Contribution and AI collaboration guidelines
* A protected-branch development workflow
* A Python 3.12 or newer command-line application under `src/pulseforge/`
* Project metadata and development dependencies in `pyproject.toml`
* Unit tests under `tests/`
* Local testing, formatting, and linting with pytest and Ruff

PulseForge does not yet contain a container image, Kubernetes resources, Helm charts, Terraform configuration, OpenTelemetry instrumentation, Elastic integration, or automated GitHub Actions workflows.

## Architectural Principles

PulseForge follows these principles:

### Simplicity

Choose the smallest implementation that solves the current problem.

Avoid adding platforms, services, or abstractions before they are needed.

### Incremental Development

Build the system in small, reviewable lessons.

Each lesson should introduce a limited number of concepts and leave the repository in a working state.

### Maintainability

Prefer readable code, documented decisions, predictable structure, and clear ownership over clever solutions.

### Automation

Automate repetitive and error-prone work when the manual process is understood and automation provides measurable value.

### Observability

Applications and infrastructure should eventually expose enough telemetry to understand their behavior, performance, and failures.

Observability will be introduced incrementally rather than added as an afterthought.

### Production-Oriented Learning

Implementations should reflect professional engineering practices while remaining appropriate for the current learning stage.

The project should not imitate production complexity without a clear reason.

## Planned Architectural Evolution

PulseForge is expected to evolve through several stages.

### Application Foundation — Implemented

PulseForge includes a small Python command-line application.

The application can run through the installed `pulseforge` command or with `python3 -m pulseforge`.

Application logic, logging configuration, and process startup are separated into focused modules.

A web framework, broader feature set, and domain model have not yet been selected.

### Testing and Code Quality — Implemented

PulseForge uses pytest for focused unit testing.

Ruff provides automated formatting, linting, import-order validation, and basic static analysis.

These checks currently run locally before a Pull Request is opened. Automated execution through GitHub Actions is planned for Phase 5.

### Containerization

The application will be packaged as a container after it functions locally and has basic automated tests.

### Kubernetes

The containerized application will be deployed to Kubernetes using the smallest useful set of manifests.

### Helm

Helm will be introduced when repeated configuration or environment-specific customization makes plain Kubernetes manifests difficult to maintain.

### Infrastructure as Code

Terraform will be introduced after a clear infrastructure target has been selected.

### Observability

OpenTelemetry will be used to generate and collect telemetry such as logs, metrics, and traces.

Elastic Stack will be used to store, explore, visualize, and alert on relevant telemetry.

### Continuous Integration and Delivery

GitHub Actions will automate validation and delivery processes after those processes have first been established and understood locally.

## Expected Future System Context

The eventual system may contain:

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

The application may later run in Kubernetes, with infrastructure managed through Terraform and application deployment packaged through Helm.

This diagram represents the intended future system context. The PulseForge application exists today, while OpenTelemetry instrumentation, telemetry collection, Elastic integration, and the supporting deployment infrastructure have not yet been implemented.

## Deferred Decisions

The following decisions are intentionally deferred:

* Python application framework
* Application features and domain model
* Local Kubernetes distribution
* Cloud provider or infrastructure platform
* Container registry
* Kubernetes deployment topology
* Helm chart structure
* Terraform backend
* OpenTelemetry Collector topology
* Elastic deployment model
* CI/CD workflow design

These decisions will be made when the project has enough requirements to evaluate meaningful trade-offs.

## Documentation Maintenance

This document should be updated whenever a lesson changes:

* System boundaries
* Major components
* Data flows
* Deployment architecture
* Observability architecture
* Infrastructure ownership
* Important architectural constraints

Meaningful architectural decisions should eventually be recorded as Architecture Decision Records.
