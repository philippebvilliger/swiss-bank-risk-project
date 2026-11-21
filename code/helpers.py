from pathlib import Path
import pandas as pd


def get_project_root():
    cwd = Path.cwd()

    if cwd.name == "code":
        project_root = cwd.parent
    elif (cwd / "swiss-bank-risk-project").is_dir():
        project_root = cwd / "swiss-bank-risk-project"
    else:
        project_root = cwd

    return project_root


def load_raw_datasets(project_root):
    raw_data_folder = project_root.joinpath("data", "raw")
    raw_data_folder.mkdir(parents=True, exist_ok=True)

    # Adapted from https://stackoverflow.com/questions/56701311/accessing-csv-in-python-when-file-name-is-unknown
    # CC BY-SA 4.0
    csv_files = list(raw_data_folder.glob("*.csv"))

    datasets = {}

    for file in csv_files:
        datasets[file.stem] = pd.read_csv(file)

    return raw_data_folder, csv_files, datasets


def load_processed_data(project_root, filename):
    processed_data_folder = project_root.joinpath("data", "processed")
    data_file = processed_data_folder.joinpath(filename)

    dataframe = pd.read_csv(data_file, parse_dates=["date"])

    return processed_data_folder, data_file, dataframe