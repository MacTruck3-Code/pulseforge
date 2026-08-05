"""Unit tests for the PulseForge application logic."""

import logging

import pytest

from pulseforge.app import run


def test_run_returns_success_exit_code() -> None:
    """Verify that the application returns a successful exit code."""
    exit_code = run()

    assert exit_code == 0


def test_run_logs_operational_status(
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Verify that the application logs its operational status."""
    caplog.set_level(logging.INFO, logger="pulseforge.app")

    run()

    assert "PulseForge status: operational" in caplog.text
