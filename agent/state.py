from typing import TypedDict, List


class State(TypedDict):
    text: str
    kind: str
    entities: List[str]
    summary: str
