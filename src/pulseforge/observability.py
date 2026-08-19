"""OpenTelemetry configuration for PulseForge."""

from opentelemetry import metrics, trace
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import SERVICE_NAME, SERVICE_VERSION, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

_RESOURCE = Resource.create(
    {
        SERVICE_NAME: "pulseforge",
        SERVICE_VERSION: "0.1.0",
    }
)


def configure_tracing() -> None:
    """Configure tracing export for PulseForge."""
    provider = TracerProvider(resource=_RESOURCE)
    provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))

    trace.set_tracer_provider(provider)


def configure_metrics() -> None:
    """Configure metrics export for PulseForge."""
    reader = PeriodicExportingMetricReader(
        OTLPMetricExporter(),
        export_interval_millis=5000,
    )
    provider = MeterProvider(
        resource=_RESOURCE,
        metric_readers=[reader],
    )

    metrics.set_meter_provider(provider)
