from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `streeteasy_mcp.resources` module.

    This is used so that we can lazily import `streeteasy_mcp.resources` only when
    needed *and* so that users can just import `streeteasy_mcp` and reference `streeteasy_mcp.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("streeteasy_mcp.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
