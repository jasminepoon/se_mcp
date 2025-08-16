# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RentalSearchParams"]


class RentalSearchParams(TypedDict, total=False):
    areas: Required[str]
    """The NYC areas and neighborhoods to filter for.

    Multiple areas can be provided as comma-separated values. See the full list of
    supported areas in the documentation.
    """

    amenities: str
    """The amenities a property has. Provide as comma-separated values."""

    limit: int
    """The number of records (page size) to return.

    Max value allowed is 500. Use offset field to paginate through all records.
    """

    max_beds: Annotated[int, PropertyInfo(alias="maxBeds")]
    """The maximum number of beds of a property"""

    max_price: Annotated[int, PropertyInfo(alias="maxPrice")]
    """The maximum price of a property"""

    min_baths: Annotated[float, PropertyInfo(alias="minBaths")]
    """The minimum number of baths of a property"""

    min_beds: Annotated[int, PropertyInfo(alias="minBeds")]
    """The minimum number of beds of a property"""

    min_price: Annotated[int, PropertyInfo(alias="minPrice")]
    """The minimum price of a property"""

    no_fee: Annotated[bool, PropertyInfo(alias="noFee")]
    """Whether the rental unit has a broker fee"""

    offset: int
    """Offset to start fetching records from"""

    types: str
    """Comma separated list of property types to filter for"""
