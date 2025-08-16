# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from streeteasy_mcp import StreeteasyMcp, AsyncStreeteasyMcp
from streeteasy_mcp.types import RentalSearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRentals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: StreeteasyMcp) -> None:
        rental = client.rentals.search(
            areas="all-downtown,all-midtown",
        )
        assert_matches_type(RentalSearchResponse, rental, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: StreeteasyMcp) -> None:
        rental = client.rentals.search(
            areas="all-downtown,all-midtown",
            amenities="doorman,gym,laundry",
            limit=10,
            max_beds=10,
            max_price=4000,
            min_baths=1,
            min_beds=1,
            min_price=2000,
            no_fee=True,
            offset=0,
            types="apartment,condo",
        )
        assert_matches_type(RentalSearchResponse, rental, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: StreeteasyMcp) -> None:
        response = client.rentals.with_raw_response.search(
            areas="all-downtown,all-midtown",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rental = response.parse()
        assert_matches_type(RentalSearchResponse, rental, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: StreeteasyMcp) -> None:
        with client.rentals.with_streaming_response.search(
            areas="all-downtown,all-midtown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rental = response.parse()
            assert_matches_type(RentalSearchResponse, rental, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRentals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncStreeteasyMcp) -> None:
        rental = await async_client.rentals.search(
            areas="all-downtown,all-midtown",
        )
        assert_matches_type(RentalSearchResponse, rental, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncStreeteasyMcp) -> None:
        rental = await async_client.rentals.search(
            areas="all-downtown,all-midtown",
            amenities="doorman,gym,laundry",
            limit=10,
            max_beds=10,
            max_price=4000,
            min_baths=1,
            min_beds=1,
            min_price=2000,
            no_fee=True,
            offset=0,
            types="apartment,condo",
        )
        assert_matches_type(RentalSearchResponse, rental, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncStreeteasyMcp) -> None:
        response = await async_client.rentals.with_raw_response.search(
            areas="all-downtown,all-midtown",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rental = await response.parse()
        assert_matches_type(RentalSearchResponse, rental, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncStreeteasyMcp) -> None:
        async with async_client.rentals.with_streaming_response.search(
            areas="all-downtown,all-midtown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rental = await response.parse()
            assert_matches_type(RentalSearchResponse, rental, path=["response"])

        assert cast(Any, response.is_closed) is True
