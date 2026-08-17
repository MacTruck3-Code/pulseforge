# PulseForge Architecture Overview

## Purpose

PulseForge is a production-oriented learning project designed to develop practical skills in software engineering, Platform Engineering, DevOps, observability, and Site Reliability Engineering.

The architecture will grow incrementally as each new technology provides clear value to the project.

This document describes the current architectural direction. Planned components are not considered implemented until they exist in the repository and have been validated.

## Current Architecture State

PulseForge now includes a local Kubernetes deployment foundation.

The current system consists of:

```text
Python Application
      ↓
Docker Image
      ↓
Local Kubernetes with kind
      ├─ Job
      │   └─ pulseforge
      │      → run-to-completion CLI
      │
      └─ Deployment
          └─ pulseforge serve
             ↓
          Service
             ↓
        /health/ready
```

GitHub Actions validates the same major layers independently:

```text
GitHub Actions CI
      ├─ Python validation
      ├─ Container validation
      └─ Kubernetes validation with kind
```

The existing `pulseforge` command remains a run-to-completion process and is used with a Kubernetes Job.

The `pulseforge serve` command provides a legitimate long-running HTTP process for the Kubernetes Deployment.

The Deployment is exposed internally through a ClusterIP Service.

The Deployment uses `/health/ready` as a readiness probe so Pods receive Service traffic only when the application is ready.

Initial CPU and memory requests and limits are configured based on observed local resource usage. These values are learning-oriented defaults rather than production capacity targets.

ConfigMap and application Secret usage remain deferred because PulseForge does not yet have meaningful non-sensitive runtime configuration or application credentials that require them.

The CI workflow builds the application image, creates an ephemeral kind cluster, loads the local image into the cluster, applies the Kubernetes manifests, and validates the Deployment, Job, and Service behavior.

Container images are not published to a registry, and Continuous Delivery has not been introduced.

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

PulseForge now also provides a minimal HTTP service using Starlette and Uvicorn.

The `pulseforge serve` execution mode runs the ASGI service while the original `pulseforge` command preserves the existing run-to-completion CLI behavior.

The service currently exposes only `/health/ready`, keeping the HTTP surface intentionally small until additional application behavior provides a reason to expand it.

A broader application feature set and domain model have not yet been selected.

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

Container image publishing and registry selection remain deferred.

Phase 6 extended the containerized application into local Kubernetes, using the same image for the run-to-completion Job and long-running Deployment modes.

### Kubernetes — Implemented

PulseForge runs locally on Kubernetes using kind and plain YAML manifests stored under `k8s/`.

The Kubernetes implementation includes:

* A dedicated `pulseforge` Namespace.
* A Job for the original run-to-completion `pulseforge` command.
* A Deployment for the long-running `pulseforge serve` process.
* A ClusterIP Service that selects the Deployment Pods.
* A readiness probe using `/health/ready`.
* CPU and memory requests and limits.

The Deployment uses Kubernetes reconciliation rather than application-level keepalive behavior. When a managed Pod is deleted, the ReplicaSet creates a replacement to restore the desired state.

Readiness determines whether a Pod should receive Service traffic. A failed readiness probe does not restart the container; it removes the unready Pod from eligible Service endpoints.

A liveness probe is intentionally not configured because PulseForge does not yet have a meaningful failure condition that requires Kubernetes to restart an otherwise running process.

ConfigMaps and application Secrets are also intentionally deferred until real runtime configuration or credentials exist.

Local images are loaded directly into the kind cluster during development and CI. A container registry, external Kubernetes environment, and Continuous Delivery remain deferred.

### Helm

Helm will be introduced when repeated configuration or environment-specific customization makes plain Kubernetes manifests difficult to maintain.

### Infrastructure as Code

Terraform will be introduced after a clear infrastructure target has been selected.

### Observability

OpenTelemetry will be used to generate and collect telemetry such as logs, metrics, and traces.

Elastic Stack will be used to store, explore, visualize, and alert on relevant telemetry.

### Continuous Integration and Delivery

GitHub Actions provides the current continuous integration layer for PulseForge.

Continuous integration runs established validation automatically on GitHub-hosted runners. The workflow uses separate Python, container, and Kubernetes validation jobs so failures remain focused and understandable.

Current CI responsibilities include:

* Unit testing with pytest.
* Ruff formatting validation.
* Ruff linting and static analysis.
* Container image builds.
* Container runtime behavior validation.
* Non-root runtime verification.
* Informational Trivy vulnerability scanning.
* Creation of an ephemeral kind cluster.
* Loading the locally built PulseForge image into kind.
* Applying the Kubernetes manifests.
* Verifying the Deployment reaches its ready state.
* Verifying the Job completes successfully.
* Verifying the ClusterIP Service reaches `/health/ready`.
* Collecting Kubernetes workload, Event, description, and log diagnostics when validation fails.

The workflow follows least-privilege repository permissions and pins external GitHub Actions to immutable commit SHAs.

The kind and kubectl binaries used by Kubernetes validation are also pinned to explicit versions and verified before use.

Continuous delivery has not yet been implemented.

PulseForge does not currently publish container images, deploy to an external Kubernetes environment, promote artifacts between environments, or require deployment credentials. Those responsibilities remain deferred until later phases.

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

PulseForge now runs locally in Kubernetes using plain manifests.

Future phases will package the Kubernetes configuration with Helm, introduce infrastructure management with Terraform when a clear target exists, and add OpenTelemetry and Elastic Stack integration for observability.

This diagram represents the intended future observability context.

The PulseForge application, container image, and local Kubernetes deployment exist today.

OpenTelemetry instrumentation, telemetry collection, Elastic integration, Terraform-managed infrastructure, Helm packaging, container publishing, and Continuous Delivery have not yet been implemented.

## Deferred Decisions

The following decisions are intentionally deferred:

* Broader application features and domain model
* Cloud provider or infrastructure platform
* Container registry
* Helm chart structure
* Terraform backend
* OpenTelemetry Collector topology
* Elastic deployment model
* Container image publishing and versioning strategy
* External Kubernetes environment
* Continuous Delivery strategy
* Production capacity and resource sizing

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
