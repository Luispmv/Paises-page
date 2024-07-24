import matplotlib.pyplot as plt
# import csv_json as cv


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
    plt.savefig("images/barras.png")
    # plt.show()


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
    plt.savefig("images/progression.png")

def pie(dictionary, dictionary_item):
    main_color = "#0B0F17"
    percentage = dictionary_item["World Population Percentage"]
    suma = sum(population["2022 Population"] for population in dictionary)
    formatted_number = f"{suma:,}"
    values = [percentage, 100 - percentage]
    labels = [f"{dictionary_item['Country']} ({percentage}%)", f"Rest of the world ({100 - percentage}%)"]
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=[main_color, 'white'], textprops={'color': 'white'})
    ax.axis('equal')
    fig.patch.set_facecolor(main_color) 
    ax.set_facecolor(main_color) 
    # plt.title(f"Poblacion mundial de {formatted_number}", color='white') 
    # plt.show()
    plt.savefig("images/pie.png")



#Este codigo lo podemos pasar a main.py
# new_dictionary = cv.csv_to_dict("../data.csv")
# new_dictionary_country = cv.find_country(new_dictionary, "Mexico")
# new_lists = cv.population_kv(new_dictionary_country)
# # grafica_barras = barras(new_lists)
# # progression(new_dictionary_country["Density"])
# pie_chart = pie(new_dictionary, new_dictionary_country)
# print(pie_chart)