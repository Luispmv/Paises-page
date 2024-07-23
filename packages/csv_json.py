import csv
import json


def csv_to_dict(path, name):
    new_dict = []
    errors = []
    with open(path,"r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        column = next(reader)

        for item in reader:
            union = dict(zip(column, item))
            new_dict.append(union)

        for pais in new_dict:
            for key, value in pais.items():
                if isinstance(value, str) and value.isdigit():
                    pais[key] = int(value)
                elif isinstance(value, str):
                    try:
                        pais[key] = float(value)
                    except ValueError as error:
                        errors.append(error)
        errors.clear()

        for item in new_dict:
            if item["Country"] == name:
                new_json = json.dumps(item, indent=4)
                return new_json
        return None

