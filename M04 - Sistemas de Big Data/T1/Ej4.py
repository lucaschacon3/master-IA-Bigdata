import spacy  # 1️⃣ Importar la librería

# 2️⃣ Cargar el modelo de lenguaje español
nlp = spacy.load("es_core_news_sm")

# 3️⃣ Definir el texto a analizar
texto = "Pedro Sánchez se reunió con Elon Musk en Madrid para hablar de tecnología e innovación."

# 4️⃣ Procesar el texto con el modelo
doc = nlp(texto)

# 5️⃣ Recorrer las entidades encontradas
print("=== ENTIDADES NOMBRADAS DETECTADAS ===")
for entidad in doc.ents:
    print(f"• {entidad.text}  →  {entidad.label_}")
