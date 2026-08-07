# PulseForge Learning Roadmap

This roadmap describes the planned learning progression for PulseForge.

It is intentionally high-level. Individual lessons will be defined through GitHub Issues with clear objectives and acceptance criteria.

The roadmap may change as the project evolves and new learning needs become clear.

## Phase 1 — Repository Foundation

Focus:

* GitHub repository structure
* Protected branch workflow
* Issues and Pull Requests
* Documentation practices
* AI collaboration guidelines
* Repository hygiene

Outcome:

A professional repository foundation that supports incremental engineering work.

## Phase 2 — Python Application Foundation

Focus:

* Python project structure
* Dependency management
* Virtual environments
* Basic application behavior
* Configuration management
* Logging fundamentals
* Error handling

Outcome:

A small, maintainable Python application that runs locally.

## Phase 3 — Testing and Code Quality

Focus:

* Unit testing
* Test structure
* Formatting
* Linting
* Static analysis
* Local validation workflow

Outcome:

Application behavior can be validated consistently before changes are merged.

## Phase 4 — Containerization

Focus:

* Container fundamentals
* Dockerfiles
* Image layers
* Build context
* Container security basics
* Local container execution

Outcome:

The application can be built and run as a container.

## Phase 5 — Continuous Integration

Focus:

* GitHub Actions fundamentals
* Pull Request validation
* Automated tests
* Formatting and lint checks
* Container image builds
* Dependency and security scanning

Outcome:

Repository changes are validated automatically before merging.

## Phase 6 — Kubernetes Fundamentals

Focus:

* Kubernetes architecture
* Pods
* Deployments
* Services
* ConfigMaps
* Secrets
* Health probes
* Resource requests and limits
* Local Kubernetes development

Outcome:

The containerized application runs reliably in Kubernetes.

## Phase 7 — Helm

Focus:

* Helm chart structure
* Templates
* Values
* Environment-specific configuration
* Chart validation
* Release management

Outcome:

Kubernetes deployment configuration is packaged and reusable.

## Phase 8 — Observability

Focus:

* Logs, metrics, and traces
* OpenTelemetry concepts
* Application instrumentation
* OpenTelemetry Collector
* Context propagation
* Telemetry quality

Outcome:

The application exposes useful telemetry that explains its behavior.

## Phase 9 — Elastic Stack Integration

Focus:

* Telemetry ingestion
* Elasticsearch data organization
* Elastic Common Schema
* Kibana dashboards
* Alerting
* Troubleshooting workflows
* Retention and lifecycle considerations

Outcome:

Application and platform telemetry can be searched, visualized, and used for operational decisions.

## Phase 10 — Terraform

Focus:

* Terraform language fundamentals
* Providers and resources
* State
* Variables and outputs
* Modules
* Planning and applying changes
* Remote state considerations
* Infrastructure validation

Outcome:

Required infrastructure can be created and managed consistently as code.

## Phase 11 — Continuous Delivery

Focus:

* Artifact promotion
* Environment separation
* Deployment workflows
* Rollback strategies
* Release versioning
* Deployment validation
* GitOps concepts

Outcome:

Validated changes can move through environments using a controlled delivery process.

## Phase 12 — Reliability Engineering

Focus:

* Service Level Indicators
* Service Level Objectives
* Error budgets
* Capacity planning
* Failure testing
* Incident response
* Runbooks
* Operational readiness reviews

Outcome:

PulseForge can be operated as a reliable service rather than only deployed as an application.

## Ongoing Engineering Practices

The following practices apply throughout the roadmap:

* Small, reviewable changes
* Documentation alongside implementation
* Secure defaults
* Clear acceptance criteria
* Meaningful testing
* Architectural decision tracking
* Pull Request review
* Learning reflection
* Technical debt identification

## Roadmap Status

| Phase                                   | Status      |
| --------------------------------------- | ----------- |
| Phase 1 — Repository Foundation         | Complete    |
| Phase 2 — Python Application Foundation | Complete    |
| Phase 3 — Testing and Code Quality      | Complete    |
| Phase 4 — Containerization              | Complete    |
| Phase 5 — Continuous Integration        | Not started |
| Phase 6 — Kubernetes Fundamentals       | Not started |
| Phase 7 — Helm                          | Not started |
| Phase 8 — Observability                 | Not started |
| Phase 9 — Elastic Stack Integration     | Not started |
| Phase 10 — Terraform                    | Not started |
| Phase 11 — Continuous Delivery          | Not started |
| Phase 12 — Reliability Engineering      | Not started |
