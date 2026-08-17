# PulseForge Learning Progress

This file records meaningful learning outcomes from the PulseForge project.

It is not intended to be a daily activity log. Entries should capture completed milestones, important engineering decisions, challenges, and concepts that need further practice.

## Current Status

| Area | Status |
|---|---|
| Most recently completed phase | Phase 6 — Kubernetes Fundamentals |
| Completion issue | #16 — Establish Kubernetes fundamentals |
| Completion Pull Request | #17 — Establish Kubernetes fundamentals |
| Phase status | Complete |
| Next phase | Phase 7 — Helm |

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

## Phase 4 — Containerization

### Completed

* Created Issue #10 to define the Phase 4 scope and acceptance criteria.
* Established a Linux-based Docker development environment on a remote Ubuntu VM.
* Added a Dockerfile using the official Python 3.12 slim base image.
* Added a `.dockerignore` to exclude local development artifacts from the Docker build context.
* Installed PulseForge into the image through its existing `pyproject.toml` package configuration.
* Configured the installed `pulseforge` command as the container entry point.
* Created a dedicated non-root user for the runtime process.
* Verified the container emits the expected operational log and exits with status code `0`.
* Verified the runtime process uses a nonzero UID and GID.
* Inspected image layers and final image contents.
* Confirmed pytest and Ruff validation still pass in the local development environment.
* Verified pytest and Ruff are not installed in the runtime image.
* Practiced creating, running, stopping, and removing a container while preserving the reusable image.
* Confirmed that setting PulseForge's `ENTRYPOINT` resets the inherited base-image `CMD`.
* Completed final documentation and Pull Request review before merging PR #11.
* Merged PR #11, which closed Issue #10 and completed Phase 4.

### Concepts Reinforced

* A container image is an immutable template used to create running containers.
* A Dockerfile describes how an image is constructed one instruction at a time.
* Dockerfile instructions contribute filesystem layers or image metadata.
* The Docker build context determines which local files are available to the build.
* `.dockerignore` reduces unnecessary build context and helps prevent local development artifacts from entering builds.
* Build-time requirements and runtime requirements should be treated separately.
* Installing PulseForge as a package validates the same packaging model used outside the container.
* `ENTRYPOINT` defines the primary container executable, while `CMD` can provide default arguments or commands.
* Exec-form process instructions avoid an unnecessary shell and provide better signal handling.
* Containers should use the least privilege required by the application.
* A named non-root user can be verified both through image metadata and the runtime numeric UID.
* Image inspection and container execution validate different aspects of the artifact.
* Images persist independently from individual containers created from them.
* Stopping a container does not remove it; `docker rm` removes a stopped container, while `docker run --rm` automates cleanup after exit.
* Docker build cache can reuse unchanged layers and significantly reduce rebuild work.

### Decisions Made

* PulseForge uses the official `python:3.12-slim` base image for Phase 4.
* The Python minor version is pinned while immutable digest pinning is deferred.
* Development dependencies such as pytest and Ruff are not installed in the runtime image.
* PulseForge is installed through `pyproject.toml` rather than executed directly from the copied source tree.
* The runtime process uses a dedicated `pulseforge` system user.
* The image uses exec-form `ENTRYPOINT ["pulseforge"]`.
* Setting PulseForge's `ENTRYPOINT` resets the base image's inherited `CMD`, so no additional `CMD` instruction is required.
* Tests remain part of local validation rather than the runtime image.
* Multi-stage builds are deferred because they do not currently provide enough value to justify the additional complexity.
* Container builds and execution remained local only during Phase 4; automation is deferred to Phase 5.

### Areas to Reinforce

* Understanding how Docker build cache invalidation changes as runtime dependencies are added.
* Distinguishing build context contents from final image contents.
* Understanding `ENTRYPOINT` and `CMD` interaction with command-line arguments.
* Evaluating when stronger image pinning provides enough value to justify maintenance overhead.
* Automating the established manual validation workflow during Phase 5.

## Phase 5 — Continuous Integration

### Completed

* Created Issue #13 to define the Phase 5 scope and acceptance criteria.
* Added a GitHub Actions workflow for continuous integration.
* Added separate Python and container validation jobs.
* Automated pytest, Ruff formatting, and Ruff linting checks on GitHub-hosted runners.
* Automated Docker image builds and container runtime validation.
* Verified the container emits the expected operational status and runs as a non-root user.
* Added Trivy container vulnerability scanning for HIGH and CRITICAL operating-system and library findings.
* Kept vulnerability scanning informational while scanner findings and future gating policy are evaluated.
* Applied least-privilege workflow permissions with read-only repository access.
* Disabled persisted checkout credentials because later workflow steps do not require authenticated Git access.
* Pinned external GitHub Actions to immutable commit SHAs.
* Evaluated dependency and Docker caching and enabled only Trivy caching where repeated overhead demonstrated clear value.
* Configured CI to validate Pull Requests targeting `main` and pushes to `main`.
* Verified Pull Request CI through PR #14.
* Verified the post-merge `main` workflow after PR #14 was merged.
* Completed Phase 5 implementation through PR #14, which closed Issue #13.

### Concepts Reinforced

* Continuous Integration independently validates repository changes in a clean environment.
* Local validation and CI validation complement each other rather than replacing one another.
* A GitHub Actions workflow contains jobs, jobs contain steps, and reusable actions can perform individual operations.
* GitHub-hosted runners provide temporary clean execution environments.
* Pull Request workflows validate proposed changes before merge.
* Push-to-`main` workflows validate the integrated repository state after merge.
* Separate jobs make failures easier to identify and troubleshoot.
* Workflow permissions should follow least privilege.
* Persisted credentials should be avoided when later workflow steps do not require them.
* Pinning actions to commit SHAs reduces supply-chain risk by preventing references from changing silently.
* Caching should solve a measured performance problem rather than be added automatically.
* Container vulnerability findings require context before they become merge-blocking policy.
* Security severity does not automatically indicate exploitability or ownership.
* Continuous Integration validates changes; Continuous Delivery publishes, promotes, or deploys them.

### Decisions Made

* CI uses Python 3.12 as the primary validation version rather than introducing a compatibility matrix prematurely.
* Python and container validation remain separate jobs.
* Feature-branch pushes do not trigger CI directly.
* Pull Requests targeting `main` provide the primary pre-merge validation.
* Pushes to `main` validate the integrated repository state.
* External GitHub Actions are pinned to immutable commit SHAs.
* Workflow permissions are limited to `contents: read`.
* Checkout credentials are not persisted.
* Python dependency caching is deferred while dependency installation remains fast.
* Docker layer caching is deferred while image builds remain small and fast.
* Trivy caching is enabled because repeated runs demonstrated meaningful download and setup overhead.
* Trivy vulnerability findings remain informational rather than merge-blocking.
* Additional overlapping security scanners are deferred until they provide demonstrated value.
* Container publishing and Continuous Delivery remain deferred to later phases.
* Required CI status checks in branch protection are deferred until repository governance changes are deliberately evaluated.

### Challenges

* Early workflow iterations produced duplicate validation from feature-branch pushes and Pull Request events.
* Trigger behavior was refined to avoid unnecessary duplicate runs.
* Initial Trivy execution included behavior outside the intended vulnerability-only scope and was narrowed deliberately.
* Trivy identified vulnerabilities inherited from the base image, reinforcing the need to distinguish application findings from upstream dependency findings.
* Workflow security and caching choices required balancing stronger controls against unnecessary maintenance complexity.

### Areas to Reinforce

* Troubleshooting more complex GitHub Actions failures.
* Maintaining SHA-pinned action versions safely over time.
* Deciding when CI checks should become required branch-protection rules.
* Defining a practical vulnerability remediation and exception policy.
* Evaluating when dependency or Docker caching becomes worthwhile.
* Understanding how Kubernetes validation should integrate into CI during Phase 6.



## Phase 6 — Kubernetes Fundamentals

### Completed

* Created Issue #16 to define the Phase 6 scope and acceptance criteria.
* Selected kind as the local Kubernetes environment after evaluating the learning goals and trade-offs.
* Created a dedicated `pulseforge` Namespace.
* Deployed the existing run-to-completion CLI as a Kubernetes Job and verified successful completion, logs, and exit behavior.
* Added a minimal long-running HTTP service using Starlette and Uvicorn while preserving the original `pulseforge` CLI behavior.
* Added `/health/ready` as the application readiness endpoint.
* Deployed the long-running service through a Kubernetes Deployment.
* Added a ClusterIP Service to expose the Deployment internally.
* Observed the Deployment, ReplicaSet, and Pod ownership relationship.
* Verified Kubernetes reconciliation by deleting a managed Pod and observing its automatic replacement.
* Added and validated a Kubernetes readiness probe.
* Deliberately caused a readiness failure and used Pod state, Events, and EndpointSlices to troubleshoot the failure.
* Confirmed that an unready Pod remains running but is removed from eligible Service endpoints.
* Evaluated liveness probes and intentionally deferred one because PulseForge does not yet have a meaningful liveness failure condition.
* Measured container resource usage and added initial CPU and memory requests and limits.
* Observed the Pod Quality of Service class change from BestEffort to Burstable.
* Evaluated ConfigMaps and Secrets and intentionally deferred application-specific resources because no meaningful runtime configuration or credentials currently exist.
* Inspected Kubernetes projected service-account data without exposing the service-account token.
* Practiced Kubernetes troubleshooting with `kubectl get`, `kubectl describe`, Events, logs, EndpointSlices, and container runtime statistics.
* Added Kubernetes integration validation to GitHub Actions using an ephemeral kind cluster.
* Configured CI to build and load the local image, apply the Kubernetes manifests, validate Deployment readiness, validate Job completion, validate Service access, and collect diagnostics on failure.
* Pinned kind and kubectl versions used by Kubernetes CI.
* Confirmed the existing pytest and Ruff validation remains healthy with six passing tests.

### Concepts Reinforced

* Kubernetes separates desired state from the controllers responsible for maintaining that state.
* A Pod is the basic workload execution unit, while higher-level controllers manage Pod lifecycle.
* A Deployment manages ReplicaSets, and ReplicaSets maintain the requested number of Pods.
* Kubernetes reconciliation continuously works to restore declared desired state.
* Jobs are appropriate for finite run-to-completion workloads.
* Deployments are appropriate for processes intended to remain running.
* Application behavior should determine the Kubernetes workload type rather than changing application behavior to satisfy a controller.
* A Service provides stable network access to selected Pods even as individual Pod identities change.
* Labels and selectors connect Kubernetes resources without directly coupling them by Pod name.
* Readiness answers whether a Pod should receive traffic.
* A readiness failure does not imply that a container should be restarted.
* Health probes should represent meaningful application behavior rather than exist only to satisfy a checklist.
* Resource requests influence scheduling and resource guarantees, while limits constrain maximum resource consumption.
* Kubernetes configuration should be introduced only when the application has real configuration to externalize.
* Secrets require careful handling even when an application does not yet require application-specific credentials.
* `Running` and `Ready` represent different workload states.
* Kubernetes Events, descriptions, logs, and endpoint information provide complementary troubleshooting evidence.
* Local Kubernetes integration testing can catch configuration and runtime problems that Python and container tests cannot detect.

### Decisions Made

* kind is the local Kubernetes environment for the current learning stage.
* Plain Kubernetes manifests are used before introducing Helm.
* The original `pulseforge` command remains a run-to-completion CLI and runs as a Kubernetes Job.
* `pulseforge serve` provides the legitimate long-running process used by the Deployment.
* Starlette and Uvicorn provide the smallest useful HTTP service foundation for the current requirements.
* The Kubernetes Service uses the default ClusterIP type because external exposure is not yet required.
* `/health/ready` is used as the readiness probe.
* A liveness probe is deferred until PulseForge has a meaningful failure condition that requires restart behavior.
* Initial resource requests are `10m` CPU and `32Mi` memory.
* Initial resource limits are `250m` CPU and `128Mi` memory.
* Current resource values are learning-oriented baselines rather than production capacity targets.
* Application ConfigMaps and Secrets are deferred until real configuration or credentials exist.
* Kubernetes CI uses kind so local and automated integration validation share the same basic cluster model.
* Kubernetes CI rebuilds the image independently rather than sharing artifacts between GitHub Actions jobs.
* Container publishing, external deployment, and Continuous Delivery remain deferred.
* Helm remains deferred to Phase 7.

### Challenges

* The initial Kubernetes environment required understanding Docker permissions, kubeconfig contexts, and the relationship between kind and containerd.
* The existing CLI exited successfully by design, which made it unsuitable for direct use in a Deployment.
* Adding a long-running service required preserving existing CLI compatibility rather than replacing the original execution model.
* A deliberately broken readiness path demonstrated that a Pod can be Running while remaining unready.
* Service routing required understanding how selectors and EndpointSlices connect stable Services to changing Pods.
* Resource settings required distinguishing measured local behavior from production sizing assumptions.
* Kubernetes CI required balancing useful integration coverage against unnecessary deployment and registry complexity.

### Areas to Reinforce

* Reading Kubernetes object status and Events during less controlled failures.
* Understanding scheduler behavior when resource requests compete for limited capacity.
* Distinguishing readiness, liveness, and startup probes as application behavior becomes more complex.
* Working with ConfigMaps and Secrets when genuine runtime configuration is introduced.
* Understanding Kubernetes identity, ServiceAccounts, and RBAC when the application needs Kubernetes API access.
* Diagnosing Service networking and DNS problems.
* Maintaining Kubernetes CI as manifests evolve.
* Understanding when plain manifests become repetitive enough to justify Helm.

## Future Entries

Add a new section after each completed phase or major lesson.

Each entry should answer:

* What was completed?
* What problem did the work solve?
* What engineering concepts were learned?
* What decisions were made?
* What was difficult?
* What should be practiced again?
