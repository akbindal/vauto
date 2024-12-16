# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentChatParams", "UserInput"]


class AgentChatParams(TypedDict, total=False):
    agent_type: Required[str]

    api_key: Required[str]

    context: Required[str]

    thread_id: Required[str]

    user_input: Required[UserInput]


class UserInput(TypedDict, total=False):
    content: Required[str]

    role: Required[str]
