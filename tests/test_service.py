"""Tests for the PulseForge HTTP service."""

from starlette.testclient import TestClient

from pulseforge.service import app


def test_readiness_endpoint() -> None:
    """Readiness endpoint reports that PulseForge is ready."""
    client = TestClient(app)

    response = client.get("/health/ready")

    assert response.status_code == 200
    assert response.json() == {"status": "ready"}
