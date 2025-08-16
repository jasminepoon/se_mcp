from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `se_mcp_2.resources` module.

    This is used so that we can lazily import `se_mcp_2.resources` only when
    needed *and* so that users can just import `se_mcp_2` and reference `se_mcp_2.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("se_mcp_2.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
