from pydantic import BaseModel
from typing import Literal

class FilterStep(BaseModel):
    columns: list[Literal[
        "sepal length (cm)", 
        "sepal width (cm)", 
        "petal length (cm)", 
        "petal width (cm)", 
        "species"
    ]]
    operator: Literal[">", "<", "==", "!=", ">=", "<="]
    value: str
