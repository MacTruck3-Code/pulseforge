"""OpenTelemetry configuration for PulseForge."""

from opentelemetry import metrics, trace
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)
from opentelemetry.sdk.resources import SERVICE_NAME, SERVICE_VERSION, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

_RESOURCE = Resource.create(
    {
        SERVICE_NAME: "pulseforge",
        SERVICE_VERSION: "0.1.0",
    }
)


def configure_tracing() -> None:
    """Configure development tracing for PulseForge."""
    provider = TracerProvider(resource=_RESOURCE)
    provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))

    trace.set_tracer_provider(provider)


def configure_metrics() -> None:
    """Configure development metrics for PulseForge."""
    reader = PeriodicExportingMetricReader(
        ConsoleMetricExporter(),
        export_interval_millis=5000,
    )
    provider = MeterProvider(
        resource=_RESOURCE,
        metric_readers=[reader],
    )

    metrics.set_meter_provider(provider)