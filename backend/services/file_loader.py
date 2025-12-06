import csv
import json
import os

def load_json_or_csv(file_path: str):
    """
    Utility function to load CSV or JSON file.
    Returns a list (for CSV) or dict (for JSON).
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".csv":
        return _load_csv(file_path)
    elif extension == ".json":
        return _load_json(file_path)
    else:
        raise ValueError("Unsupported file type. Only CSV or JSON allowed.")


def _load_csv(file_path: str):
    data = []
    with open(file_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def _load_json(file_path: str):
    with open(file_path, "r", encoding="utf-8") as jsonfile:
        return json.load(jsonfile)
