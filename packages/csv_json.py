import csv


def csv_to_dict(path):
    new_dict = []
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
                        pass
        return new_dict
    

def find_country(dict, name):
    for country in dict:
        if country["Country"] == name:
            return country
        else:
            None


def population_kv(dictionary):
    population_dict = {
        "2022": dictionary["2022 Population"],
        "2020": dictionary["2020 Population"],
        "2015": dictionary["2015 Population"],
        "2010": dictionary["2010 Population"],
        "2000": dictionary["2000 Population"],
        "1990": dictionary["1990 Population"],
        "1980": dictionary["1980 Population"],
        "1970": dictionary["1970 Population"]
    }
    keys = [item for item in population_dict.keys()]
    values = [item for item in population_dict.values()]
    return keys, values