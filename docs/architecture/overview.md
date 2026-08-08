# PulseForge Architecture Overview

## Purpose

PulseForge is a production-oriented learning project designed to develop practical skills in software engineering, Platform Engineering, DevOps, observability, and Site Reliability Engineering.

The architecture will grow incrementally as each new technology provides clear value to the project.

This document describes the current architectural direction. Planned components are not considered implemented until they exist in the repository and have been validated.

## Current Architecture State

PulseForge has completed its continuous integration foundation.

The current system consists of:

```text
Python Application
      ↓
Docker Image
      ↓
GitHub Actions CI
      ├─ Python validation
      └─ Container validation
```

GitHub Actions now validates application behavior, formatting, linting, container builds, container runtime behavior, non-root execution, and container vulnerabilities.

The CI workflow validates artifacts but does not publish or deploy them.

Kubernetes deployment is the next architectural expansion in Phase 6.

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

These checks can be run locally before changes are pushed and are also executed automatically by GitHub Actions during continuous integration.

Keeping the local and CI commands aligned makes failures easier to reproduce and troubleshoot.

### Containerization — Implemented

PulseForge can be built as a Docker image using an official Python 3.12 slim base image.

The image installs PulseForge through its existing Python package configuration and uses the installed `pulseforge` command as the container process.

The runtime process executes as a dedicated non-root user.

Development tools such as pytest and Ruff are not installed in the runtime image.

Container builds and runtime behavior can be validated locally and are also validated automatically through GitHub Actions.

Continuous integration verifies:

* The image builds successfully.
* The application produces the expected operational output.
* The container exits successfully.
* The runtime process does not execute as root.
* HIGH and CRITICAL operating-system and library vulnerabilities are reported by Trivy.

Vulnerability findings are currently informational rather than merge-blocking.

Container image publishing and registry selection remain deferred. Kubernetes deployment begins in Phase 6 after the continuous integration foundation is complete.

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

GitHub Actions provides the current continuous integration layer for PulseForge.

Continuous integration runs established validation automatically on GitHub-hosted runners. The workflow includes separate Python and container validation jobs so failures remain focused and understandable.

Current CI responsibilities include:

* Unit testing with pytest.
* Ruff formatting validation.
* Ruff linting and static analysis.
* Container image builds.
* Container runtime behavior validation.
* Non-root runtime verification.
* Informational Trivy vulnerability scanning.

The workflow follows least-privilege repository permissions and pins external GitHub Actions to immutable commit SHAs.

Continuous delivery has not yet been implemented.

PulseForge does not currently publish container images, deploy applications, promote artifacts between environments, or require deployment credentials. Those responsibilities remain deferred until later phases.


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
* Container image publishing and versioning strategy

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
