"""Command-line entry point for PulseForge."""

import logging

from pulseforge.app import run
from pulseforge.logging import configure_logging

LOGGER = logging.getLogger(__name__)


def main() -> None:
    """Start PulseForge and exit with the application status code."""
    configure_logging()

    try:
        exit_code = run()
    except RuntimeError:
        LOGGER.exception("PulseForge encountered an expected runtime error.")
        exit_code = 1

    raise SystemExit(exit_code)
