df <- data.frame(
  Nombre = c("Logitech g305", "Newskill Hanshi", "iPhone 13", "Pixel 9"),
  Categoria = c("Periférico", "Periférico", "Teléfono", "Teléfono"),
  Precio = c(59.99, 39.99, 799.00, 699.00)
)

print("Productos de la categoría Teléfono:")
telefonos <- subset(df, Categoria == "Teléfono")
print(telefonos)

print("-----------------")
print("Precio medio de los teléfonos:")

precio_medio_telefonos <- mean(telefonos$Precio)
print(precio_medio_telefonos)