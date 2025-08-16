# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import rental_search_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.rental_search_response import RentalSearchResponse

__all__ = ["RentalsResource", "AsyncRentalsResource"]


class RentalsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RentalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jasminepoon/se_mcp#accessing-raw-response-data-eg-headers
        """
        return RentalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RentalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jasminepoon/se_mcp#with_streaming_response
        """
        return RentalsResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        areas: str,
        amenities: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        max_beds: int | NotGiven = NOT_GIVEN,
        max_price: int | NotGiven = NOT_GIVEN,
        min_baths: float | NotGiven = NOT_GIVEN,
        min_beds: int | NotGiven = NOT_GIVEN,
        min_price: int | NotGiven = NOT_GIVEN,
        no_fee: bool | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        types: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RentalSearchResponse:
        """
        Find rentals that are currently listed for rent in specific NYC neighborhoods
        with various filter options

        Args:
          areas: The NYC areas and neighborhoods to filter for. Multiple areas can be provided as
              comma-separated values. See the full list of supported areas in the
              documentation.

          amenities: The amenities a property has. Provide as comma-separated values.

          limit: The number of records (page size) to return. Max value allowed is 500. Use
              offset field to paginate through all records.

          max_beds: The maximum number of beds of a property

          max_price: The maximum price of a property

          min_baths: The minimum number of baths of a property

          min_beds: The minimum number of beds of a property

          min_price: The minimum price of a property

          no_fee: Whether the rental unit has a broker fee

          offset: Offset to start fetching records from

          types: Comma separated list of property types to filter for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/rentals/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "areas": areas,
                        "amenities": amenities,
                        "limit": limit,
                        "max_beds": max_beds,
                        "max_price": max_price,
                        "min_baths": min_baths,
                        "min_beds": min_beds,
                        "min_price": min_price,
                        "no_fee": no_fee,
                        "offset": offset,
                        "types": types,
                    },
                    rental_search_params.RentalSearchParams,
                ),
            ),
            cast_to=RentalSearchResponse,
        )


class AsyncRentalsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRentalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jasminepoon/se_mcp#accessing-raw-response-data-eg-headers
        """
        return AsyncRentalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRentalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jasminepoon/se_mcp#with_streaming_response
        """
        return AsyncRentalsResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        areas: str,
        amenities: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        max_beds: int | NotGiven = NOT_GIVEN,
        max_price: int | NotGiven = NOT_GIVEN,
        min_baths: float | NotGiven = NOT_GIVEN,
        min_beds: int | NotGiven = NOT_GIVEN,
        min_price: int | NotGiven = NOT_GIVEN,
        no_fee: bool | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        types: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RentalSearchResponse:
        """
        Find rentals that are currently listed for rent in specific NYC neighborhoods
        with various filter options

        Args:
          areas: The NYC areas and neighborhoods to filter for. Multiple areas can be provided as
              comma-separated values. See the full list of supported areas in the
              documentation.

          amenities: The amenities a property has. Provide as comma-separated values.

          limit: The number of records (page size) to return. Max value allowed is 500. Use
              offset field to paginate through all records.

          max_beds: The maximum number of beds of a property

          max_price: The maximum price of a property

          min_baths: The minimum number of baths of a property

          min_beds: The minimum number of beds of a property

          min_price: The minimum price of a property

          no_fee: Whether the rental unit has a broker fee

          offset: Offset to start fetching records from

          types: Comma separated list of property types to filter for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/rentals/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "areas": areas,
                        "amenities": amenities,
                        "limit": limit,
                        "max_beds": max_beds,
                        "max_price": max_price,
                        "min_baths": min_baths,
                        "min_beds": min_beds,
                        "min_price": min_price,
                        "no_fee": no_fee,
                        "offset": offset,
                        "types": types,
                    },
                    rental_search_params.RentalSearchParams,
                ),
            ),
            cast_to=RentalSearchResponse,
        )


class RentalsResourceWithRawResponse:
    def __init__(self, rentals: RentalsResource) -> None:
        self._rentals = rentals

        self.search = to_raw_response_wrapper(
            rentals.search,
        )


class AsyncRentalsResourceWithRawResponse:
    def __init__(self, rentals: AsyncRentalsResource) -> None:
        self._rentals = rentals

        self.search = async_to_raw_response_wrapper(
            rentals.search,
        )


class RentalsResourceWithStreamingResponse:
    def __init__(self, rentals: RentalsResource) -> None:
        self._rentals = rentals

        self.search = to_streamed_response_wrapper(
            rentals.search,
        )


class AsyncRentalsResourceWithStreamingResponse:
    def __init__(self, rentals: AsyncRentalsResource) -> None:
        self._rentals = rentals

        self.search = async_to_streamed_response_wrapper(
            rentals.search,
        )
