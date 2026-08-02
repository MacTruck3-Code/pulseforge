"""Command-line entry point for PulseForge."""

import logging

LOGGER = logging.getLogger(__name__)


def configure_logging() -> None:
    """Configure application logging."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )


def run() -> int:
    """Run the PulseForge application logic."""
    LOGGER.info("PulseForge status: operational")
    return 0


def main() -> None:
    """Start PulseForge and exit with the application status code."""
    configure_logging()

    try:
        exit_code = run()
    except RuntimeError:
        LOGGER.exception("PulseForge encountered an expected runtime error.")
        exit_code = 1

    raise SystemExit(exit_code)