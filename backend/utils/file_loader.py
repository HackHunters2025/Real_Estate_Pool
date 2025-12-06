# backend/utils/file_loader.py

import json
import csv

def load_json(file_path: str):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except Exception:
        return None


def load_csv(file_path: str):
    """
    Returns CSV numeric values or dicts depending on content.
    """
    try:
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            data = []
            for row in reader:
                # Convert numeric fields where possible
                converted = [float(x) if x.replace('.', '', 1).isdigit() else x for x in row]
                data.append(converted)
            return data
    except Exception:
        return None


def load_text(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return None
