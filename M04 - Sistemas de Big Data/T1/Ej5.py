import requests
from bs4 import BeautifulSoup

# 1️⃣ URL de la página principal
url = "http://books.toscrape.com/"

# 2️⃣ Descargar el contenido HTML
response = requests.get(url)

# Verificar que la petición fue exitosa (código 200)
if response.status_code == 200:
    # 3️⃣ Parsear el HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # 4️⃣ Buscar todos los artículos (cada libro está dentro de <article class="product_pod">)
    libros = soup.find_all("article", class_="product_pod")

    # 5️⃣ Recorrer y extraer título y precio
    for libro in libros:
        # El título está en el atributo 'title' del enlace dentro de <h3>
        titulo = libro.h3.a["title"]

        # El precio está dentro de <p class="price_color">
        precio = libro.find("p", class_="price_color").text

        print(f"Título: {titulo}  |  Precio: {precio}")

else:
    print("❌ Error al acceder a la página:", response.status_code)
