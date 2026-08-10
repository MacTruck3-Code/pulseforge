"""HTTP service for PulseForge."""

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import uvicorn


async def readiness(request):
    """Report whether PulseForge is ready to serve requests."""
    return JSONResponse({"status": "ready"})


app = Starlette(
    routes=[
        Route("/health/ready", readiness),
    ]
)

def serve() -> None:
    """Run the PulseForge HTTP service."""
    uvicorn.run(
        "pulseforge.service:app",
        host="0.0.0.0",
        port=8080,
    )
