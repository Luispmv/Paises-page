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
    # plt.savefig("barras.png")
    plt.show()


def progression(n):
    main_color = "#0B0F17"
    data = int(n)
    x = list(range(data))
    y = [2 ** i for i in x] 
    plt.figure(figsize=(8, 6), facecolor=main_color)
    ax = plt.gca()  
    ax.set_facecolor(main_color)
    for spine in ax.spines.values():
        spine.set_visible(False)
    plt.plot(x, y, marker='o', color="white", linestyle='-', markersize=8)
    plt.title('Tasa de Crecimiento Poblacional', color="white")
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.grid(True)
    ax.tick_params(axis='x', colors="white")
    ax.tick_params(axis='y', colors="white") 
    ax.set_xlabel('Índice', color=main_color)
    ax.set_ylabel('Valor', color=main_color)
    # plt.show()
    plt.savefig("progression.png")

new_dictionary = cvj.csv_to_dict("../data.csv")
new_dictionary_country = cvj.find_country(new_dictionary, "Mexico")
new_lists = cvj.population_kv(new_dictionary_country)
# grafica_barras = barras(new_lists)
progression(new_dictionary_country["Density"])
