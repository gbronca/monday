from typing import Literal, TypedDict


class State(TypedDict):
    state: Literal["all", "active", "archived", "deleted"]
