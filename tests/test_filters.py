import pandas as pd
from models.filter_step import FilterStep
from utils.dataframe_utils import apply_filters

def test_filtering():
    data = {
        "sepal length (cm)": [5.1, 4.9, 4.7],
        "sepal width (cm)": [3.5, 3.0, 3.2],
        "petal length (cm)": [1.4, 1.4, 1.3],
        "petal width (cm)": [0.2, 0.2, 0.2],
        "species": ["setosa", "setosa", "setosa"],
    }
    df = pd.DataFrame(data)

    filters = [
        FilterStep(columns=["sepal length (cm)"], operator=">", value="4.8"),
    ]

    filtered_df = apply_filters(df, filters)
    assert len(filtered_df) == 2  # Check expected number of rows
