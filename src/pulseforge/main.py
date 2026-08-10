"""Command-line entry point for PulseForge."""

import argparse
import logging

from pulseforge.app import run
from pulseforge.logging import configure_logging
from pulseforge.service import serve

LOGGER = logging.getLogger(__name__)


def main(args: list[str] | None = None) -> None:
    """Start PulseForge using the requested execution mode."""
    configure_logging()

    parser = argparse.ArgumentParser(prog="pulseforge")
    parser.add_argument(
        "command",
        nargs="?",
        choices=["serve"],
    )
    parsed_args = parser.parse_args(args)

    if parsed_args.command == "serve":
        serve()
        return

    try:
        exit_code = run()
    except RuntimeError:
        LOGGER.exception("PulseForge encountered an expected runtime error.")
        exit_code = 1

    raise SystemExit(exit_code)