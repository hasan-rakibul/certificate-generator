import csv
from typing import Dict, List
import pandas as pd

def readExcelConfig(file_path: str) -> Dict[List[str], List[List[str]]]:
    df = pd.read_excel(file_path)
    df = df.fillna('')
    df["name"] = df["Title"] + " " + df["FirstName"] + " " + df["LastName"]
    df["name"] = df["name"].str.strip()
    df["name"] = df["name"]
    df["name"] = df["name"].str.upper()
    df["OrganisationName"] = df["OrganisationName"].str.strip()
    df["OrganisationName"] = df["OrganisationName"].str.upper()

    fields = ["name", "OrganisationName"]
    values = df[fields].values.tolist()
    return {
        "fields": fields,
        "values": values
    }

def readCSVConfig(file_path: str) -> Dict[List[str], List[List[str]]]:
    with open(file_path, encoding='utf8') as file:
        rows = list(csv.reader(file))
        if (len(rows) < 2):
            raise Exception(f"Invalid fields file '{file_path}'")
        return {
            "fields": rows[0],
            "values": rows[1:]
        }


def readTXTConfig(file_path: str) -> List[str]:
    with open(file_path, encoding='utf8') as file:
        rows = file.read().splitlines()
        if (len(rows) < 1):
            raise Exception(f"Invalid fields file '{file_path}'")
        return rows
