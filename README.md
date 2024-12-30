
# Data Transformation Assistant

This project demonstrates a two-layered approach for processing and transforming data using a pandas DataFrame. The layers include:
1. A set of predefined commands for data transformation (e.g., filtering by predicates).
2. An AI-powered chat interface that interprets user queries into structured data transformation commands and applies them.

## Features
- **AI-Driven Filtering**: Use natural language queries to filter and transform a dataset.
- **Structured Transformation**: AI generates a sequence of structured filters, ensuring correctness and precision.
- **Support for Complex Queries**: The assistant can process multiple conditions, including logical combinations (`AND`/`OR`).
- **Customizable Queries**: Supports filtering by sepal/petal length and width, and species inclusion/exclusion.

## Dataset
The project uses the Iris dataset, a classic dataset for pattern recognition:
- Sepal Length (`sepal length (cm)`)
- Sepal Width (`sepal width (cm)`)
- Petal Length (`petal length (cm)`)
- Petal Width (`petal width (cm)`)
- Species (`setosa`, `versicolor`, `virginica`)

## How It Works
1. **Input a Query**: Provide a natural language query, such as:
   ```plaintext
   Filter for flowers with a sepal length under 6 but wide sepals (above 3.5 in width) and exclude species that are virginica. Additionally, select only those with petal lengths less than 4.5.
   ```
2. **AI Parses the Query**: The AI generates a structured sequence of filtering commands using the `FilterStep` model. Supported filtering options include:
   - **Numerical Filters**: Compare sepal/petal length and width using `<`, `>`, `<=`, `>=`, `==`, or `!=`.
   - **Categorical Filters**: Include or exclude one or multiple species.
3. **Filters Applied**: The commands are applied to the Iris dataset step-by-step, with intermediate results output to the command line for transparency.
4. **Final Output**: The final filtered DataFrame is displayed in the command line.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/data-transformation-assistant.git
   cd data-transformation-assistant
   ```
2. Set up a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # For Unix
   venv\Scripts\activate      # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Set Your OpenAI API Key in `main.py`**:
   Locate the `client` initialization in `main.py` and replace `'your_openai_api_key_here'` with your OpenAI API key:
   ```python
   client = OpenAI(api_key='your_openai_api_key_here')

2. **Set Your Query in `main.py`**:
   Locate the `user_query` variable in `main.py` and set it to your desired query. The default query is:
   ```python
   user_query = "Filter for flowers with a sepal length under 6 but wide sepals (above 3.5 in width) and exclude species that are virginica. Additionally, select only those with petal lengths less than 4.5."
   ```
3. **Run the Application**:
   Execute the script:
   ```bash
   python main.py
   ```
5. **View Results**:
   The script will:
   - Display intermediate filtered DataFrames after each filtering step.
   - Output the final filtered DataFrame in the command line.

## Project Structure
- **`main.py`**: Entry point for the application.
- **`commands/`**: Contains predefined transformation commands.
  - `filter.py`: Implements the filtering logic.
- **`ai_interface/`**: Interfaces with the AI to parse user queries.
- **`tests/`**: Unit tests for validating components.
- **`data/`**: Placeholder for additional datasets (optional).

## Example Queries
1. **Numerical Filters**:
   ```plaintext
   Filter for flowers with sepal length < 6, sepal width > 3.5, and petal length <= 4.5.
   ```
2. **Categorical Filters**:
   ```plaintext
   Filter for species setosa and versicolor only.
   ```
3. **Combined Filters**:
   ```plaintext
   Filter for flowers where species is virginica or versicolor, petal width >= 2.0, and sepal width < 3.0.
   ```

## Limitations
- Currently supports only filtering operations.
- Limited to the Iris dataset by default but can be extended to other datasets.

## Future Improvements
- Add support for column selection.
- Extend to additional operations such as sorting and grouping.
- Integrate visualizations (e.g., matplotlib).

## Contributions
Contributions are welcome! Fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
