from pydantic import BaseModel
from .filter_step import FilterStep

class FilterResponse(BaseModel):
    filters: list[FilterStep]
