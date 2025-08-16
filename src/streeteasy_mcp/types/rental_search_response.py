# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RentalSearchResponse", "Listing", "Pagination"]


class Listing(BaseModel):
    id: str
    """Unique identifier for the listing"""

    latitude: float
    """Latitude coordinate of the property"""

    longitude: float
    """Longitude coordinate of the property"""

    price: int
    """Monthly rental price in USD"""

    status: Literal["open", "closed"]
    """Current status of the listing"""

    url: str
    """Direct link to the listing on StreetEasy"""


class Pagination(BaseModel):
    count: int
    """Total number of listings matching the search criteria"""

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)
    """Offset to use for the next page of results"""


class RentalSearchResponse(BaseModel):
    listings: List[Listing]
    """Array of rental listings"""

    pagination: Pagination
