import matplotlib.pyplot as plt
import csv_json as cvj

def barras(tupla):
    main_color = "#0B0F17"
    label, value = tupla
    fig, ax = plt.subplots(facecolor='lightblue')
    ax.set_facecolor(main_color)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.bar(label, value, color='white')
    fig.patch.set_facecolor(main_color)
    plt.title("Población a través de los años", color="white")
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors=main_color)
    plt.show()


new_dictionary = cvj.csv_to_dict("../data.csv")
new_dictionary_country = cvj.find_country(new_dictionary, "India")
new_lists = cvj.population_kv(new_dictionary_country)
grafica_barras = barras(new_lists)
