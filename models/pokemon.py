from pydantic import BaseModel


class Pokemon(BaseModel):
    id: int
    name: dict
    type: list[str]
    base: dict
    region: str


