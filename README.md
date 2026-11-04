# Swiss Bank Risk Project

This project assesses whether changes in euro-area financial stress, measured by the ECB Composite Indicator of Systemic Stress (CISS) help predict unusual widening in Swiss commercial-bank bond spreads over the following four weeks. It compares three logistic regression models using different variables and a decision tree using weekly ECB and SNB data and evaluates their out-of-sample predictive performance.

## Installation

pip install -r requirements.txt

## Run order

Run the notebooks in this order:

1. code/01_get_data.ipynb
2. code/02_clean.ipynb
3. code/03_explore.ipynb
4. code/04_features.ipynb
5. code/05_model.ipynb
6. code/06_figures.ipynb

## Runtime and output

The full project should take a few minutes to run on a standard computer. It produces cleaned and processed weekly data, model evaluation results as well as the final figures used in the report.

## Data sources

The data comes from official European Central Bank (ECB) and Swiss National Bank (SNB) sources. The project uses the ECB CISS index, the CHF/EUR exchange rate, the SNB policy rate and Swiss commercial-bank and government bond yields.