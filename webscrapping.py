import requests
from bs4 import BeautifulSoup

# URL de la página que queremos raspar
url = 'https://news.ycombinator.com/'

# Realizamos la petición a la web
response = requests.get(url)
# Verificamos que la petición se haya realizado correctamente con response.status_code == 200
if response.status_code == 200:
    # Creamos el objeto BeautifulSoup y especificamos el parser HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Buscamos todos los elementos que contengan un título de noticia.
    # En este caso, los títulos de las noticias están en elementos de tipo 'a' con clase 'titlelink'
    titles = soup.find_all('span', class_='titleline')
    palabra = "Hacker"
    cont =  soup.get_text().lower().count(palabra.lower())
    Url = soup.find_all('a', href=True)
    Contador = 0
    # Imprimimos los títulos encontrados
    for title in titles:
        print(title.text.lower()) 
    for url in Url:
        Contador +=1
        print(f" {Contador} ___ {url['href']}")


    if cont == 0:
        
        print(f"========== La palabra {palabra} no se ha encontrado ==========")
    else:
        
        print (f"========== La palabra {palabra} se ha encontrado {cont} veces ==========")

            

else:
    print('Error en la petición:', response.status_code)