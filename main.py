from packages import csv_json as cvj

user = input("Coloca el nombre de un pais: ")
call = cvj.csv_to_dict("data.csv", user)
print(call)
