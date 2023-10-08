import requests
from bs4 import BeautifulSoup


# USER AGENT PARA PROTEGERNOS DE BANEOS
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}

# URL SEMILLA
url = 'https://stackoverflow.com/questions'

#Requerimiento al servidor

respuesta = requests.get(url, headers=headers)

#Parseio del arbol con beautiiful soup
soup = BeautifulSoup(respuesta.text)

contenedor_de_preguntas = soup.find(id="questions")
lista_de_preguntas = contenedor_de_preguntas.find_all('div', class_="s-post-summary")



for pregunta in lista_de_preguntas:
    texto_pregunta = pregunta.find('h3').text
    descripcion_pregunta=pregunta.find(class_='s-post-summary--content-excerpt').text
    descripcion_pregunta=descripcion_pregunta.replace('\n', '').replace('\r', '')#limpieza de texto
    print(texto_pregunta)
    print(descripcion_pregunta)