# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vautomate_sdk import VautomateSDK, AsyncVautomateSDK

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_chat(self, client: VautomateSDK) -> None:
        agent = client.agents.chat(
            agent_type="agent_type",
            api_key="api_key",
            context="context",
            thread_id="thread_id",
            user_input={
                "content": "content",
                "role": "role",
            },
        )
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    def test_raw_response_chat(self, client: VautomateSDK) -> None:
        response = client.agents.with_raw_response.chat(
            agent_type="agent_type",
            api_key="api_key",
            context="context",
            thread_id="thread_id",
            user_input={
                "content": "content",
                "role": "role",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    def test_streaming_response_chat(self, client: VautomateSDK) -> None:
        with client.agents.with_streaming_response.chat(
            agent_type="agent_type",
            api_key="api_key",
            context="context",
            thread_id="thread_id",
            user_input={
                "content": "content",
                "role": "role",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_chat(self, async_client: AsyncVautomateSDK) -> None:
        agent = await async_client.agents.chat(
            agent_type="agent_type",
            api_key="api_key",
            context="context",
            thread_id="thread_id",
            user_input={
                "content": "content",
                "role": "role",
            },
        )
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    async def test_raw_response_chat(self, async_client: AsyncVautomateSDK) -> None:
        response = await async_client.agents.with_raw_response.chat(
            agent_type="agent_type",
            api_key="api_key",
            context="context",
            thread_id="thread_id",
            user_input={
                "content": "content",
                "role": "role",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @parametrize
    async def test_streaming_response_chat(self, async_client: AsyncVautomateSDK) -> None:
        async with async_client.agents.with_streaming_response.chat(
            agent_type="agent_type",
            api_key="api_key",
            context="context",
            thread_id="thread_id",
            user_input={
                "content": "content",
                "role": "role",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True
