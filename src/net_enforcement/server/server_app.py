from __future__ import annotations

from rich.console import Console


from typing import TYPE_CHECKING



class ServerApp:
    def __init__(self, console: Console) -> None:
        self.console = console

    async def run_server(self) -> None:
        pass