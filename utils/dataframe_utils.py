import pandas as pd

def apply_filters(df, filters):
    for step in filters:
        operator = step.operator
        if operator == "=":
            operator = "=="
        for column in step.columns:
            if operator == ">":
                df = df[df[column] > float(step.value)]
            elif operator == "<":
                df = df[df[column] < float(step.value)]
            elif operator == ">=":
                df = df[df[column] >= float(step.value)]
            elif operator == "<=":
                df = df[df[column] <= float(step.value)]
            elif operator == "==":
                df = df[df[column] == step.value]
            elif operator == "!=":
                df = df[df[column] != step.value]
    return df
