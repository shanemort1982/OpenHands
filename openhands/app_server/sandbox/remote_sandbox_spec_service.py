from typing import AsyncGenerator

from fastapi import Request
from pydantic import Field

from openhands.app_server.sandbox.preset_sandbox_spec_service import (
    PresetSandboxSpecService,
)
from openhands.app_server.sandbox.sandbox_spec_models import (
    SandboxSpecInfo,
)
from openhands.app_server.sandbox.sandbox_spec_service import (
    SandboxSpecService,
    SandboxSpecServiceInjector,
    get_agent_server_env,
    get_agent_server_image,
)
from openhands.app_server.services.injector import InjectorState


def get_default_sandbox_specs():
    import os

    # Support v0.62-style workspace mounting where /workspace contains all projects
    # instead of v1.0-style /workspace/project/ isolation
    working_dir = os.environ.get('SANDBOX_WORKING_DIR', '/workspace/project')
    return [
        SandboxSpecInfo(
            id=get_agent_server_image(),
            command=['/usr/local/bin/openhands-agent-server', '--port', '60000'],
            initial_env={
                'OPENVSCODE_SERVER_ROOT': '/openhands/.openvscode-server',
                'LOG_JSON': 'true',
                'OH_ENABLE_VNC': '0',
                'OH_CONVERSATIONS_PATH': '/workspace/conversations',
                'OH_BASH_EVENTS_DIR': '/workspace/bash_events',
                'OH_VSCODE_PORT': '60001',
                **get_agent_server_env(),
            },
            working_dir=working_dir,
        )
    ]


class RemoteSandboxSpecServiceInjector(SandboxSpecServiceInjector):
    specs: list[SandboxSpecInfo] = Field(
        default_factory=get_default_sandbox_specs,
        description='Preset list of sandbox specs',
    )

    async def inject(
        self, state: InjectorState, request: Request | None = None
    ) -> AsyncGenerator[SandboxSpecService, None]:
        yield PresetSandboxSpecService(self.specs)
