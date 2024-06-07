# workspace_demo
copilot workspace

## Olympic Gold Medals Analysis Notebook

The `Olympic_Gold_Medals_Analysis.ipynb` notebook is designed to count gold medals per country by Olympic year. This Jupyter Notebook includes sections for data loading, data cleaning, analysis, and visualizations to effectively display the results. To use this notebook, simply load it in a Jupyter environment and follow the instructions provided within the notebook for analysis.

### Running the Notebook

To run the `Olympic_Gold_Medals_Analysis.ipynb` notebook, you will need a Jupyter environment. Ensure you have Python installed, preferably version 3.8 or above. The following libraries are required:
- Pandas
- Matplotlib
- Seaborn

You can install these libraries using pip:
```
pip install pandas matplotlib seaborn
```

After installing the necessary libraries, open the notebook in your Jupyter environment and follow the step-by-step instructions provided within the notebook for data analysis and visualization.

### Import Data

The notebook utilizes a sample dataset of Olympic gold medals for analysis. The dataset is in CSV format and contains information about the year, country, and number of gold medals won. Ensure to download the dataset and place it in the same directory as the notebook for seamless data loading and analysis.

To import the dataset into the notebook, use the following code snippet:
```python
import pandas as pd

data = pd.read_csv('olympic_gold_medals.csv')
```

This will load the dataset into a Pandas DataFrame, ready for analysis.

## Daily Affirmations Application

The Daily Affirmations Application is designed to automatically post a new affirmation daily, helping users start their day with positive thoughts. This application sources affirmations from a predefined list and posts them at a specified time each day.

### Setting Up and Running the Application

To set up and run the Daily Affirmations Application, you will need Python installed, preferably version 3.8 or above. The application requires the following dependencies:
- requests
- schedule

You can install these dependencies using pip:
```
pip install requests schedule
```

After installing the necessary dependencies, run the application by executing the `daily_affirmations_app.py` script in your terminal:
```
python daily_affirmations_app.py
```

This will initiate the application, and it will automatically post a daily affirmation at the specified time.

## Deploying to GitHub Pages

The project is now successfully deployed to GitHub Pages. You can access the project at the following URL: [https://bekahwhittle.github.io/workspace_demo/](https://bekahwhittle.github.io/workspace_demo/).

A `gh-pages` branch has been created to host the static content, including the `index.html` file which serves as the entry point for the GitHub Pages site. This setup allows for the easy sharing and demonstration of the project's features.
