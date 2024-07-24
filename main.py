import os
from packages import csv_json as cvj
from packages import dataview as dtv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/images", StaticFiles(directory="images"), name="images")


country = "United States"
image = "https://www.google.com/maps/vt/data=biY_M2bGuTEXA-mtsjF1PuXt-g4h8ApuAl_2DVBZpdDV5Yj-EKALv1CWQSEzZu5JDBFPYMaR2VJ-F-lkeo3XHAMNOCBgsQoeJeifFfWrS83sPL23p5kXvSTC2jIqFSg-KMOst8oin7h-t7fa8nNOAtjJK_PwO7cSAVGSk9geegPsw-PIV1LJufllsXGG29EkY1K0zRwKT8XOf8zujxaQhluLO9Z2Hn2DvZfXQwadn6-6ph8TZMey2K5VWaJC176gfVEmFfGZeWWSHQ6IcL3r02DwFb9z6Q"
grafico_barras = "/images/barras.png"
grafico_progresion = "/images/progression.png"
grafico_pastel = "/images/pie.png"

@app.get("/")
def run():
    call = cvj.csv_to_dict("data.csv")
    return call

@app.get("/Country")
def oneCountry():
    dictionary = cvj.csv_to_dict("data.csv")  # Inicializar dictionary dentro de la función
    calling = cvj.find_country(dictionary, country)
    return calling


def create_plots():
    new_dictionary = cvj.csv_to_dict("data.csv")
    new_dictionary_country = cvj.find_country(new_dictionary, country)
    new_tuple = cvj.population_kv(new_dictionary_country)
    if not os.path.exists("images"):
        os.makedirs("images")
    bar_chart = dtv.barras(new_tuple)
    grow_chart = dtv.progression(new_dictionary_country["Density"])
    pie_chart = dtv.pie(new_dictionary, new_dictionary_country)
    return bar_chart, grow_chart, pie_chart

create_plots()

def render(dict_item):
    return f'<body style="background-color: #06080C; display: grid; place-items: center; font-family: Impact, Haettenschweiler;">\
    <main style="width: 100%; max-width: 1300px;">\
        <header style="display: flex; justify-content: space-around;">\
            <figure style="width: 75%; margin: 0;">\
                <img style="width: 100%; height: 100%;" src="{image}" alt="Grafico del pais">\
            </figure>\
            <aside style="background-color: #0B0F17; width: 25%; margin-left: 10px;">\
                <figure style="margin: 0; position: relative;">\
                    <img style="width: 100%; height: 170px;" src="https://flagpedia.net/data/flags/h80/mx.webp" alt="Country Flag">\
                    <div style="background-color: #0B0F17; color: white; position: absolute; top: 0; right: 0; padding: 0.7rem; text-align: center; border-bottom-left-radius: 40px;">\
                        <p style="margin: 0;">Rank</p>\
                        <p style="margin: 0;">{dict_item["Rank"]}</p>\
                    </div>\
                </figure>\
                <article style="color: white; padding-left: 1rem;">\
                    <p style="font-size: 30px;">{dict_item["Country"]}</p>\
                    <p style="font-size: 30px;">{dict_item["Capital"]}</p>\
                    <p style="font-size: 30px;">{dict_item["Continent"]}</p>\
                    <p style="font-size: 30px;">{dict_item["Area"]}</p>\
                    <p style="font-size: 30px;">{dict_item["World Population Percentage"]}</p>\
                </article>\
            </aside>\
        </header>\
        <footer style="display: flex; justify-content: space-between; gap: 10px;">\
            <figure style="width: 100%; height: 350px; background-color: #0B0F17; margin-left: 0px; margin-right: 0px;"><img style="width: 100%; height: 100%; object-fit:contain" src="{grafico_barras}" alt="grafico_barras"></figure>\
            <figure style="width: 100%; height: 350px; background-color: #0B0F17; margin-left: 0px; margin-right: 0px;"><img style="width: 100%; height: 100%; object-fit:contain" src="{grafico_progresion}" alt="grafico_progresion"></figure>\
            <figure style="width: 100%; height: 350px; background-color: #0B0F17; margin-left: 0px; margin-right: 0px;"><img style="width: 100%; height: 100%; object-fit:contain" src="{grafico_pastel}" alt="grafico_progresion"></figure>\
        </footer>\
    </main>\
</body>'

@app.get("/Template", response_class=HTMLResponse)
def renderize():
    dictionary = cvj.csv_to_dict("data.csv")  
    dict_item = cvj.find_country(dictionary, country) 
    return render(dict_item)
