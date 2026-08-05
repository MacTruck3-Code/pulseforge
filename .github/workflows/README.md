# GitHub Actions Workflows

This directory will contain GitHub Actions workflows for PulseForge.

No automated workflows are currently implemented.

PulseForge now has a Python application, pytest unit tests, and Ruff formatting and linting checks that run locally. GitHub Actions is intentionally deferred until **Phase 5: Continuous Integration**, after the application has been containerized and the local container workflow is understood.

Automation will be introduced only after the corresponding manual process is understood and can be performed successfully.

## Planned Workflows

### Markdown Validation

Purpose:

* Check Markdown formatting
* Detect broken internal links
* Identify common documentation issues

Add when:

* Documentation volume makes manual validation unreliable
* A Markdown validation tool has been selected and tested locally

### Python Validation

Current local validation:

* Run unit tests with pytest
* Check formatting with Ruff
* Run linting and static analysis with Ruff

Purpose:

* Run automated tests
* Check formatting
* Run linting
* Perform type checking

Add when:

* Phase 5: Continuous Integration begins
* The Phase 4 container workflow works locally
* The exact automated validation scope has been reviewed
* Any additional checks are first established locally

### Container Validation

Purpose:

* Build the application container image
* Validate the Dockerfile
* Scan the image for known vulnerabilities
* Confirm the container starts successfully

Add when:

* The application has been containerized
* The local container build is reliable

### Kubernetes Validation

Purpose:

* Validate Kubernetes manifests
* Check manifest formatting and structure
* Detect common configuration and security issues

Add when:

* Kubernetes manifests exist
* Local validation commands have been selected

### Helm Validation

Purpose:

* Lint the Helm chart
* Render templates
* Validate generated Kubernetes resources

Add when:

* A Helm chart exists
* The chart can be installed successfully in a development environment

### Terraform Validation

Purpose:

* Check formatting
* Initialize Terraform without applying changes
* Validate configuration
* Generate and review plans safely

Add when:

* Terraform configuration exists
* State and provider decisions have been documented

### Security Scanning

Purpose:

* Scan dependencies
* Detect exposed secrets
* Identify vulnerable container packages
* Review infrastructure configuration for security risks

Add when:

* The repository contains dependencies or deployable artifacts
* The selected scanning tools have been evaluated for usefulness and noise

### Continuous Delivery

Purpose:

* Publish versioned artifacts
* Promote validated changes
* Deploy to controlled environments
* Verify deployments
* Support rollback procedures

Add when:

* Continuous integration is reliable
* Environments and artifact storage exist
* The deployment process has been documented and tested manually

## Workflow Design Principles

Future workflows should:

* Perform one clear responsibility
* Use pinned or intentionally versioned actions
* Follow least-privilege permissions
* Avoid storing secrets in repository files
* Provide readable failure messages
* Run only when relevant files change
* Be reproducible locally when practical
* Be documented alongside implementation
* Avoid automating processes that are not yet understood

## Implementation Requirement

Before adding a workflow:

1. Define the problem it solves.
2. Establish the equivalent local validation process.
3. Document important security and maintenance considerations.
4. Implement the smallest useful workflow.
5. Verify its behavior through a Pull Request.
