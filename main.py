from packages import csv_json as cvj

from fastapi import FastAPI

app = FastAPI()

country = "Mexico"
@app.get("/")
def run():
    call = cvj.csv_to_dict("data.csv")
    return call

dictionary = run()

@app.get("/Country")
def oneCountry():
    calling = cvj.find_country(dictionary, country)
    return calling