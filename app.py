
import requests #libreria de python que permite hacer solicitudes HTTP

api_key = '8c9da465d252dbb823453ace018c0c6e' #API key que se genera al registrate a la api de openweathermap


user_input = input("Ingrese la ciudad: ") #input para ingresar e imprimir la ciudad a buscar 
print(user_input)

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

#haciendo la primera solicitud, la url utilizada es un endpoint 
#el resultado de la solicitud se guarda en la variable weather_data 