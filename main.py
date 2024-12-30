from pydantic import BaseModel
from openai import OpenAI
import pandas as pd
from sklearn.datasets import load_iris
from models.filter_response import FilterResponse

# Initialize OpenAI client
client = OpenAI(api_key='your_openai_api_key_here')

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Debugging: Check dataset structure
print("Initial DataFrame:")
print(df.head())

# Define user query
user_query = """Filter for flowers with a sepal length under 6 but wide sepals (above 3.5 in width) and exclude species that are virginica. Additionally, select only those with petal lengths less than 4.5"""

# Send query to the LLM
completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "You are a data assistant. Respond with structured filters for the following dataset."},
        {"role": "user", "content": user_query},
    ],
    response_format=FilterResponse,
)


# Parse the response
message = completion.choices[0].message
if not message.parsed:
    print("Invalid query or model refusal.")
else:
    filters = message.parsed.filters

    # Debugging: Check parsed filters
    print("Parsed Filters from LLM:")
    for filter_step in filters:
        print(filter_step)

    # Apply filters to the DataFrame
    species_filters = []
    for step in filters:
        print(f"Applying Filter: {step}")
        try:
            operator = step.operator
            if operator == "=":
                operator = "=="

            # Apply filter to each column in the `columns` list
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
                else:
                    print(f"Unsupported operator: {operator}")
            print("Filtered DataFrame:")
            print(df)
        except Exception as e:
            print(f"Error applying filter {step}: {e}")


    # Combine species filters as OR condition
    if species_filters:
        print(f"Applying combined species filter: {species_filters}")
        df = df[df["species"].isin(species_filters)]

        # Debugging: Show DataFrame after applying species filters
        print("Filtered DataFrame after species filter:")
        print(df)

# Final filtered DataFrame
print("Final Filtered DataFrame:")
print(df)
