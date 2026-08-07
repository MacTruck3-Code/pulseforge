# GitHub Actions Workflows

This directory contains GitHub Actions workflows for PulseForge.

**Phase 5: Continuous Integration** is currently in progress.

The `Continuous Integration` workflow automates validation that was first established locally. It currently validates Python code quality and behavior, builds and runs the PulseForge container image, verifies important container runtime expectations, and reports HIGH and CRITICAL container vulnerabilities with Trivy.

The workflow uses GitHub-hosted runners, least-privilege repository permissions, SHA-pinned actions, and caching where it has demonstrated practical value.

Security vulnerability findings are currently informational and do not fail the workflow while the findings, severity model, and appropriate future gating policy are being evaluated.

## Workflow Triggers

The `Continuous Integration` workflow currently runs:

* On pushes to repository branches.
* On pull requests targeting `main`.

The broad push trigger is being retained temporarily while Phase 5 is under active development so workflow changes can be validated before a Pull Request exists.

Once Pull Request execution has been proven, the push trigger will be narrowed to `main` to avoid running the same validation twice for commits pushed to an open Pull Request.

Pull Request validation is the primary CI protection point because changes to the protected `main` branch are expected to arrive through reviewed Pull Requests.

## Workflow Security

The workflow follows least-privilege principles.

Repository permissions are explicitly limited to:

```yaml
permissions:
  contents: read
```

The jobs only need permission to read repository contents. They do not publish packages, modify repository files, create releases, deploy applications, or require deployment credentials.

External GitHub Actions are pinned to full commit SHAs rather than floating version tags. Version comments are retained beside the SHA so the intended release remains understandable.

SHA pinning prevents an action reference from silently changing between workflow runs. Updating an action therefore becomes an explicit, reviewable repository change.

Additional permissions should only be introduced when a workflow step has a demonstrated requirement for them.

## Troubleshooting Workflow Failures

GitHub Actions failures should be investigated from the most specific level outward:

```text
Workflow
   ↓
Failed job
   ↓
Failed step
   ↓
Command output
   ↓
Root cause
```

Start by identifying which job failed:

* `Python validation` for tests, formatting, linting, or Python setup.
* `Container validation` for image builds, runtime behavior, non-root validation, or vulnerability scanning.

Then open the failed step and review the command output.

Whenever practical, reproduce the failing command locally before changing the workflow. The CI commands intentionally match established local validation commands so failures can be investigated without relying exclusively on the GitHub Actions environment.

A successful workflow confirms that the automated checks passed. It does not prove that the application is free from every possible defect or security issue.

## Caching Decisions

Caching is used selectively rather than enabled for every workflow dependency.

Current decisions:

* **Trivy caching is enabled** because repeated runs showed that Trivy otherwise downloads a large vulnerability database and installs its tooling on each clean runner.
* **Python dependency caching is deferred** because PulseForge currently has few development dependencies and installation remains fast.
* **Docker layer caching is deferred** because the container image is small and builds remain fast.

A cache improves performance by reusing previously downloaded or generated data. It does not replace dependency installation, validation, or reproducible build configuration.

Caching should be introduced when measured workflow cost justifies the additional configuration and maintenance.

## Validation Areas

### Markdown Validation

Purpose:

* Check Markdown formatting
* Detect broken internal links
* Identify common documentation issues

Add when:

* Documentation volume makes manual validation unreliable
* A Markdown validation tool has been selected and tested locally

### Python Validation

The workflow validates Python code using the same commands established locally:

* Run unit tests with pytest.
* Check formatting with Ruff.
* Run linting and static analysis with Ruff.

The job:

* Runs on a GitHub-hosted Ubuntu runner.
* Uses Python 3.12 to match the project runtime target.
* Installs the project with development dependencies.
* Fails when tests, formatting, or linting checks fail.
* Uses SHA-pinned GitHub Actions.
* Does not currently use pip dependency caching because dependency installation is still small and fast.

This keeps local and CI validation aligned so developers can reproduce failures before pushing changes.

### Container Validation

The workflow validates the PulseForge container using the same core behaviors established during Phase 4.

The job:

* Builds the image as `pulseforge:ci`.
* Runs the container and verifies the expected `PulseForge status: operational` output.
* Fails if the container exits unsuccessfully or the expected output is missing.
* Verifies the runtime process uses a non-root user.
* Scans the image with Trivy for HIGH and CRITICAL operating-system and library vulnerabilities.
* Reports vulnerability findings without failing CI while an appropriate future security-gating policy is evaluated.
* Uses Trivy caching because repeated runs demonstrated meaningful download and setup overhead.
* Does not currently use Docker layer caching because container builds remain small and fast.
* Does not publish the image to a container registry.

This validates the deployable artifact without introducing continuous delivery or deployment responsibilities.

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

Phase 5 evaluated several security scanning categories:

* Dependency scanning for vulnerable application dependencies.
* Secret scanning for accidentally committed credentials.
* Static analysis for potentially unsafe source-code patterns.
* Container vulnerability scanning for known vulnerabilities in the built image.

Container vulnerability scanning was selected as the first automated security check because the container image is PulseForge's current deployable artifact.

Trivy currently scans the built image for HIGH and CRITICAL operating-system and library vulnerabilities.

The scan is intentionally informational:

* Findings are visible in GitHub Actions logs.
* Vulnerabilities do not currently fail the workflow.
* Findings are reviewed before deciding whether future severity-based gating is appropriate.
* Overlapping security scanners are not being added without a demonstrated need.

Initial scans found vulnerabilities inherited from the Python Debian base image while reporting no vulnerabilities in the PulseForge Python package itself.

Additional security scanning may be introduced later when repository complexity or risk justifies it.

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
