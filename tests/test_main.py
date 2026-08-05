"""Unit tests for PulseForge startup behavior."""

from unittest.mock import patch

import pytest

from pulseforge.main import main


def test_main_exits_with_application_exit_code() -> None:
    """Verify that main exits with the code returned by the application."""
    with (
        patch("pulseforge.main.configure_logging"),
        patch("pulseforge.main.run", return_value=7),
        pytest.raises(SystemExit) as exit_info,
    ):
        main()

    assert exit_info.value.code == 7


def test_main_exits_with_failure_when_runtime_error_occurs() -> None:
    """Verify that expected runtime errors produce a failure exit code."""
    with (
        patch("pulseforge.main.configure_logging"),
        patch(
            "pulseforge.main.run",
            side_effect=RuntimeError("test failure"),
        ),
        pytest.raises(SystemExit) as exit_info,
    ):
        main()

    assert exit_info.value.code == 1
