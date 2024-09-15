# Covid-19 Symptoms Model

## Overview

The `covid19_model.ipynb` Jupyter Notebook is designed to simulate and analyze Covid-19 symptoms data. It generates random data for symptoms including fever, cold, shivering, and weight loss, categorizes some of the symptoms into discrete levels, and provides functionality to sort and save the data based on a selected parameter.

## Features

- **Data Generation**: Creates a dataset of 100 records with random values for symptoms:
  - Fever (in the range 80-120)
  - Cold (0-100)
  - Shivering (0-100)
  - Weight Loss (0-100)
- **Categorization**: Converts 'Cold' and 'Shivering' into categorical data with labels:
  - 'no'
  - 'low'
  - 'medium'
  - 'high'
  - 'very high'
- **Sorting**: Sorts the data based on a user-selected parameter.
- **Results Storage**: Saves the sorted dataset to an Excel file (`result.xlsx`).

## Files

- `covid19_model.ipynb`: Jupyter Notebook containing the code to generate, categorize, sort, and save the Covid-19 symptoms data.
- `result.xlsx`: Excel file where the sorted dataset is stored.

## Notebook Overview

1. **Data Generation**:
   - Generates random values for symptoms:
     - Fever
     - Cold
     - Shivering
     - Weight Loss
   - Creates a DataFrame with these values.

2. **Categorization**:
   - Converts the 'Cold' and 'Shivering' columns into categorical data using predefined bins and labels.

3. **Sorting**:
   - Prompts the user to enter a parameter for sorting.
   - Sorts the DataFrame based on the selected parameter.

4. **Saving Results**:
   - Saves the sorted DataFrame to `result.xlsx`.

## Usage

1. **Open the Notebook**:
    - Start Jupyter Notebook:
    ```bash
    jupyter notebook covid19_model.ipynb
    ```
    - Open the notebook file from the Jupyter interface.

2. **Run the Cells**:
    - Execute each cell in the notebook. Ensure to run the cell that prompts for the parameter input.

3. **Enter the Parameter**:
    - When prompted, enter one of the following parameters to sort the data:
      - `Fever`
      - `Cold`
      - `Shivering`
      - `Weight Loss`

4. **Output**:
    - **Excel File**: The `result.xlsx` file will contain the dataset sorted by the chosen parameter.

## Example Output

The `result.xlsx` file will include the sorted dataset with columns:
