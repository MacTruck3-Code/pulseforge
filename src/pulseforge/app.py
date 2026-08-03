"""Core application logic for PulseForge."""

import logging

LOGGER = logging.getLogger(__name__)


def run() -> int:
    """Run the PulseForge application logic."""
    LOGGER.info("PulseForge status: operational")
    return 0
