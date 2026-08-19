"""OpenTelemetry configuration for PulseForge."""

from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, SERVICE_VERSION, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor


def configure_tracing() -> None:
    """Configure development tracing for PulseForge."""
    resource = Resource.create(
        {
            SERVICE_NAME: "pulseforge",
            SERVICE_VERSION: "0.1.0",
        }
    )

    provider = TracerProvider(resource=resource)
    provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))

    trace.set_tracer_provider(provider)
